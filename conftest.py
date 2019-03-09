import pytest
from pathlib import Path
import json
import logging

from challenge.db import connect, LocalConfig, WriteAPI

_LOG = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='function')
def empty_db():
    """
    Return an empty mongodb
    """

    config = LocalConfig(database_name='ashoka_testing')
    db = connect(cfg=config.cfg)
    write_db = WriteAPI(db)
    write_db.init_db()

    yield db

    db.client.drop_database('ashoka_testing')


@pytest.fixture(scope='module')
def initialized_db():
    """
    Return an initialized mongodb with data in the resources directory
    """

    config = LocalConfig(database_name='ashoka_testing')
    db = connect(cfg=config.cfg)
    write_db = WriteAPI(db)
    write_db.init_db()

    if (Path(__file__).parent / 'resources/fruits.json').exists():
        with open(Path(__file__).parent / 'resources/fruits.json') as fd:
            fruits = set(json.load(fd))

        _LOG.info('Added fruits: %s', len(fruits))
    else:
        fruits = {"orange", "apple", "banana", "strawberry"}

    with open(Path(__file__).parent / 'resources/people.json', 'r') as fd:
        people = json.load(fd)
    write_db.add_people(people, fruits)
    _LOG.info('Added people to database aj_initialized: %s', len(people))

    with open(Path(__file__).parent / 'resources/companies.json', 'r') as fd:
        companies = json.load(fd)
    write_db.add_companies(companies)
    _LOG.info('Added companies to database aj_initialized: %s', len(companies))

    yield db

    db.client.drop_database('ashoka_testing')
