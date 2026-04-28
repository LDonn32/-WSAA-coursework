from flask import Flask, jsonify, request, abort
from teacherDAO import teacherDAO
from studentDAO import studentDAO


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return "School API Running"

# -------------------------
# TEACHER ROUTES
# -------------------------


# get all teachers to display in the dropdown menu
@app.route('/teachers')
def getAllTeachers():
    return jsonify(teacherDAO.getAll())


# get a specific teacher by ID to display in the teacher details section
@app.route('/teachers/<int:id>')
def getTeacher(id):
    teacher = teacherDAO.findByID(id)
    return jsonify(teacher)

# create a new teacher when the form is submitted
@app.route('/teachers', methods=['POST'])
def createTeacher():
    if not request.json:
        abort(400)

    # create a new teacher object from the form data and save it to the database
    teacher = {
        "name": request.json["name"],
        "class_name": request.json["class_name"]
    }

    return jsonify(teacherDAO.create(teacher))


# update an existing teacher when the form is submitted
@app.route('/teachers/<int:id>', methods=['PUT'])
def updateTeacher(id):
    teacher = teacherDAO.findByID(id)
    if not teacher:
        abort(404)

    # update the teacher object with the new form data and save it to the database
    data = request.json
    teacher["name"] = data.get("name", teacher["name"])
    teacher["class_name"] = data.get("class_name", teacher["class_name"])

    teacherDAO.update(id, teacher)
    return jsonify(teacher)

# delete a teacher when the delete button is clicked
@app.route('/teachers/<int:id>', methods=['DELETE'])
def deleteTeacher(id):
    teacherDAO.delete(id)
    return jsonify({"done": True})


# update an existing teacher when the form is submitted
@app.route('/teachers/<int:id>', methods=['PUT'])
def update_teacher(id):
    teacher = request.json
    updated_teacher = teacherDAO.update(id, teacher)
    return jsonify(updated_teacher)




# -------------------------
# STUDENT ROUTES
# -------------------------

# get all students to display in the student list
@app.route('/students')
def getAllStudents():
    return jsonify(studentDAO.getAll())

# get a specific student by ID to display in the student details section
@app.route('/students/<int:id>')
def getStudent(id):
    return jsonify(studentDAO.findByID(id))

# create a new student when the form is submitted
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

# update an existing student when the form is submitted
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

# delete a student when the delete button is clicked
@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    studentDAO.delete(id)
    return jsonify({"done": True})


# update an existing student when the form is submitted
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = request.json
    updated_student = studentDAO.update(id, student)
    return jsonify(updated_student)


# run the Flask app
if __name__ == '__main__':
    app.run(debug=True)




