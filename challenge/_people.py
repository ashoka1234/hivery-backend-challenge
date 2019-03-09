import logging

from flask import Blueprint, Response, abort
import json

import challenge._model as model

_LOG = logging.getLogger(__name__)
bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route('/fruits_and_vegetables/<person>')
def fruits_and_vegetables(person: str = None):
    """
    Return name, age, fruits liked, and vegetables liked
    """

    result = model.QUERY_DB.get_person(person, {"_id": 0, "name": 1, "age": 1, "fruits": 1, "vegetables":1})

    if not result:
        abort(404, '{} not found'.format(person))

    result['username'] = result.pop('name')

    return Response(
        json.dumps(result),
        content_type='application/json'
    )


@bp.route('/friends/<string:name1>/<string:name2>')
def friends(name1: str, name2: str):
    """
    Return common friends of two persons who are brown eyes and living
    """

    name1_found, name2_found, result = model.QUERY_DB.get_friendship(name1, name2)

    if not name1_found or not name2_found:
        abort(404, 'name1 found: {}, name2 found: {}'.format(name1_found, name2_found))

    return Response(
        json.dumps(result),
        content_type='application/json'
    )
