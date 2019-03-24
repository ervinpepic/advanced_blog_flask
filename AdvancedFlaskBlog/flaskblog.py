from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '765ed382c961290b2d0963a0ffe39643'

posts = [
	{
		'author': 'Ervin Pepic',
		'title': 'Blog Post 1.',
		'content': 'Prvi post sadrzaj',
		'date_posted': 'April 1, 2019'
	},
	{
		'author': 'Emel Pepic',
		'title': 'Blog Post 2.',
		'content': 'Drugi post sadrzaj',
		'date_posted': 'April 3, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('Logged in!', 'success')
			return redirect(url_for('home'))
	else:
		flash('Login unsuccesseful. Pleas check your credentials.', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)