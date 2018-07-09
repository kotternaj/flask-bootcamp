from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Owner:')
    pup_id = StringField('ID of puppy:')
    submit = SubmitField('Add Owner')