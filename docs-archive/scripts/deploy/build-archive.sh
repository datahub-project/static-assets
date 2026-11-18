#!/usr/bin/env bash
#
# Build the docs archive with the memory settings needed for the full
# multi-version Docusaurus build.
#
# Output lands in docs-archive/build/ (Docusaurus static output).
# Run scripts/deploy/package-prebuilt.sh next to wrap it for Vercel.
#
set -euo pipefail

ARCHIVE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ARCHIVE_DIR"

# Raise the V8 heap limit and serialize SSR to keep peak memory manageable.
# The server compile needs well above the default heap; run this on a machine
# (or runner) with enough RAM to back the limit below, or provide swap.
# 24 GB: 20 GB ran out of memory once the archive reached 18 versions (1.8.0).
# Needs a machine with >=32 GB RAM; quit other heavy apps while it runs.
export NODE_OPTIONS="--max-old-space-size=24576"
export DOCUSAURUS_SSR_CONCURRENCY=1

echo ">> Building docs archive in $ARCHIVE_DIR"
rm -rf build .docusaurus
npm run build
echo ">> Build complete -> $ARCHIVE_DIR/build"
