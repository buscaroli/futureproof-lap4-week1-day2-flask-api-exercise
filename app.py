from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

cards = [
    {'id': 1,
     'question': 'What is the third planet in the Solar System?',
     'answer': 'Earth'
     },
    {
        'id': 2,
        'question': 'question 2',
        'answer': 'answer 2'
    },
    {
        'id': 3,
        'question': 'question 3',
        'answer': 'answer 3'
    }
]


@app.route('/')
def home():
    return jsonify({'message': 'Hello to Cards!'}), 200


@app.route('/api/cards', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(cards)
    elif request.method == 'POST':
        new_card = request.json
        new_card['id'] = cards[-1]['id'] + 1
        cards.append(new_card)
        return f"{new_card}", 201


if __name__ == "__main__":
    app.run(debug=True)
