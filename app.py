from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound

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


@app.route('/api/cards/<int:card_id>', methods=["GET", "DELETE"])
def card_handler(card_id):
    if request.method == "GET":
        try:
            return next(card for card in cards if card['id'] == card_id)
        except:
            raise NotFound(f"No cards with an ID of {card_id}!")
    if request.method == "DELETE":
        try:
            for card in cards:
                print(f"* * * {card}")
                if card["id"] == card_id:
                    cards.remove(card)
            return f"Card removed", 200
        except:
            raise NotFound(f"No cards with ID {card_id} to delete")


# Error handlers
@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops... {err}"}), 404


if __name__ == "__main__":
    app.run(debug=True)
