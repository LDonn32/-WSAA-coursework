from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)  # allow cross-origin requests 

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "students.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/students", methods=["GET"])
def get_students():
    db = get_db()
    rows = db.execute("SELECT * FROM students").fetchall()
    return jsonify([dict(row) for row in rows])

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json or {}
    db = get_db()
    db.execute(
        "INSERT INTO students (name, address, email, course) VALUES (?, ?, ?, ?)",
        (data.get("name"), data.get("address"), data.get("email"), data.get("course"))
    )
    db.commit()
    return jsonify({"status": "created"}), 201

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json or {}
    db = get_db()
    db.execute(
        "UPDATE students SET name=?, address=?, email=?, course=? WHERE id=?",
        (data.get("name"), data.get("address"), data.get("email"), data.get("course"), id)
    )
    db.commit()
    return jsonify({"status": "updated"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    return jsonify({"status": "deleted"})

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    # For local testing only. On PythonAnywhere the WSGI server will run the app.
    app.run(debug=True)





























