from flask.testing import FlaskClient


def test_companies(empty_client: FlaskClient, initialized_db):

    # Test a company having employees
    rv = empty_client.get('/companies/PERMADYNE')
    assert rv.status_code == 200
    data = rv.json
    assert data['company'] == 'PERMADYNE'
    assert len(data['employees']) == 7

    # Test a company not having employees
    rv = empty_client.get('/companies/NETBOOK')
    assert rv.status_code == 200
    data = rv.json
    assert data['company'] == 'NETBOOK'
    assert len(data['employees']) == 0

    # Test a company not in the database
    rv = empty_client.get('/companies/BHP')
    assert rv.status_code == 404


