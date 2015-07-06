__author__ = 'trevor'

from flask import render_template, redirect, flash, request
from app import translyator, nlp
from .forms import TextForm

@translyator.route('/', methods=['GET', 'POST'])
def home():
    form = TextForm()
    if form.validate_on_submit():
        flash("Processing Text...")
        # call the main crap here? idfk...
        return redirect('/read')
    return render_template('index.html', form=form)


@translyator.route('/read', methods=['GET', 'POST'])
def read():
    if request.method == 'POST':
        translyator.logger.debug('Handling POST')
        entered_text = unicode(request.form['full_text'])
        content = nlp.process_text(entered_text, 'your_key')
        return content
