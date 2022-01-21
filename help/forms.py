from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HelpForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    domain_name = StringField()
    submit = SubmitField('Wyślij')