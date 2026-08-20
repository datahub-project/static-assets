#!/usr/bin/env bash
#
# Wrap the finished Docusaurus build/ into Vercel's Build Output API (v3)
# layout at docs-archive/.vercel/output/, so that:
#
#     npx vercel deploy --prebuilt --prod
#
# uploads the already-built site without Vercel rebuilding it from source.
#
# Run build-archive.sh first to produce build/.
#
set -euo pipefail

ARCHIVE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BUILD_DIR="$ARCHIVE_DIR/build"
OUTPUT_DIR="$ARCHIVE_DIR/.vercel/output"

if [ ! -d "$BUILD_DIR" ] || [ ! -f "$BUILD_DIR/index.html" ]; then
  echo "ERROR: no build found at $BUILD_DIR — run scripts/deploy/build-archive.sh first." >&2
  exit 1
fi

echo ">> Packaging $BUILD_DIR -> $OUTPUT_DIR"
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR/static"

# Copy the entire static site into the Build Output API's static/ folder.
cp -R "$BUILD_DIR"/. "$OUTPUT_DIR/static/"

# Static-site config, plus 308s from /docs/X.Y.Z/ to each version's landing page
# (most versions have no page at the version root). Generated from versions.json;
# versions that already have a root page are skipped.
node - "$ARCHIVE_DIR" "$OUTPUT_DIR" <<'NODE'
const fs = require('fs');
const path = require('path');
const [archiveDir, outputDir] = process.argv.slice(2);

const versions = JSON.parse(fs.readFileSync(path.join(archiveDir, 'versions.json'), 'utf8'));
const staticDir = path.join(outputDir, 'static');

// landing pages, best first
const CANDIDATES = ['features', 'introduction'];
const routes = [];
const skipped = [];

for (const v of versions) {
  if (fs.existsSync(path.join(staticDir, 'docs', v, 'index.html'))) {
    skipped.push(`${v} (already has a root page)`);
    continue;
  }
  const landing = CANDIDATES.find((c) =>
    fs.existsSync(path.join(staticDir, 'docs', v, c, 'index.html'))
  );
  if (!landing) {
    skipped.push(`${v} (no landing page found)`);
    continue;
  }
  // dots escaped so they match literally
  routes.push({
    src: `^/docs/${v.replace(/\./g, '\\.')}/?$`,
    status: 308,
    headers: { Location: `/docs/${v}/${landing}` },
  });
}

// redirects first, then real files
const config = {
  version: 3,
  routes: [...routes, { handle: 'filesystem' }],
};

fs.writeFileSync(path.join(outputDir, 'config.json'), `${JSON.stringify(config, null, 2)}\n`);
console.log(`>> wrote ${routes.length} version-root redirects`);
for (const s of skipped) console.log(`   skipped ${s}`);
NODE

echo ">> Prebuilt output ready at $OUTPUT_DIR"
echo ">> Deploy with: (cd $ARCHIVE_DIR && npx vercel deploy --prebuilt --prod --yes --token=\$VERCEL_TOKEN)"
