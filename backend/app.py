from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
    # TODO: replace with your implementation. This is a mock response

    # return jsonify([
    #     {'course': 'COMP1531', 'id': 1, 'mark': 85, 'name': 'Alice Zhang'},
    #     {'course': 'COMP1531', 'id': 2, 'mark': 72, 'name': 'Bob Smith'}
    # ]), 200
    students = db.get_all_students()
    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    student_data = request.json

    if not student_data:
        return jsonify({"error": "request body is required"}), 404
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark", 0)
    if not name or not course:
        return jsonify({"error": "name and course are required"}), 404
    student = db.insert_student(name, course, mark)
    return jsonify(student), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """

    student_data = request.json
    if not student_data:
        return jsonify({"error": "request body is required"}), 404
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")
    student = db.update_student(student_id, name, course, mark)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student), 200
    # pass  # replace with your implementation



@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """

    # pass  # replace with your implementation
    student = db.delete_student(student_id)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student), 200



@app.route("/stats")
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """

    # pass  # replace with your implementation
    students = db.get_all_students()
    marks = [student["mark"] for student in students]
    count = len(marks)
    if count == 0:
        return jsonify({"count": 0, "average": 0, "min": None, "max": None}), 200

    return jsonify({"count": count, "average": sum(marks) / count, "min": min(marks), "max": max(marks)}), 200



@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
