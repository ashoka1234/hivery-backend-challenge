from pathlib import Path
import flask
from flask_caching import Cache
from pymongo import MongoClient

NAME = 'challenge'
BASE_DIR = Path(__file__).parent.parent

app = flask.Flask(NAME)

# Optional environment settings file or variable
app.config.from_pyfile(BASE_DIR / 'settings.env.py', silent=True)
app.config.from_envvar('HIVERY_SETTINGS', silent=True)

app.config.setdefault('CACHE_TYPE', 'simple')
cache = Cache(
    app=app,
    config=app.config,
)

mongo_client = MongoClient()
db = mongo_client['hivery_backend_challenge']
