__author__ = 'trevor'

from flask import render_template, request
from app import translyator, nlp
from .forms import TextForm


@translyator.route('/', methods=['GET', 'POST'])
def home():
    form = TextForm()
    return render_template('index.html', form=form)

@translyator.route('/read', methods=['GET', 'POST'])
def read():
    form = TextForm(request.form)
    if request.method == 'POST' and form.validate():
        translyator.logger.debug('Handling POST')
        entered_text = unicode(form.full_text_input.data)
        content = nlp.process_text(entered_text,
                                   '')
        return content
    return ""

