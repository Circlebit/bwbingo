from flask import render_template, request
from app import app
from .forms import BuzzwordForm

bwList = []

@app.route('/', methods=['GET', 'POST'])
def newBingo():
	form = BuzzwordForm()
	if request.method == 'POST': # and form.validate(): # add validation!
		if form.bwInput.data not in bwList and form.bwInput.data != '': # dont accept duplicates or empty string
			bwList.append(form.bwInput.data)
		print(bwList) # for debugging
	return render_template('index.html',
							form = form,
							bwList = bwList)