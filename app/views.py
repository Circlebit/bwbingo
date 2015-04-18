from flask import render_template, request
from app import app
from .forms import BuzzwordForm, DelButtonForm
from random import shuffle

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


@app.route('/table', methods=['GET'])
def table():

	### DEBUG CASE
	#bwList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
	###
	bwList_shuff = bwList[:]
	shuffle(bwList_shuff)

	bwList_shuff.insert(12, "FREE")
	print(bwList_shuff)

	return render_template('table.html',
							bwList_shuff=bwList_shuff)