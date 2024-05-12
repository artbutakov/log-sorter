from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = HiddenField()
