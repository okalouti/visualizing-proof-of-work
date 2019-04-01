import pytest
import json
from app import app, Blockchain

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

@pytest.fixture
def new_blockchain():
    blockchain = Blockchain()
    return blockchain

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def test_new_blockchain(new_blockchain):
    print(new_blockchain.chain)
    assert new_blockchain.chain[0]['proof'] == 100
    assert new_blockchain.chain[0]['previous_hash'] == 1


def test_response(client):
    response = client.get('/chain')
    formatted = json_of_response(response)
    assert formatted['length'] == 1