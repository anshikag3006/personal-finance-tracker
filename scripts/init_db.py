import sqlite3
from pathlib import Path

db_path = Path("db/finance.db")
schema_path = Path("sql/schema.sql")

db_path.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON;")

schema_sql = schema_path.read_text()
conn.executescript(schema_sql)

conn.close()

print(f"✅ Database initialized successfully at: {db_path.resolve()}")