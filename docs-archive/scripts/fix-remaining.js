#!/usr/bin/env node
/**
 * fix-remaining.js — targeted fixes after bulk sanitization:
 *   1. Remove explicit @site/src/pages/docs/_components/ imports (mocked by pages plugin)
 *   2. Replace bare <Tab> → <Tabs> and </Tab> → </Tabs> typos (literal, not entity-encoded)
 */
const fs = require('fs');
const path = require('path');

const VERSIONED_DOCS = path.join(__dirname, '..', 'versioned_docs');

// Imports to strip — these live in src/pages/ and get mocked to null
const STALE_IMPORT_RE = /^import\s+\w+\s+from\s+'@site\/src\/pages\/docs\/_components\/[^']+';?\s*\n?/gm;

// <Tab> on its own line (typo for <Tabs>)
const TAB_OPEN_LITERAL_RE = /^<Tab>$/gm;
// </Tab> on its own line (typo for </Tabs>)
const TAB_CLOSE_LITERAL_RE = /^<\/Tab>$/gm;

let totalFiles = 0;
let totalModified = 0;

function processFile(filePath) {
  let text;
  try { text = fs.readFileSync(filePath, 'utf8'); } catch { return; }

  const original = text;

  // 1. Remove stale src/pages imports
  text = text.replace(STALE_IMPORT_RE, '');

  // 2. Fix <Tab> → <Tabs> typos (literal, already unescaped)
  text = text.replace(TAB_OPEN_LITERAL_RE, '<Tabs>');
  text = text.replace(TAB_CLOSE_LITERAL_RE, '</Tabs>');

  totalFiles++;
  if (text !== original) {
    fs.writeFileSync(filePath, text, 'utf8');
    totalModified++;
    console.log('  fixed:', path.relative(VERSIONED_DOCS, filePath));
  }
}

function walkDir(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walkDir(full);
    else if (/\.(md|mdx)$/.test(entry.name)) processFile(full);
  }
}

walkDir(VERSIONED_DOCS);
console.log(`\nFixed ${totalModified}/${totalFiles} files`);
