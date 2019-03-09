import pytest
from flask.testing import FlaskClient

import challenge
from challenge import _model


@pytest.fixture(scope='function')
def empty_client() -> FlaskClient:

    _model.cache.clear()
    challenge.APP.config['TESTING'] = True

    return challenge.APP.test_client()
