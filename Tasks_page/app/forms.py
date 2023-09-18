from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField
from wtforms.fields.simple import BooleanField, EmailField, TextAreaField

from .models import User

def codi_validator(form, field):
    if field.data == "Steven" or field.data == "Steven":
        raise validators.ValidationError("The username Steven is not permitted.")


class LoginForm(Form):
    
    username = StringField("Username", [
        validators.DataRequired(), 
        validators.Length(min=4, max=50, message=('The username is out of range'))
    ])

    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.length(min=6, max=50, message=('Password is required.'))
    ])

class RegisterForm(Form):
    username = StringField("Username", [
        validators.length(min=4, max=50),
        codi_validator
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.DataRequired(message="Email is required"),
        validators.Email(message="Enter a valid email address")
    ])

    password = PasswordField('Password', [
        validators.DataRequired("The password is required."),
        validators.EqualTo("confirm_password", message="The password does not match.")
    ])
    confirm_password = PasswordField("Confirm password")
    accept = BooleanField("", [
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError("The username is already in use")


    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError("Email is already in use")


    def validate(self):
        if not Form.validate(self):
            return False
        
        if len(self.password.data) < 6:
            self.password.errors.append("Password must contain more than 6 characters")
            return False

        return True
    
class TaskForm(Form):
    title = StringField("Título",[
        validators.length(min=4, max=50, message="Title out of range."),
        validators.DataRequired(message="The title is required.")
    ])
    description = TextAreaField("Description", [
        validators.DataRequired(message="Description is required")
    ], render_kw={"rows": 8})


