""" 
We create classes similar to the models.py, then we create some fields
inside the classes, where those fields are the required fields for the users
that they have to fill in to register to the website.

"""

from flask_wtf import FlaskForm
"""
We need to import special fields that are recognized by special type of fields
Example: Integer field or String field.

To do this:
"""
from wtforms import StringField, PasswordField, SubmitField

# Inherits from the flaskform class
class RegisterForm(FlaskForm):
    username = StringField(label='username')  # A convention to give a label for each field
    email_address = StringField(label='email')
    # Two passwords for confirmation of the password. Later create validation for the password.
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')    
    submit = SubmitField(label='submit')  # Button to submit the final information.