from flask import Flask, jsonify, request, render_template
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
def index():
    return render_template('index.html', questions=cards)


@app.route('/api/cards', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return jsonify(cards)
    elif request.method == 'POST':
        new_card = request.json
        new_card['id'] = cards[-1]['id'] + 1
        cards.append(new_card)
        return f"{new_card}", 201


@app.route('/api/cards/<int:card_id>', methods=["GET", "DELETE", "PUT"])
def card_handler(card_id):
    if request.method == "GET":
        try:
            return next(card for card in cards if card['id'] == card_id)
        except:
            raise NotFound(f"No cards with an ID of {card_id}!")

    elif request.method == "DELETE":
        try:
            for card in cards:
                if card["id"] == card_id:
                    cards.remove(card)
            return f"Card removed", 200
        except:
            raise NotFound(
                f"No cards with ID {card_id} found. Could not delete")

    elif request.method == "PUT":
        try:
            for card in cards:
                print(f"id is: {card_id}")
                map(lambda x: x if x["id"] != card_id else req.json(), cards)
            return f"Card Updated"
        except:
            raise NotFound(
                f"No cards with ID {card_id} found. Could not update.")


# Error handlers
@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops... {err}"}), 404


if __name__ == "__main__":
    app.run(debug=True)
