# Healthcare Dataset for DataHub

Patient hospital records loaded as a **forking data pipeline** (raw → staging → billing mart + demographics mart) with planted data quality issues for testing quality monitoring, circuit breaking, and selective pipeline halting.

Built from the [Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) on Kaggle — ~55k synthetic patient records with medical conditions, billing, and admission details.

---

## What's Included

```
healthcare/
├── healthcare.db             ← Pipeline with quality issues planted (committed, ~2MB)
├── create_db.py              ← Generates healthcare.db from source CSV
├── ingest.yaml               ← Ingests into DataHub
├── add_lineage.py            ← Adds pipeline lineage (auto-discovers URNs)
├── add_metadata.py           ← Adds tags, glossary terms, ownership
└── README.md                 ← You are here
```

> **Note:** Only one variant exists. Quality issues are always planted — they ARE the point of this dataset.

---

## Quick Start

```bash
# 1. Ingest into DataHub
datahub ingest -c ingest.yaml

# 2. Add pipeline lineage
python add_lineage.py

# 3. Add metadata
python add_metadata.py
```

---

## The Pipeline

```
raw_patients ──→ staging_patients ──┬──→ mart_billing
                                    └──→ mart_demographics
```

This is a **forking pipeline** — one source feeds two independent downstream marts. Quality issues in `raw_patients` propagate through staging into BOTH marts, but the impact differs:

- **mart_billing** is directly affected by negative billing amounts and date swaps (financial impact)
- **mart_demographics** is affected by invalid ages and NULL names (reporting impact)

A smart quality system should selectively halt based on which mart is impacted — not shut down everything.

---

## What's in the Database

### Tables (4 pipeline stages)

| Table | Rows | Description |
|---|---|---|
| `raw_patients` | ~55,500 | Source patient records with quality issues planted |
| `staging_patients` | ~55,500 | Standardized columns (lowercased, trimmed) — issues propagate through |
| `mart_billing` | ~55,500 | Financial view: billing amount, insurance, length of stay |
| `mart_demographics` | ~55,500 | Demographics view: age, gender, blood type, medical condition |

### Views (3 — for lineage)

| View | Lineage | Purpose |
|---|---|---|
| `v_staging_from_raw` | raw_patients → staging_patients | Shows the staging transformation |
| `v_billing_from_staging` | staging_patients → mart_billing | Shows the billing mart derivation |
| `v_demographics_from_staging` | staging_patients → mart_demographics | Shows the demographics mart derivation |

### Columns in raw_patients

| Column | Description |
|---|---|
| `name` | Patient name |
| `age` | Patient age at admission |
| `gender` | Male / Female |
| `blood_type` | Blood type (A+, B-, O+, etc.) |
| `medical_condition` | Diagnosis (Diabetes, Asthma, Cancer, etc.) |
| `date_of_admission` | Hospital admission date |
| `doctor` | Attending physician |
| `hospital` | Hospital name |
| `insurance_provider` | Insurance company |
| `billing_amount` | Total charge for services |
| `room_number` | Hospital room number |
| `admission_type` | Emergency / Elective / Urgent |
| `discharge_date` | Hospital discharge date |
| `medication` | Prescribed medication |
| `test_results` | Normal / Abnormal / Inconclusive |

---

## Planted Quality Issues

All issues are planted in `raw_patients` and propagate through the pipeline unchanged. A quality circuit breaker should catch them at the raw stage.

| Issue | What's Planted | Rows Affected | Impact on Marts |
|---|---|---|---|
| Negative billing | `billing_amount` set to negative values | ~2% (~1,100 rows) | mart_billing: negative revenue, wrong totals |
| NULL names | `name` set to NULL | ~1% (~555 rows) | mart_demographics: incomplete records |
| Invalid ages | Ages set to < 0 or > 120 | ~1.5% (~830 rows) | mart_demographics: impossible age values |
| Date swaps | `date_of_admission` and `discharge_date` swapped | ~0.5% (~275 rows) | mart_billing: negative length_of_stay |

