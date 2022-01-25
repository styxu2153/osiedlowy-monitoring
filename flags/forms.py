from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from models import Flaga

class AddressForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    domain_name = StringField(validators=[DataRequired()])
    submit = SubmitField('Wyślij')
    
    def validate_domain_name(self, domain_name):
        domain_name = Flaga.query.filter_by(domain_name='http://'+domain_name.data).first()
        if domain_name is not None:
            raise ValidationError('Domena z tą nazwą już istnieje w bazie danych!')