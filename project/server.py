from flask import Flask, jsonify, request, abort, send_from_directory
from studentDAO import (
    get_all_students,
    get_student_by_id,
    create_student,
    update_student,
    delete_student
)

app = Flask(__name__, static_folder='static')

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# RESTful API endpoints

@app.route('/api/students', methods=['GET'])
def api_get_all_students():
    return jsonify(get_all_students())

@app.route('/api/students/<int:student_id>', methods=['GET'])
def api_get_student(student_id):
    student = get_student_by_id(student_id)
    if student is None:
        abort(404, description="Student not found")
    return jsonify(student)

@app.route('/api/students', methods=['POST'])
def api_create_student():
    if not request.json:
        abort(400, description="Request must be JSON")

    required_fields = ['name', 'address', 'email', 'course']
    for field in required_fields:
        if field not in request.json:
            abort(400, description=f"Missing required field: {field}")

    student = {
        'name': request.json['name'],
        'address': request.json['address'],
        'email': request.json['email'],
        'course': request.json['course']
    }

    try:
        new_id = create_student(student)
        student['id'] = new_id
        return jsonify(student), 201
    except Exception as e:
        abort(400, description=str(e))

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def api_update_student(student_id):
    if not request.json:
        abort(400, description="Request must be JSON")

    existing = get_student_by_id(student_id)
    if existing is None:
        abort(404, description="Student not found")

    student = {
        'name': request.json.get('name', existing['name']),
        'address': request.json.get('address', existing['address']),
        'email': request.json.get('email', existing['email']),
        'course': request.json.get('course', existing['course'])
    }

    update_student(student_id, student)
    student['id'] = student_id
    return jsonify(student)

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def api_delete_student(student_id):
    if not delete_student(student_id):
        abort(404, description="Student not found")
    return jsonify({'message': 'Student deleted', 'id': student_id})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': error.description}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400

if __name__ == '__main__':
    app.run(debug=True)
