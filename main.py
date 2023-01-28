from Backend import definitions
from flask import Flask, request, jsonify

app = Flask(__name__)


# MainRoute
# use for testing values
@app.route("/", methods=['GET'])
def index():
    return "HEllO WORLD"


# Route to get results
# input-param list of cards
# return result card list
@app.route("/result", methods=["GET"])
def get_cards():
    input_data = request.json
    card_list = input_data[definitions.DATA_CARDLIST]
    # ToDo use CardList to calculate result and return
    result = {
        "result": "myResult"
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