**The selective halting challenge:** Negative billing affects `mart_billing` but NOT `mart_demographics`. Invalid ages affect `mart_demographics` but NOT `mart_billing`. A naive circuit breaker halts everything. A smart one halts only the affected downstream.

All issues use `random.seed(42)` for reproducibility.

---

## Metadata

### Tags

| Tag | Description | Attached To |
|---|---|---|
| `pii` | Contains patient names, ages, medical conditions | raw_patients, staging_patients, mart_demographics |
| `critical` | Business-critical, direct financial impact | mart_billing |
| `internal` | Internal use, lower severity if quality degrades | mart_demographics |
| `quality_monitored` | Active quality monitoring expected | raw_patients |
| `pipeline_stage` | Part of the raw → staging → mart pipeline | All 4 tables |

### Glossary Terms

| Term | Definition | Attached To |
|---|---|---|
| Billing Amount | Total charge for services. Must always be positive. Negative = data entry error. | raw_patients, mart_billing |
| Admission Date | When the patient was admitted. Must precede discharge date. | raw_patients, staging_patients |
| Length of Stay | discharge_date minus admission_date in days. Negative = date swap. | mart_billing |

### Ownership

| Team | Owns | Why |
|---|---|---|
| `clinical_team` | raw_patients, staging_patients | Responsible for source data quality |
| `finance_team` | mart_billing | Consumes billing data for revenue reporting |
| `research_team` | mart_demographics | Uses demographics for studies and analytics |

---

## Lineage in DataHub

`add_lineage.py` creates both table-to-table and view-to-table lineage:

**Table lineage (the pipeline flow):**
```
raw_patients → staging_patients → mart_billing
                                → mart_demographics
```

**View lineage (how transformations work):**
```
v_staging_from_raw ← raw_patients
v_billing_from_staging ← staging_patients
v_demographics_from_staging ← staging_patients
```

Click `mart_billing` → Lineage tab in DataHub to see the full chain.

---

## Generate from Scratch

```bash
# Download from: https://kaggle.com/datasets/prasad22/healthcare-dataset
# Extract the ZIP, then:

python create_db.py /path/to/csvs
```

The script loads the CSV, plants quality issues, creates pipeline stages, and builds views — all in one step. No flags needed (there's only one variant).

---

## Original Data Source

| | |
|---|---|
| **Dataset** | [Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) |
| **Author** | Prasad22 |
| **License** | CC0 1.0 (Public Domain) |
| **Records** | ~55,500 synthetic patient records |

> This is a synthetic (dummy) dataset — no real patient data is used. The data is CC0 licensed (public domain).

### What We Modified

- **Column names** normalized to snake_case (e.g., "Date of Admission" → `date_of_admission`)
- **Quality issues planted** in raw_patients: negative billing, NULL names, invalid ages, date swaps
- **Pipeline stages** created: staging_patients, mart_billing, mart_demographics (not in original CSV)
- **Views** created for DataHub lineage

---

## Troubleshooting

### Lineage shows one direction only

The fork (staging → billing + demographics) should show TWO downstream arrows from staging. If you only see one, re-run `python add_lineage.py` — it emits all 6 lineage edges.

### Quality issues not visible in mart tables

They should propagate automatically. Verify with:
```sql
sqlite3 healthcare.db "SELECT COUNT(*) FROM mart_billing WHERE billing_amount < 0"
```

### Tags show only one per table

This was a known issue with earlier versions of the metadata script. The current version batches all tags per table into a single emit. Re-run `python add_metadata.py`.

---

## All Available Commands

```bash
# ── Database generation ──
python create_db.py /path/to/csvs         # Creates healthcare.db

# ── Ingestion ──
datahub ingest -c ingest.yaml

# ── Lineage ──
python add_lineage.py                      # Add pipeline lineage
python add_lineage.py --dry-run            # Preview only

# ── Metadata ──
python add_metadata.py                     # Add tags, glossary, ownership
python add_metadata.py --dry-run           # Preview only
```