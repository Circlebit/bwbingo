from flask import render_template, request
from app import app
from .forms import BuzzwordForm

bwList = []


@app.route('/index')
def index():
	return render_template('index.html',
							title = 'TITEL',
							subject = 'fnord')

@app.route('/', methods=['GET', 'POST'])
def newBingo():
	form = BuzzwordForm() #request.form)
	if request.method == 'POST': # and form.validate():
		if form.bwInput.data not in bwList and form.bwInput.data != '':
			bwList.append(form.bwInput.data)
		print(bwList)
	return render_template('index.html',
							form = form,
							bwList = bwList)