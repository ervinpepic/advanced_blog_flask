from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
	username 			= StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
	email 				= StringField('Email', validators=[DataRequired(), Email()])
	password 			= PasswordField('Password', validators=[DataRequired()])
	confirm_password 	= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit 				= SubmitField('Sign Up')

	def validate_username(self, username):
		user 	= User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('User with that username already exists. Chose another...')

	def validate_email(self, email):
		user 	= User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email is already used...')

class LoginForm(FlaskForm):
	email 				= StringField('Email', validators=[DataRequired(), Email()])
	password 			= PasswordField('Password', validators=[DataRequired()])
	remember			= BooleanField('Remeber me')
	submit 				= SubmitField('Login')


