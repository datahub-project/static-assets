#!/usr/bin/env node
/**
 * sanitize-versions.js
 * Runs the full MDX/URN sanitization pipeline on one or all versioned_docs directories.
 *
 * Usage:
 *   node sanitize-versions.js                    # all versions except 1.3.0
 *   node sanitize-versions.js version-1.1.0      # specific version
 */

const fs = require('fs');
const path = require('path');

// ─── Configuration ────────────────────────────────────────────────────────────

const VERSIONED_DOCS = path.join(__dirname, '..', 'versioned_docs');
const TARGET_VERSIONS = process.argv[2]
  ? [process.argv[2]]
  : fs.readdirSync(VERSIONED_DOCS).filter(d => d !== 'version-1.3.0' && d.startsWith('version-'));

// HTML/JSX tags that should be unescaped from &lt;TAG&gt; → <TAG>
const UNESCAPE_TAGS = new Set([
  'Tabs', 'TabItem', 'FeatureAvailability',
  'div', 'span', 'p', 'a', 'strong', 'em', 'b', 'i',
  'details', 'summary',
  'table', 'thead', 'tbody', 'tr', 'td', 'th',
  'ul', 'ol', 'li',
  'img', 'br', 'hr',
  'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
  'code', 'pre',
  'note', 'warning', 'info', 'tip', 'caution',
]);

