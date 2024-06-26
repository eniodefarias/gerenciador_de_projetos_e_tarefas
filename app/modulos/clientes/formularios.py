from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')
