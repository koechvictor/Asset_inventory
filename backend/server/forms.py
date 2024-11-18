from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError
from server.models import Users
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(min=4)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=6)])
    confirmPassword = PasswordField('Confirm password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')

    def validate_email(self, field):
        user = Users.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already taken, please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('SignIn')

class MessageForm(FlaskForm):
    #recipient = SelectField('Recipient', coerce=int, validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Send')

    #def __init__(self, *args, **kwargs):
     #   super(MessageForm, self).__init__(*args, **kwargs)
      #  self.recipient.choices = [(user.id, user.username) for user in Users.query.all() if user.id != current_user.id]

class PostForm(FlaskForm):
    post = StringField('post', validators=[DataRequired()])
    submit = SubmitField('Add post')