// Bare URN pattern (no surrounding backticks)
const URN_RE = /urn:li:[A-Za-z0-9.:_()/,@\-]+/g;
// Markdown link with URN href: [text](urn:li:...)
const URN_LINK_RE = /\[([^\]]*)\]\(`{0,2}(urn:li:[^)`\s]*)`{0,2}\)/g;
// &lt;TAG attrs&gt; or &lt;/TAG&gt;
const HTML_ENTITY_TAG_RE = /&lt;(\/?)([\w][\w-]*)([^&>]*)&gt;/g;
// <instance.name> or similar dotted JSX-like expressions in text
const DOTTED_TAG_RE = /<([A-Za-z][A-Za-z0-9]*\.[A-Za-z][A-Za-z0-9]*)([^>]*)>/g;
// Spurious backtick-wrapping of URNs inside code blocks
const WRAPPED_URN_IN_CODE_RE = /`(urn:li:[^`]+)`/g;
// &lt;Tab&gt; typo (missing 's')
const TAB_TYPO_OPEN_RE = /&lt;Tab&gt;/g;
const TAB_TYPO_CLOSE_RE = /<\/Tab>(\s*)$/gm;

// ─── Fenced code block splitter ───────────────────────────────────────────────

function splitContent(text) {
  const segments = [];
  const lines = text.split('\n');
  let inFence = false;
  let fenceChar = '';
  let fenceLen = 0;
  let buf = [];
  let isCode = false;

  for (const line of lines) {
    if (!inFence) {
      const m = line.match(/^[ \t]{0,3}(`{3,}|~{3,})[^\r]*/);
      if (m) {
        if (buf.length) segments.push({ text: buf.join('\n'), isCode });
        buf = [line];
        fenceChar = m[1][0];
        fenceLen = m[1].length;
        inFence = true;
        isCode = true;
      } else {
        buf.push(line);
      }
    } else {
      buf.push(line);
      const m = line.match(/^[ \t]{0,3}(`{3,}|~{3,})\s*$/);
      if (m && m[1][0] === fenceChar && m[1].length >= fenceLen) {
        segments.push({ text: buf.join('\n'), isCode: true });
        buf = [];
        inFence = false;
        isCode = false;
      }
    }
  }
  if (buf.length) segments.push({ text: buf.join('\n'), isCode });
  return segments;
}

// ─── Inline-code-span aware URN wrapper ───────────────────────────────────────

function wrapBareUrns(text) {
  // Track backtick spans to skip already-wrapped URNs
  const result = [];
  let i = 0;
  while (i < text.length) {
    // Count consecutive backticks
    if (text[i] === '`') {
      let j = i;
      while (j < text.length && text[j] === '`') j++;
      const tick = text.slice(i, j);
      // Find matching closing ticks
      let k = j;
      let found = false;
      while (k < text.length) {
        if (text[k] === '`') {
          let l = k;
          while (l < text.length && text[l] === '`') l++;
          if (l - k === tick.length) { k = l; found = true; break; }
          k = l;
        } else k++;
      }
      if (found) {
        result.push(text.slice(i, k));
        i = k;
      } else {
        result.push(tick);
        i = j;
      }
    } else {
      // Accumulate plain text until next backtick
      let j = i;
      while (j < text.length && text[j] !== '`') j++;
      const chunk = text.slice(i, j);
      result.push(chunk.replace(URN_RE, m => `\`${m}\``));
      i = j;
    }
  }
  return result.join('');
}

// ─── Transform a non-code segment ─────────────────────────────────────────────

function transformText(text) {
  // 1. Convert markdown links with URN hrefs to inline code
  text = text.replace(URN_LINK_RE, (_, label, urn) =>
    label ? `${label} (\`${urn}\`)` : `\`${urn}\``
  );

  // 2. Unescape &lt;TAG&gt; → <TAG> for known HTML/JSX tags
  text = text.replace(HTML_ENTITY_TAG_RE, (match, slash, name, attrs) => {
    if (UNESCAPE_TAGS.has(name)) return `<${slash}${name}${attrs}>`;
    return match;
  });

  // 3. Fix &lt;Tab&gt; typo → <Tabs>
  text = text.replace(TAB_TYPO_OPEN_RE, '<Tabs>');
  text = text.replace(TAB_TYPO_CLOSE_RE, (_, space) => `</Tabs>${space}`);

  // 4. Escape dotted JSX-like expressions that MDX misparses: <foo.bar> → &lt;foo.bar&gt;
  text = text.replace(DOTTED_TAG_RE, (match, name, attrs) => {
    // Only escape if not already inside a JSX context (i.e. in plain text)
    return `&lt;${name}${attrs}&gt;`;
  });

  // 5. Wrap bare URNs in backticks
  text = wrapBareUrns(text);

  return text;
}

// ─── Transform a code-block segment ──────────────────────────────────────────

function transformCode(text) {
  // Remove spurious backtick-wrapping of URNs that was added by earlier runs
  return text.replace(WRAPPED_URN_IN_CODE_RE, '$1');
}

// ─── Fix features.md import paths ─────────────────────────────────────────────

function fixFeaturesImports(text) {
  // Escaped underscore in import: @site/src/pages/docs/\_components → _components
  return text.replace(
    /@site\/src\/pages\/docs\\\/_components/g,
    '@site/src/pages/docs/_components'
  );
}

// ─── Process a single file ────────────────────────────────────────────────────

function processFile(filePath) {
  let original;
  try { original = fs.readFileSync(filePath, 'utf8'); } catch { return false; }

  let text = original;

  // Fix features.md imports everywhere
  text = fixFeaturesImports(text);

  const segments = splitContent(text);
  const transformed = segments.map(seg =>
    seg.isCode ? transformCode(seg.text) : transformText(seg.text)
  ).join('\n');

  // Stitch: splitContent uses '\n' join, restore with one join
  const out = transformed;

  if (out !== original) {
    fs.writeFileSync(filePath, out, 'utf8');
    return true;
  }
  return false;
}

// ─── Walk a directory ─────────────────────────────────────────────────────────

function walkDir(dir, fn) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walkDir(full, fn);
    else if (entry.isFile() && /\.(md|mdx)$/.test(entry.name)) fn(full);
  }
}

// ─── Main ─────────────────────────────────────────────────────────────────────

let totalFiles = 0;
let totalModified = 0;

for (const versionDir of TARGET_VERSIONS) {
  const versionPath = path.join(VERSIONED_DOCS, versionDir);
  if (!fs.existsSync(versionPath)) {
    console.log(`⚠ Skipping ${versionDir} — directory not found`);
    continue;
  }

  let vFiles = 0, vModified = 0;
  walkDir(versionPath, filePath => {
    vFiles++;
    if (processFile(filePath)) vModified++;
  });

  console.log(`${versionDir}: ${vModified}/${vFiles} files modified`);
  totalFiles += vFiles;
  totalModified += vModified;
}

console.log(`\nTotal: ${totalModified}/${totalFiles} files modified across ${TARGET_VERSIONS.length} versions`);
