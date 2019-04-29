from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/users/<username>")
def user(username):
    result = {
        "username": username,
        "last_modified": "2018-11-15T11:16:01",
        "id": 123,
        "groups": [
            "Editors",
        ],
    }
    return jsonify(result)


@app.route("/provider_states", methods=["POST"])
def provider_states():
    print(request.json)
    return ""
