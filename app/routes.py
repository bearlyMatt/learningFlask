from flask import render_template, flash, redirect
from app import app
## from the forms.py file (app/forms.py)  import the LoginForm class
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username':'bearlyMatt'}
	posts = [
	{
		'author': {'username': 'John'},
		'body': 'Beautiful day in portland!'
	},
	{
		'author': {'username': 'Susan'},
		'body': 'The Avengers movie was so cool!'
	}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

##url root for applet
## methods are GET i.e. retrieve info FROM server and POST i.e. send info TO server
@app.route('/login', methods=['GET', 'POST'])
## instantiate the login page
def login():
	## create object 'form'
	form = LoginForm()
	## GET request will return false (nothing to validate) but POST request will be true (user/pass needs validation)
	if form.validate_on_submit():
			##alert user of background process
			flash('Login Requested for User {}, remember_me={}'.format(
				form.username.data, form.remember_me.data
			))
			## send correct login to index page
			return redirect(url_for('/index'))
	##render object 'form' with the html template 'form'
	return render_template('login.html', title='Sign In', form=form)
