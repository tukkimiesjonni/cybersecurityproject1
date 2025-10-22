import sqlite3

DATABASE = "database.db"
SCHEMA_FILE = "schema.sql"

# Connect to SQLite (will create the file if it doesn't exist)
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Read and execute schema.sql
with open(SCHEMA_FILE, "r") as f:
    schema_sql = f.read()

cursor.executescript(schema_sql)  # executes multiple SQL statements at once
conn.commit()
conn.close()

print(f"Database '{DATABASE}' initialized successfully.")
