import logging

from flask import Blueprint, abort, jsonify

import challenge._model as model

_LOG = logging.getLogger(__name__)
bp = Blueprint('companies', __name__, url_prefix='/companies')


@bp.route('/')
@bp.route('/<string:name>')
def company(name: str = None):
    """
    Return employees of the company
    """

    if not name:
        abort(501, {'endpoints': ['/companies/<string:name>']})

    result = model.QUERY_DB.get_company(name)
    if not result:
        _LOG.info('%s not found', name)
        abort(404, {name: 'not found'})

    return jsonify(result)
