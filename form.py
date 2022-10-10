from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class myForm(FlaskForm):
    country_name = StringField('country', validators=[DataRequired()])
    submit = SubmitField('Get Info')
