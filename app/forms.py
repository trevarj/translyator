__author__ = 'trevor'
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length


class TextForm(Form):
    full_text_input = TextAreaField(label='full_text_input',
                              description='Enter text here to translate.',
                              validators=[DataRequired(),
                                          Length(min=1, max=10000, message="Please enter 1-10000 characters.")])


