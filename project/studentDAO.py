import mysql.connector
from dbconfig import mysql

class StudentDAO:
    def connect(self):
        return mysql.connector.connect(
            host=mysql['host'],
            user=mysql['user'],
            password=mysql['password'],
            database=mysql['database']
        )

    def getAll(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()
        db.close()
        return results

    def findById(self, id):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student WHERE id=%s", (id,))
        result = cursor.fetchone()
        db.close()
        return result

    def create(self, student):
        db = self.connect()
        cursor = db.cursor()
        sql = "INSERT INTO student (firstname, lastname, age) VALUES (%s, %s, %s)"
        values = (student["firstname"], student["lastname"], student["age"])
        cursor.execute(sql, values)
        db.commit()
        new_id = cursor.lastrowid
        db.close()
        return new_id

    def update(self, id, student):
        db = self.connect()
        cursor = db.cursor()
        sql = "UPDATE student SET firstname=%s, lastname=%s, age=%s WHERE id=%s"
        values = (student["firstname"], student["lastname"], student["age"], id)
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return cursor.rowcount

    def delete(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (id,))
        db.commit()
        db.close()
        return cursor.rowcount


studentDAO = StudentDAO()
