from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)