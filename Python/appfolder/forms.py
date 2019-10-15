from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    
    weekNumber = StringField('weekNumber', validators=[DataRequired()])
    submit = SubmitField("Submit")


    