from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class BuzzwordForm(Form):
	bwInput = StringField('buzzword', validators=[DataRequired()])