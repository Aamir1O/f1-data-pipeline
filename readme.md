# F1 Data Pipeline

A production-style data engineering pipeline built on Formula 1 data.

## Stack
- **Python** — extract, transform, load scripts
- **FastF1** — F1 telemetry and lap data API
- **SQLite** — local data storage
- **Apache Airflow** — pipeline orchestration and scheduling

## Pipeline Architecture
```
FastF1 API → extract.py → raw CSV → transform.py → clean CSV → load.py → SQLite
↑
Orchestrated by Airflow DAG (daily schedule)
```

## Project Structure
```
airflow_f1/
├── dags/
│   └── f1_etl.py          # Airflow DAG definition
├── scripts/
│   ├── extract.py          # Pull lap data from FastF1
│   ├── transform.py        # Clean nulls, remove outliers
│   └── load.py             # Write to SQLite database
└── data/
├── raw/                # Raw FastF1 output
└── f1.db               # Final database
```

## What It Does

1. **Extract** — pulls lap-by-lap data from the FastF1 API for a given race round
2. **Transform** — removes null lap times, filters outlier laps (pit stops, safety car)
3. **Load** — writes 1100+ clean laps into a SQLite database
4. **Schedule** — Airflow DAG runs daily, logs every step, tracks task state

## Setup

```bash
pip3 install apache-airflow fastf1 pandas
export AIRFLOW_HOME=~/airflow_f1
airflow db migrate
airflow webserver --port 8080 &
airflow scheduler &
```

Built by Aamir · 2026

Built by Aamir · 2026
