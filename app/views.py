from flask import render_template, request
from app import app
from .forms import BuzzwordForm, DelButtonForm

bwList = []
delButtonList = []
l = [2,3,4]

@app.route('/', methods=['GET', 'POST'])
def newBingo():
	form = BuzzwordForm()
	delform = DelButtonForm()
	
	#print(delform.delId.data)
	if request.method == 'POST': # and form.validate(): # add validation!
		if form.bwInput.data not in bwList and form.bwInput.data != '': # dont accept duplicates or empty string
			bwList.append(form.bwInput.data)
			delform.delId.data = len(bwList)-1
			delButtonList.append(delform)

		# some prints for debugging
		print("delButtonList: ")
		print(delButtonList)
		for button in delButtonList:
			print(button.delId.data)
		
	return render_template('index.html',
							form = form,
							bwList = bwList,
							delform = delform)