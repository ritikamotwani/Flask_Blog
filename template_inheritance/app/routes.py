from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
	user = {'username':	'Ritika'}
	posts = [
		{
			'author':{'username':'John'},
			'body':'Beutiful day'
		},
		{
			'author':{'username':'Susan'},
			'body':'Avengers movie was cool!'
		}
	]
	return render_template('index.html', title='Home', user = user, posts = posts)
