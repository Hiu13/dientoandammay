
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/stats', methods=['GET'])
def get_stats():
    try:
        response = requests.get('http://student_service:5000/students')
        data = response.json()
        result = {}
        for student in data:
            name = student.get("name")
            hours = student.get("hours", 0)
            result[name] = result.get(name, 0) + hours
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/')
def home():
    return 'Student Service đang chạy OK!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
