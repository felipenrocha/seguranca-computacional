import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flaskr.models.frequency import frequencyLetters, frequencyTrigrams
from flaskr.models.vigenere import key_gen, encryption, decryption
    # create and configure the app

    
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        SECRET_KEY='dev'
    )
#setup forms
bootstrap = Bootstrap4(app)
criptogram = ''
# main route
@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = EncryptForm()
    criptogram = ''
    key = ''
    if form.validate_on_submit():
        message = form.message.data
        key_base = form.key.data
        key = key_gen(key_base, message)
        criptogram = encryption(key, message)
        #     key = key_gen(key_base, message)
        #     print('Messagem: ', message)
        #     print('Chave gerada: ', key)
        #     criptogram = encryption(key_base, message)
        #     print('\nMensagem Cifrada: ', criptogram , "\n")

    return  render_template('encrypt.html', form=form, key=key, criptogram=criptogram)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = EncryptForm()
    criptogram = ''
    key = ''
    if form.validate_on_submit():
        message = form.message.data
        key_base = form.key.data
        key = key_gen(key_base, message)
        criptogram = decryption(key, message)
        #     key = key_gen(key_base, message)
        #     print('Messagem: ', message)
        #     print('Chave gerada: ', key)
        #     criptogram = encryption(key_base, message)
        #     print('\nMensagem Cifrada: ', criptogram , "\n")

    return  render_template('decrypt.html', form=form, key=key, criptogram=criptogram)
@app.route('/ed', methods=['GET'])
def encryptAndDecrypt():
    return  render_template('part1.html')

#hack route
@app.route('/hack', methods=['GET', 'POST'])
def hack():
    keySize = 0
    form = TextForm()
    lettersDictionary = {}
    trigramsDictionary = {}


    # get value of criptogram 
    if form.validate_on_submit():
        criptogram = form.criptogram.data
        lettersDictionary = frequencyLetters(criptogram)
        trigramsDictionary = frequencyTrigrams(criptogram)
    
    return render_template('solver.html', form=form, frequencyDictionary=lettersDictionary, trigramsDictionary=trigramsDictionary, checkMultiple=checkMultiple) 



# form class 
class TextForm(FlaskForm):
    criptogram = TextAreaField("", validators=[DataRequired()])
    submit = SubmitField('Check frequency')

class EncryptForm(FlaskForm):
    message = TextAreaField("", validators=[DataRequired()])
    key = TextAreaField("", validators=[DataRequired()])
    submit = SubmitField('Encrypt/Decrypt')

def checkMultiple(multiple, number):
    if multiple % number == 0:
        return ' x '
    else:
        return ' '