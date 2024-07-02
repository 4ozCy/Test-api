from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

with open('pickup-lines.json', 'r') as f:
    picku-plines_data = json.load(f)

pickup-lines = pickup-lines_data['pickup-lines']

@app.route('/api/random/pickup?lines', methods=['GET'])
def get_pickup():
    random_pickup-lines = random.choice(pickup-lines)
    return jsonify({'pickup-lines': random_pickup-lines})

if __name__ == '__main__':
    app.run(debug=True)
