from flask import Flask, request, jsonify
from studentDAO import studentDAO

app = Flask(__name__)

@app.route('/students')
def getAll():
    return jsonify(studentDAO.getAll())

@app.route('/students/<int:id>')
def findById(id):
    return jsonify(studentDAO.findById(id))

@app.route('/students', methods=['POST'])
def create():
    student = request.json
    new_id = studentDAO.create(student)
    return jsonify({"id": new_id})

@app.route('/students/<int:id>', methods=['PUT'])
def update(id):
    student = request.json
    result = studentDAO.update(id, student)
    return jsonify({"updated": result})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete(id):
    result = studentDAO.delete(id)
    return jsonify({"deleted": result})

if __name__ == "__main__":
    app.run(debug=True)
