import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./visiontrack.db")

def load_csvs(projects_csv: str, tasks_csv: str, costs_csv: str, scopes_csv: str):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
    with engine.begin() as conn:
        pd.read_csv(projects_csv).to_sql("projects", conn, if_exists="append", index=False)
        pd.read_csv(tasks_csv).to_sql("tasks", conn, if_exists="append", index=False)
        pd.read_csv(costs_csv).to_sql("costs", conn, if_exists="append", index=False)
        pd.read_csv(scopes_csv).to_sql("scope_changes", conn, if_exists="append", index=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python -m visiontrack.etl.load_sample_data <projects.csv> <tasks.csv> <costs.csv> <scopes.csv>")
        raise SystemExit(1)
    load_csvs(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
