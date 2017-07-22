from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, HiddenField #BooleanField
from wtforms.validators import DataRequired

class BuzzwordForm(Form):
	bwInput = StringField('buzzword', validators=[DataRequired()])

class DelButtonForm(Form):
	delId = HiddenField()
	delButton = SubmitField(' - ')

# impelement titleform here
#class TitleForm(Form):
#	Title = StringField('Title')
