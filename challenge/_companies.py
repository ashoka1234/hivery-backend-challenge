import logging

from flask import Blueprint, Response, abort
import json

import challenge._model as model

_LOG = logging.getLogger(__name__)
bp = Blueprint('companies', __name__, url_prefix='/companies')


@bp.route('/<string:name>')
def company(name):
    """
    Return employees of the company
    """
    result = model.QUERY_DB.get_company(name)
    if not result:
        _LOG.info('%s not found', name)
        abort(404, '{} not found'.format(name))
    return Response(
        json.dumps(result),
        content_type='application/json'
    )

