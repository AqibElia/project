from flask import Flask, jsonify, request
app = Flask(__name__)
students = [
    {"id": 1, "name":"Aqib", "age": 20, "grade": "A"},
    {"id": 2, "name":"Mudasir", "age":20, "grade": "B"}
]
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)
@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify (student)
@app.route('/api/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    new_student={
        "id": len(students) + 1,
        "name": new_student.get('name'),
        "age": new_student.get('age'),
        "grade": new_student.get('grade')
    }
    return jsonify(new_student), 201
@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    student= next((s for s in students if s['id'] == id), None)
    if student:
        student_data = request.get_json()
        student ['name'] = student_data.get('name', student['name'])
        student ['age'] = student_data.get('age', student['age'])
        student ['grade'] = student_data.get('grade', student['grade'])
        return jsonify(student)
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
