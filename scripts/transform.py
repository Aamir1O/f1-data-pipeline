import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.expanduser("~/airflow_f1")


def transform():
    # Read raw data
    raw_file = os.path.join(BASE_DIR, "data", "raw", "laps_raw.csv")
    df = pd.read_csv(raw_file)
    logging.info(f"Loaded {len(df)} rows")

    # Drop rows with missing lap times
    df = df.dropna(subset=["LapTime"])
    logging.info(f"After dropping nulls: {len(df)} rows")

    # Remove outlier laps (safety car, pit laps etc.)
    df = df[df["LapTime"] < df["LapTime"].quantile(0.95)]
    logging.info(f"After removing outliers: {len(df)} rows")

    # Rename columns to snake_case
    df.columns = [c.lower() for c in df.columns]

    # Save clean data
    output_file = os.path.join(BASE_DIR, "data", "clean_laps.csv")
    df.to_csv(output_file, index=False)

    logging.info(f"Transform complete. Saved to {output_file}")


if __name__ == "__main__":
    transform()
