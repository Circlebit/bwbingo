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

	bwList_free = bwList[:]
	bwList_free.insert(12, "FREE")

	tablelink = request.base_url + "table?shuffle=true&bw=" + "|".join(bwList_free)

	return render_template('index.html',
							form = form,
							bwList = bwList,
							delButtonList = delButtonList,
							tablelink = tablelink)


@app.route('/table', methods=['GET'])
def table():

	bwUrl = request.args.get('bw')
	if bwUrl:
		bwList = bwUrl.split("|")

	### DEBUG CASES
	# bwList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
	# table?bw=jahvistic|jamnagar|jerseyed|loneness|nonidiomatical|nonplutocratic|beak|changefully|though|unfainting|polytheist|decolorizing|disillusionist|dialogite|scapegoatism|romanticise|scorpion|shopwalker|substitutively|snotty|speediness|stephanotis|stereotyping|sunwise|infancy|hoover|hypnagogic

	bwList_shuff = bwList[:]
	if request.args.get('shuffle'):
		del bwList_shuff[12]
		shuffle(bwList_shuff)
		bwList_shuff.insert(12, "FREE")


	#bwList_shuff.insert(12, "FREE")

	permalink = request.base_url + "?bw=" + "|".join(bwList_shuff)
	reshuffle = request.base_url + "?shuffle=true&bw=" + "|".join(bwList_shuff)

	return render_template('table.html',
							bwList_shuff=bwList_shuff,
							permalink = permalink,
							reshuffle = reshuffle)
