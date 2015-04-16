from flask import render_template, request
from app import app
from .forms import BuzzwordForm, DelButtonForm

bwList = []
delButtonList = []

@app.route('/', methods=['GET', 'POST'])
def newBingo():
	form = BuzzwordForm()
	delform = DelButtonForm()
	
	if request.method == 'POST': # and form.validate(): # add validation!
		if form.bwInput.data not in bwList and form.bwInput.data != '': # dont accept duplicates or empty string
			bwList.append(form.bwInput.data)
			delButtonList.append(delform)

		delform_answer = DelButtonForm(request.form) #??

		if bwList and delButtonList and delform_answer.delId.data:
			del bwList[int(delform_answer.delId.data)]

	return render_template('index.html',
							form = form,
							bwList = bwList,
							delButtonList = delButtonList)