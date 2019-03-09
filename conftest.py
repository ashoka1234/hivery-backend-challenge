import pytest
from pathlib import Path
import json

from challenge.db import connect, LocalConfig, WriteAPI


@pytest.fixture(scope='function')
def empty_db():

    config = LocalConfig()
    config.set_database_name('aj_empty')
    db = connect(cfg=config.cfg)
    write_db = WriteAPI(db)
    write_db.init_db()

    yield db

    db.client.drop_database('aj_empty')


@pytest.fixture(scope='module')
def initialized_db():

    config = LocalConfig()
    config.set_database_name('aj_initialized')
    db = connect(cfg=config.cfg)
    write_db = WriteAPI(db)
    write_db.init_db()

    if (Path(__file__).parent / 'resources/fruits.json').exists():
        with open( Path(__file__).parent / 'resources/fruits.json') as fd:
            fruits = set(json.load(fd))
    else:
        fruits = {"orange", "apple", "banana", "strawberry"}

    with open(Path(__file__).parent / 'resources/people.json', 'r') as fd:
        people = json.load(fd)
    write_db.add_people(people, fruits)

    with open(Path(__file__).parent / 'resources/companies.json', 'r') as fd:
        companies = json.load(fd)
    write_db.add_companies(companies)

    yield db

    db.client.drop_database('aj_initialized')
