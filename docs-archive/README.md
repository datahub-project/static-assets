# DataHub Legacy Docs Archive

This directory contains the static archive for older, legacy versions of DataHub documentation (v0.10.5 through v1.3.0). 

To keep the main `datahub` repository lightweight and ensure fast CI/CD pipelines, these legacy versions have been decoupled and are hosted here. They are built using [Docusaurus 2](https://docusaurus.io/).

## Local Development

To run the archive locally, you will need Node.js (v18.x recommended).

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the Server
Because this archive contains over a dozen full versions of the documentation, it requires a higher memory heap to compile. You must set the `NODE_OPTIONS` environment variable before starting or building.
```bash
export NODE_OPTIONS=--max-old-space-size=8192
npm start
```

This command starts a local development server at `http://localhost:3000`.

#### ⚠️ Maintenance Note
Do not upgrade this archive to Docusaurus v3. These legacy versions contain historical MDX 1 syntax. Upgrading to v3 (MDX 2) will cause fatal parsing errors across thousands of older files. Treat this directory as a read-only time capsule unless fixing critical broken links or 404s.
