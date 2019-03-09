from pathlib import Path
import flask
from flask_caching import Cache
from challenge.db import connect, QueryAPI

NAME = 'challenge'
BASE_DIR = Path(__file__).parent.parent

APP = flask.Flask(NAME)

# Optional environment settings file or variable
APP.config.from_pyfile(BASE_DIR / 'settings.env.py', silent=True)

APP.config.setdefault('CACHE_TYPE', 'simple')
cache = Cache(
    app=APP,
    config=APP.config,
)

QUERY_DB = QueryAPI(connect())
