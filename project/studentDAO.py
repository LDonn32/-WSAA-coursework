import sqlite3
import dbconfig as cfg
from os import path

class StudentDAO:
    connection = ""
    cursor = ""
    database = ""

    def __init__(self):
        self.database = cfg.mysql['database']

    def getcursor(self):
        ROOT = path.dirname(path.realpath(__file__))
        self.connection = sqlite3.connect(path.join(ROOT, self.database))
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()

        students = []
        for row in results:
            students.append(self.convertToDictionary(row))

        self.closeAll()
        return students

    def findByID(self, id):
        cursor = self.getcursor()
        sql = f"SELECT * FROM student WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchone()

        student = self.convertToDictionary(result)
        self.closeAll()
        return student

    def create(self, student):
        cursor = self.getcursor()
        sql = f"""
            INSERT INTO student (name, class_name, teacher_id, qualification_level)
            VALUES ("{student.get('name')}", "{student.get('class_name')}", 
                    {student.get('teacher_id')}, "{student.get('qualification_level')}")
        """
        cursor.execute(sql)
        self.connection.commit()

        student["id"] = cursor.lastrowid
        self.closeAll()
        return student

    def update(self, id, student):
        cursor = self.getcursor()
        sql = f"""
            UPDATE student SET 
                name = "{student.get('name')}",
                class_name = "{student.get('class_name')}",
                teacher_id = {student.get('teacher_id')},
                qualification_level = "{student.get('qualification_level')}"
            WHERE id = {id}
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = f"DELETE FROM student WHERE id = {id}"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, row):
        keys = ["id", "name", "class_name", "teacher_id", "qualification_level"]
        student = {}
        if row:
            for i, col in enumerate(row):
                student[keys[i]] = col
        return student


def update(self, id, student):
    cursor = self.db.cursor()
    sql = """UPDATE student 
             SET name = ?, class_name = ?, teacher_id = ?, qualification_level = ?
             WHERE id = ?"""
    values = [
        student['name'],
        student['class_name'],
        student['teacher_id'],
        student['qualification_level'],
        id
    ]
    cursor.execute(sql, values)
    self.db.commit()
    return self.findByID(id)



studentDAO = StudentDAO()
