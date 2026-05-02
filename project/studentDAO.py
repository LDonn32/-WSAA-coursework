import sqlite3
from dbconfig import get_db_path

def get_connection():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row  # Enables dict-like access
    return conn

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None
def create_student(student):
    conn = get_connection()
    cur = conn.cursor()

    # find the smallest missing id
    cur.execute("SELECT id FROM students ORDER BY id")
    existing_ids = [row["id"] for row in cur.fetchall()]

    new_id = 1
    for i in existing_ids:
        if i == new_id:
            new_id += 1
        else:
            break

    cur.execute("""
        INSERT INTO students (id, name, address, email, course)
        VALUES (?, ?, ?, ?, ?)
    """, (new_id, student['name'], student['address'], student['email'], student['course']))

    conn.commit()
    conn.close()
    return new_id


def update_student(student_id, student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name = ?, address = ?, email = ?, course = ?
        WHERE id = ?
    ''', (student['name'], student['address'], student['email'], student['course'], student_id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0











