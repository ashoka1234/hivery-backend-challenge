from . import _people, _companies, _model

APP = _model.APP
APP.register_blueprint(_people.bp)
APP.register_blueprint(_companies.bp)
