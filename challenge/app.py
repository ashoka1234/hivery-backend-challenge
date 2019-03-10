from flask import make_response, jsonify, abort
from . import _people, _companies, _model

APP = _model.APP
APP.register_blueprint(_people.bp)
APP.register_blueprint(_companies.bp)


@APP.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 404)


@APP.errorhandler(501)
def not_implemented(error):
    return make_response(jsonify({'error': error.description}), 501)


@APP.route('/')
def gateway():
    abort(501, {'endpoints': ['/people/fruits_and_vegetables/<string:person>',
                              '/people/friends/<string:name1>/<string:name2>',
                              '/companies/<string:name>']})
