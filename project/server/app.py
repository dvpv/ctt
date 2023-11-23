from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the MariaDB database URI from the environment variable
database_uri = os.environ.get(
    "TODO_APP_DATABASE_URI", "mysql+pymysql://username:password@localhost/dbname"
)
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)


# Create tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created")


# Routes
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "task": task.task} for task in tasks]
    return jsonify(task_list)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = Task(task=data["task"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"}), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})
    else:
        return jsonify({"message": "Task not found"}), 404


if __name__ == "__main__":
    # Run the server
    app.run(host="0.0.0.0", port=1337, debug=True)
