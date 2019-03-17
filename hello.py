from flask import Flask, request, jsonify 
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)
todos = {}

@app.route("/", methods=["GET", "POST", "DELETE"])
def root_resource():
    response = None
    if request.method == "GET": 
        response = jsonify(list(todos.values()))
    if request.method == "POST":
        body = request.get_json()
        body['completed'] = False

        id = str(uuid.uuid4())
        body['url'] = request.url + id
        todos[id] = body

        response = jsonify(body)
    if request.method == "DELETE":
        todos.clear()
        response = jsonify(list(todos.values()))
    print(todos)
    return response

@app.route('/<id>', methods=["GET"])
def id_resource(id):
    return jsonify(todos[id])

app.run()