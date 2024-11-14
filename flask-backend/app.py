from flask import Flask, request, jsonify
import mysql.connector

from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kotesh@1234",
    database="todo_db"
)

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    task = data.get('task')
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    db.commit()
    return jsonify({"message": "Task added successfully!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
