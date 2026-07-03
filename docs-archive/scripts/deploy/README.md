# Docs archive — deploy scripts

This archive builds many documentation versions with Docusaurus in a single
site. That build is memory-intensive and can exceed the memory available on
hosted build environments. To avoid that, we build the static site in an
environment we control and then upload the finished output to Vercel, so Vercel
serves it without rebuilding.

## Flow

```bash
# 1. Build the static site -> build/
./scripts/deploy/build-archive.sh

# 2. Wrap build/ into Vercel's Build Output API layout -> .vercel/output/
./scripts/deploy/package-prebuilt.sh

# 3. Upload the prebuilt output (Vercel serves it as-is, no rebuild).
export VERCEL_TOKEN=...            # provide via a secret; never commit it
export VERCEL_ORG_ID=...
export VERCEL_PROJECT_ID=...
npx vercel deploy --prebuilt --prod --yes --token="$VERCEL_TOKEN"
```

## Why `--prebuilt`

`--prebuilt` tells Vercel to upload the contents of `.vercel/output/` directly
instead of building from source. This keeps the build in an environment with
enough memory and avoids rebuilding on deploy.

## Vercel project settings

- The archive is its own Vercel project, served at `archive.docs.datahub.com`.
- Git-triggered deploys should be disabled for that project so a push does not
  start a build from source. Deploys are expected to run via the CLI with
  `--prebuilt`.

## Committed vs generated

- **Committed:** documentation source (`versioned_docs/`, configs) and these
  scripts.
- **Generated (git-ignored):** `build/`, `.docusaurus/`, `node_modules/`,
  `.vercel/`.
