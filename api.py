from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

with open('quotes.json', 'r') as f:
    quotes_data = json.load(f)

quotes = quotes_data['quotes']

@app.route('/api/quote', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(debug=True)
