from flask import Flask, jsonify, request, abort
from teacherDAO import teacherDAO
from studentDAO import studentDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "School API Running"

# -------------------------
# TEACHER ROUTES
# -------------------------

@app.route('/teachers')
def getAllTeachers():
    return jsonify(teacherDAO.getAll())

@app.route('/teachers/<int:id>')
def getTeacher(id):
    teacher = teacherDAO.findByID(id)
    return jsonify(teacher)

@app.route('/teachers', methods=['POST'])
def createTeacher():
    if not request.json:
        abort(400)

    teacher = {
        "name": request.json["name"],
        "class_name": request.json["class_name"]
    }

    return jsonify(teacherDAO.create(teacher))

@app.route('/teachers/<int:id>', methods=['PUT'])
def updateTeacher(id):
    teacher = teacherDAO.findByID(id)
    if not teacher:
        abort(404)

    data = request.json
    teacher["name"] = data.get("name", teacher["name"])
    teacher["class_name"] = data.get("class_name", teacher["class_name"])

    teacherDAO.update(id, teacher)
    return jsonify(teacher)

@app.route('/teachers/<int:id>', methods=['DELETE'])
def deleteTeacher(id):
    teacherDAO.delete(id)
    return jsonify({"done": True})

# -------------------------
# STUDENT ROUTES
# -------------------------

@app.route('/students')
def getAllStudents():
    return jsonify(studentDAO.getAll())

@app.route('/students/<int:id>')
def getStudent(id):
    return jsonify(studentDAO.findByID(id))

@app.route('/students', methods=['POST'])
def createStudent():
    if not request.json:
        abort(400)

    student = {
        "name": request.json["name"],
        "class_name": request.json["class_name"],
        "teacher_id": request.json["teacher_id"],
        "qualification_level": request.json["qualification_level"]
    }

    return jsonify(studentDAO.create(student))

@app.route('/students/<int:id>', methods=['PUT'])
def updateStudent(id):
    student = studentDAO.findByID(id)
    if not student:
        abort(404)

    data = request.json
    student["name"] = data.get("name", student["name"])
    student["class_name"] = data.get("class_name", student["class_name"])
    student["teacher_id"] = data.get("teacher_id", student["teacher_id"])
    student["qualification_level"] = data.get("qualification_level", student["qualification_level"])

    studentDAO.update(id, student)
    return jsonify(student)

@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    studentDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)




