from __future__ import absolute_import

import logging

from flask import Blueprint

_LOG = logging.getLogger(__name__)
bp = Blueprint('companies', __name__, url_prefix='/companies')


@bp.route('company/<string:name>')
def company(name):
    pass

