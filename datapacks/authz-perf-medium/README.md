# authz-perf-medium

Medium-scale authorization performance datapack for DataHub. Ingested via `datahub datapack load authz-perf-medium`.

## Contents

| File | Purpose |
|------|---------|
| `index.json` | Pack manifest (version, MCP file list) |
| `mcps/` | Metadata change proposals (~6378) |

Test oracles (`personas.json`, `benchmarks.json`) are maintained in the DataHub repository under `perf-test/authz-perf/fixture/` and are not part of this pack.

## Personas (17)

All personas use password = username (`persona-*` / `persona-*`).

| Persona | Stress focus |
|---------|----------------|
| `persona-admin` | Platform + direct user policy |
| `persona-zero-authz` | Baseline vs denied path |
| `persona-light-groups` … `persona-heavy-groups` | Group membership fanout (3–200 groups) |
| `persona-sso-groups` / `persona-native-groups` / `persona-dual-aspect` | SSO vs native membership aspects |
| `persona-direct-role` / `persona-role-via-groups` | Role inheritance |
| `persona-domain-policy-user` / `persona-multi-domain-policy` | Domain filter / multi-value DOMAIN |
| `persona-domain-owner` | Ownership-based checks |
| `persona-policy-direct` / `persona-platform-all-users` | Direct user / allUsers actors |
| `persona-group-policy-actor` | Group-based policy actor |

## Load

```bash
datahub datapack load authz-perf-medium
```

For local development before the registry URL is published:

```bash
datahub datapack load authz-perf-medium \
  --url "file://$(pwd)/datapacks/authz-perf-medium/index.json" \
  --trust-custom
```

## Benchmarks

Persona latency benchmarks are documented in the DataHub repository at `perf-test/authz-perf/README.md`.
