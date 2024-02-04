import json
from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load the actions from the JSON file
    with open('actions.json', 'r') as file:
        data = json.load(file)
        actions = data["actions"]

    # Endpoint for querying by codeword
    @app.route('/action/by_codeword/<int:codeword>', methods=['GET'])
    def get_action_by_codeword(codeword):
        for action in actions:
            if action["codeword"] == codeword:
                return jsonify({"id": action["id"]})
        return jsonify({"error": "Action not "}), 404

    @app.route('/action/by_id/<action_id>', methods=['GET'])
    def get_codewords_by_id(action_id):
        codewords = [action["codeword"] for action in actions if action["id"] == action_id]
        if not codewords:
            return jsonify({"error": "Codewords not found"}), 404
        elif len(codewords) == 1:
            return jsonify({"codeword": codewords[0]})
        else:
            return jsonify({"codewords": codewords})
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=3000)
