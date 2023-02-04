import json

from flask import Flask, request, jsonify

from Backend import definitions

app = Flask(__name__)


# CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


# MainRoute
# use for testing values
@app.route("/", methods=['GET'])
def index():
    return "HEllO WORLD"


@app.route("/hand-results", methods=['POST'])
def api():
    cards = request.get_json()
    print(cards)
    return jsonify(cards)


if __name__ == '__main__':
    app.run()
