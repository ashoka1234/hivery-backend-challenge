from . import _people, _companies, _model

app = _model.app
app.register_blueprint(_people.bp)
app.register_blueprint(_companies.bp)

# Define the root endpoint