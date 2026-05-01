from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__, static_url_path='', static_folder='static')

def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------
# GET ALL STUDENTS
# -----------------------
@app.route("/students", methods=["GET"])
def get_students():
    db = get_db()
    rows = db.execute("SELECT * FROM students").fetchall()
    return jsonify([dict(row) for row in rows])

# -----------------------
# CREATE STUDENT
# -----------------------
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO students (name, address, email, course) VALUES (?, ?, ?, ?)",
        (data["name"], data["address"], data["email"], data["course"])
    )
    db.commit()
    return jsonify({"status": "created"})

# -----------------------
# UPDATE STUDENT
# -----------------------
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    db = get_db()
    db.execute(
        "UPDATE students SET name=?, address=?, email=?, course=? WHERE id=?",
        (data["name"], data["address"], data["email"], data["course"], id)
    )
    db.commit()
    return jsonify({"status": "updated"})

# -----------------------
# DELETE STUDENT
# -----------------------
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    return jsonify({"status": "deleted"})

# -----------------------
# SERVE FRONTEND
# -----------------------
@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run()
