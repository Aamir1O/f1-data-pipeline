import fastf1
import pandas as pd
import os

BASE_DIR = os.path.expanduser("~/airflow_f1")

def extract(year=2026, round_number=7):
    # Enable cache
    os.makedirs("/tmp/fastf1_cache", exist_ok=True)
    fastf1.Cache.enable_cache("/tmp/fastf1_cache")

    # Load race session
    session = fastf1.get_session(year, round_number, "R")
    session.load()

    # Get lap data
    laps = session.laps[
        ["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "Position"]
    ].copy()

    laps["LapTime"] = laps["LapTime"].dt.total_seconds()
    laps["race_round"] = round_number
    laps["year"] = year

    # Create output directory
    raw_dir = os.path.join(BASE_DIR, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)

    # Save CSV
    output_file = os.path.join(raw_dir, "laps_raw.csv")
    laps.to_csv(output_file, index=False)

    print(f"Extracted {len(laps)} laps")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    extract()
