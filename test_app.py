from app import app
import pytest


def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert 'message' in response.json


def test_index_get():
    response = app.test_client().get('/api/cards')
    print(response.json)
    assert response.status_code == 200
    assert {'answer': 'Earth', 'id': 1,
            'question': 'What is the third planet in the Solar System?'} in response.json

def test_card_handler():
    response = app.test_client().get('/api/cards/1')
    assert response.status_code == 200
    assert 'answer' in response.json

def test_card_handler_NotFound():
    response = app.test_client().get('/api/cards/234098238472')
    assert response.status_code == 404

def test_index_post():
    response = app.test_client().post(
        '/api/cards',
        headers={'Content-Type': 'application/json'},
        data={
            'question': 'test question',
            'answer': 'test answer'
        }
    )
    assert response.status_code == 400

def test_handle_404():
    response = app.test_client().get(
        '/sdjkfhalskdf')
    assert response.status_code == 404
