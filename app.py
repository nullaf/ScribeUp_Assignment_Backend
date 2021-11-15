from flask import Flask, make_response, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')


def fetch_trial_data():
    # Should use a database to fetch data
    file_object = open("data.json", "r")
    return json.loads(file_object.read())


@app.route("/<username>", methods=["GET"])
def fetch_user_trial_data(username):
    data = fetch_trial_data()
    if username in data["users"]:
        return make_response(jsonify(data["users"][username]), 200)

    return make_response(jsonify({"error": "User not found"}), 404)


if __name__ == "__main__":
    if app.config['FLASK_ENV'] == 'production':
        # Should use WSGI or Waitress instead for prod
        app.run(debug=app.config['DEBUG'])
    else:
        app.run(host='localhost', port='8000', debug=app.config['DEBUG'])
