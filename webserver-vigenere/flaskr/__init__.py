import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flaskr.models.frequency import frequencyLetters, frequencyTrigrams
    # create and configure the app

    
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        SECRET_KEY='dev'
    )
#setup forms
bootstrap = Bootstrap4(app)
criptogram = ''
# main route
@app.route('/', methods=['GET', 'POST'])
def home():
    keySize = 0
    form = TextForm()
    lettersDictionary = {}
    trigramsDictionary = {}


    # get value of criptogram 
    if form.validate_on_submit():
        criptogram = form.criptogram.data
        lettersDictionary = frequencyLetters(criptogram)
        trigramsDictionary = frequencyTrigrams(criptogram)
    
    return render_template('home.html', form=form, frequencyDictionary=lettersDictionary, trigramsDictionary=trigramsDictionary, checkMultiple=checkMultiple) 



# form class 
class TextForm(FlaskForm):
    criptogram = TextAreaField("", validators=[DataRequired()])
    submit = SubmitField('Check frequency')


def checkMultiple(multiple, number):
    if multiple % number == 0:
        return ' x '
    else:
        return ' '