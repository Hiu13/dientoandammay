
from flask import Flask, request, jsonify

app = Flask(__name__)
students = []

@app.route('/add', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({'message': 'Student added successfully'}), 201

@app.route("/students")
def get_students():
    return jsonify([
        {"id": 1, "name": "Alice", "hours": 20},
        {"id": 2, "name": "Bob", "hours": 22}
    ])
@app.route('/')
def home():
    return 'Student Service đang chạy OK!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
