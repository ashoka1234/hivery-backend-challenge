from flask.testing import FlaskClient


def test_fruits_and_vegetables(empty_client: FlaskClient, initialized_db):

    rv = empty_client.get('/people/fruits_and_vegetables/Decker Mckenzie')
    assert rv.status_code == 200
    data = rv.json
    assert data['age'] == 60
    assert data['username'] == 'Decker Mckenzie'
    assert bool(data['fruits']) is False
    assert len(data['vegetables']) == 4

    # Test a person not in the database
    rv = empty_client.get('/people/fruits_and_vegetables/Steve Smith')
    assert rv.status_code == 404


def test_friends(empty_client: FlaskClient, initialized_db):

    # Test two persons with common friends who are living and has brown eyes
    rv = empty_client.get('/people/friends/Bonnie Bass/Mindy Beasley')
    assert rv.status_code == 200
    data = rv.json
    assert data['people'][0]['name'] == 'Bonnie Bass'
    assert data['people'][1]['name'] == 'Mindy Beasley'
    assert data['friends'][0] == 1
    assert len(data['friends']) == 1

    # Test two persons without common friends who are living and has brown eyes
    rv = empty_client.get('/people/friends/Carmella Lambert/Gabrielle Horton')
    assert rv.status_code == 200
    data = rv.json
    assert len(data['friends']) == 0

    # Test persons with one of them not in the database
    rv = empty_client.get('/people/friends/Carmella Lambert/Steve Smith')
    assert rv.status_code == 404
