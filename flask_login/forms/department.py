from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DepartmentsForm(FlaskForm):
    title = StringField('Department title', validators=[DataRequired()])
    chief = StringField("Chief", validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = StringField('Department email', validators=[DataRequired()])
    submit = SubmitField('Применить')