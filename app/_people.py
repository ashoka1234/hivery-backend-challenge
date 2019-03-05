from __future__ import absolute_import

import logging

from flask import Blueprint

_LOG = logging.getLogger(__name__)
bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route('fruit_and_vegetables/<string:name>')
def fruit_and_vegetables(name):
    pass


@bp.route('friends/<string:name1>/<string:name2>')
def friends(name1, name2):
    pass
