import logging

from flask import Blueprint, abort, jsonify

import challenge._model as model

_LOG = logging.getLogger(__name__)
bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route('/')
def people_gateway():
    abort(501, {'endpoints': ['/people/fruits_and_vegetables/<string:person>',
                              '/people/friends/<string:name1>/<string:name2>']})


@bp.route('/fruits_and_vegetables')
@bp.route('/fruits_and_vegetables/<person>')
def fruits_and_vegetables(person: str = None):
    """
    Return name, age, fruits liked, and vegetables liked
    """
    if not person:
        abort(501, {'endpoints': ['/people/fruits_and_vegetables/<string:person>']})

    result = model.QUERY_DB.get_person(person, {"_id": 0, "name": 1, "age": 1, "fruits": 1, "vegetables":1})

    if not result:
        abort(404, {person: 'not found'})

    result['username'] = result.pop('name')

    return jsonify(result)


@bp.route('/friends')
@bp.route('/friends/<string:name1>')
@bp.route('/friends/<string:name1>/<string:name2>')
def friends(name1: str = None, name2: str = None):
    """
    Return common friends of two persons who are brown eyes and living
    """
    if not name1 or not name2:
        abort(501, {'endpoints': ['/people/friends/<string:name1>/<string:name2>']})

    name1_found, name2_found, result = model.QUERY_DB.get_friendship(name1, name2)

    if not name1_found or not name2_found:
        abort(404, {name1: 'found' if name1_found else 'not found',
                    name2: 'found' if name2_found else 'not found'})

    return jsonify(result)
