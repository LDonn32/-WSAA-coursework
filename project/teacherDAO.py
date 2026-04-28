import sqlite3
import dbconfig as cfg
from os import path

class TeacherDAO:
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
        sql = "SELECT * FROM teacher"
        cursor.execute(sql)
        results = cursor.fetchall()

        teachers = []
        for row in results:
            teachers.append(self.convertToDictionary(row))

        self.closeAll()
        return teachers

    def findByID(self, id):
        cursor = self.getcursor()
        sql = f"SELECT * FROM teacher WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchone()

        teacher = self.convertToDictionary(result)

        # Get students for this teacher
        sql2 = f"SELECT id, name, class_name, qualification_level FROM student WHERE teacher_id = {id}"
        cursor.execute(sql2)
        students = cursor.fetchall()

        teacher["students"] = []
        for s in students:
            teacher["students"].append({
                "id": s[0],
                "name": s[1],
                "class_name": s[2],
                "qualification_level": s[3]
            })

        self.closeAll()
        return teacher

    def create(self, teacher):
        cursor = self.getcursor()
        sql = f"""
            INSERT INTO teacher (name, class_name)
            VALUES ("{teacher.get('name')}", "{teacher.get('class_name')}")
        """
        cursor.execute(sql)
        self.connection.commit()

        teacher["id"] = cursor.lastrowid
        self.closeAll()
        return teacher

    def update(self, id, teacher):
        cursor = self.getcursor()
        sql = f"""
            UPDATE teacher SET 
                name = "{teacher.get('name')}",
                class_name = "{teacher.get('class_name')}"
            WHERE id = {id}
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = f"DELETE FROM teacher WHERE id = {id}"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, row):
        keys = ["id", "name", "class_name"]
        teacher = {}
        if row:
            for i, col in enumerate(row):
                teacher[keys[i]] = col
        return teacher
    

def update(self, id, teacher):
    cursor = self.db.cursor()
    sql = "UPDATE teacher SET name = ?, class_name = ? WHERE id = ?"
    values = [teacher['name'], teacher['class_name'], id]
    cursor.execute(sql, values)
    self.db.commit()
    return self.findByID(id)




teacherDAO = TeacherDAO()
