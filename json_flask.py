from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

with open('request.json') as f:
    data = json.load(f)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = [0, 1, 2, 3, 4, 5]
    return jsonify({"key": result})

@app.route("/json", methods=['POST'])
def json():
    # req = request.get_json()
    # Recieved the following on the flask server
    # 127.0.0.1 - - [31/Mar/2020 21:17:23] "GET /json HTTP/1.1" 405 -
    # {'name': 'ruchir', 'message': 'testing JSON to Flask!'}
    # print(req)
    # return "Thanks!", 200

    if request.is_json:
        req = request.get_json()
        return "JSON Recieved", 200
    else:
        return "No JSON recieved", 400
