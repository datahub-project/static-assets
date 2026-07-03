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

# Minimal valid config for a purely static site. Vercel serves static/ as-is
# and uses the generated 404.html for not-found routes automatically.
cat > "$OUTPUT_DIR/config.json" <<'JSON'
{
  "version": 3
}
JSON

echo ">> Prebuilt output ready at $OUTPUT_DIR"
echo ">> Deploy with: (cd $ARCHIVE_DIR && npx vercel deploy --prebuilt --prod --yes --token=\$VERCEL_TOKEN)"
