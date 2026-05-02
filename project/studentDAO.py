import sqlite3
from dbconfig import get_connection

class StudentDAO:

    def getAll(self):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def findById(self, id):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def create(self, student):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student (firstname, lastname, age) VALUES (?, ?, ?)",
            (student["firstname"], student["lastname"], student["age"])
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, id, student):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE student SET firstname=?, lastname=?, age=? WHERE id=?",
            (student["firstname"], student["lastname"], student["age"], id)
        )
        conn.commit()
        conn.close()
        return cursor.rowcount

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount

studentDAO = StudentDAO()

















