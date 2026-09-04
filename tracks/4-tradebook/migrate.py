import csv
import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
CSV_PATH = BASE / "data" / "trades.csv"
DB_PATH = BASE / "tradebook.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS trades")
    cur.execute("""
        CREATE TABLE trades (
            trade_id TEXT PRIMARY KEY,
            timestamp TEXT,
            ticker TEXT,
            side TEXT,
            quantity REAL,
            price REAL,
            notional REAL,
            desk TEXT,
            trader TEXT
        )
    """)

    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        rows = [
            (
                r["trade_id"], r["timestamp"], r["ticker"], r["side"],
                float(r["quantity"]), float(r["price"]), float(r["notional"]),
                r["desk"], r["trader"],
            )
            for r in reader
        ]

    cur.executemany(
        "INSERT INTO trades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows
    )
    conn.commit()
    conn.close()
    print(f"Loaded {len(rows)} trades into {DB_PATH}")

if __name__ == "__main__":
    main()
