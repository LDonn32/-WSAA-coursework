import sqlite3
from dbconfig import get_db_path

def create_tables():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database created at: {get_db_path()}")

if __name__ == "__main__":
    create_tables()


