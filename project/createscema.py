#!/usr/bin/env python3
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "students.db")

def create_schema():
    print("Using DB at:", DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      address TEXT,
      email TEXT,
      course TEXT
    );
    """)

    # Optional: insert a couple of test rows if table is empty
    cur.execute("SELECT count(*) FROM students")
    count = cur.fetchone()[0]
    if count == 0:
        cur.executemany(
            "INSERT INTO students (name, address, email, course) VALUES (?, ?, ?, ?)",
            [
                ("Alice Example", "1 Main St", "alice@example.com", "Math"),
                ("Bob Example", "2 High St", "bob@example.com", "History")
            ]
        )
        print("Inserted sample rows")

    conn.commit()
    conn.close()
    print("Schema created/verified")

if __name__ == "__main__":
    create_schema()
