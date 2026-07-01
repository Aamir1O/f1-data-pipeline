import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

def load():
    # Read clean data
    df = pd.read_csv('/home/batman/airflow_f1/data/clean_laps.csv')
    logging.info(f"Loading {len(df)} rows into database")

    # Connect to SQLite
    conn = sqlite3.connect('/home/batman/airflow_f1/data/f1.db')
    
    # Load into table
    df.to_sql('laps', conn, if_exists='replace', index=False)
    
    conn.close()
    logging.info("Load complete. Data in f1.db")

if __name__ == "__main__":
    load()
