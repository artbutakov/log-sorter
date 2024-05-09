from wtforms.fields.simple import StringField, SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired


class SearchForm(Form):
    searchbar = StringField(validators=[DataRequired()])
    button = SubmitField('Search')
