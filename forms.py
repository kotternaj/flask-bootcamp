from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):

    id = IntegerField('ID # of Puppy to Remove:')
    submit = SubmitField('Remove Puppy') 

class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner:')
    pup_id = StringField('ID of puppy:')
    submit = SubmitField('Add Owner')