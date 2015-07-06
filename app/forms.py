__author__ = 'trevor'
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class TextForm(Form):
    full_text = TextAreaField(label='full_text',
                              description='Enter text here to translate.',
                              validators=[DataRequired()])