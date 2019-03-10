from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
arr = []  
@app.route("/", methods=["GET", "POST", "DELETE"])
def hello():
    global arr

    if request.method == "GET": 
        print(arr)
        return jsonify(arr)
    if request.method == "POST":
        body = request.get_json()
        print(body)
        arr.append(body['title'])
        print(arr)	
        return jsonify(body)
    if request.method == "DELETE":
        if len(arr) > 0:
            arr.pop()   
        print(arr)
        return jsonify(arr)

app.run()