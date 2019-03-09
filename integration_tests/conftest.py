import pytest
from flask.testing import FlaskClient

import challenge
from challenge import _model
from challenge.db import QueryAPI


@pytest.fixture(scope='module')
def empty_client(initialized_db) -> FlaskClient:
    """
    Return Flask client with access to initialized mongodb with data in the
    resources directory
    """

    _model.QUERY_DB = QueryAPI(initialized_db)
    _model.cache.clear()
    challenge.APP.config['TESTING'] = True

    return challenge.APP.test_client()

