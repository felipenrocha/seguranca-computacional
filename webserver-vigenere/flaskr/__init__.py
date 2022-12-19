import os

from flask import Flask, render_template, redirect, url_for, request, json
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired
from flaskr.models.frequency import frequencyLetters, frequencyTrigrams, getChartValues
from flaskr.models.vigenere import key_gen, encryption, decryption
from flask_wtf.csrf import CSRFProtect
    
    # create and configure the app

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "current_criptogram.json")

app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config.from_mapping(
        SECRET_KEY='dev'
    )
#setup forms
bootstrap = Bootstrap4(app)

# main route
@app.route('/')
def home():
    return  render_template('index.html')


# PART 1 ROUTE
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
    return  render_template('decrypt.html', form=form, key=key, criptogram=criptogram)
@app.route('/ed', methods=['GET'])
def encryptAndDecrypt():
    return  render_template('part1.html')




#hack route (PART2)
@app.route('/hack', methods=['GET', 'POST'])
def hack():
    keySize = 0
    form = TextForm()
    keySizeForm = KeySizeForm()
    
    criptogram = ''
    lettersDictionary = {}
    trigramsDictionary = {}
    if form.submit.data and form.validate_on_submit() and request.method == 'POST':
        
        criptogram = form.criptogram.data # get value of criptogram
        lettersDictionary = frequencyLetters(criptogram)
        trigramsDictionary = frequencyTrigrams(criptogram)
        json_dump = {"criptogram": criptogram, "lettersDictionary": lettersDictionary, "trigramsDictionary": trigramsDictionary} # persisting the criptogram for later (unfortenetely):

        with open(json_url, "w", encoding="utf8") as write_file:
            json.dump(json_dump, write_file, indent=4)
        print("in form 1")
        
        return redirect('/hack-part-two', code=302) 

    if keySizeForm.validate_on_submit() and request.method == 'POST' :
        criptogram  = getCurrentCriptogram()
        
        if criptogram:
            lettersDictionary = frequencyLetters(criptogram)
            trigramsDictionary = frequencyTrigrams(criptogram)
        value = keySizeForm.value.data
        return render_template('solver.html', form=form, form2=keySizeForm, frequencyDictionary=lettersDictionary, trigramsDictionary=trigramsDictionary, checkMultiple=checkMultiple, keySize=int(value)) 
    return render_template('solver.html', form=form, form2=keySizeForm, frequencyDictionary=lettersDictionary, trigramsDictionary=trigramsDictionary, checkMultiple=checkMultiple) 

    
#hack route (PART2)
@app.route('/hack-part-two', methods=['GET', 'POST'])
def hack_two():
    keySizeForm = KeySizeForm()
    lettersDictionary = getCurrentDictionary()['lettersDictionary']
    trigramsDictionary = getCurrentDictionary()['trigramsDictionary']


    if keySizeForm.submit.data and keySizeForm.validate_on_submit() and request.method == 'POST':
        value = int(keySizeForm.value.data)
        print("value", keySizeForm.value.data)
        return redirect('/hack-part-three/'+str(value), code=302)

    return render_template('solver2.html', form2=keySizeForm, frequencyDictionary=lettersDictionary, trigramsDictionary=trigramsDictionary, checkMultiple=checkMultiple) 



@app.route('/api/frequency', methods=['POST'])
def frequency():
    req = request.get_json()
    currentLetter = int(req['currentLetter'])
    keySize = int(req['keySize'])
    criptogram = getCurrentCriptogram()
    resp = getChartValues(criptogram=criptogram, currentLetter=currentLetter, keySize=keySize)
    print(resp)
    return resp


@app.route('/hack-part-three/<keysize>', methods=['GET', 'POST'])
def hack_three(keysize):
    
    return render_template('solver3.html', keySize=int(keysize)) 

def getCurrentCriptogram():
    jsonFile = {}
    with open(json_url, "r", encoding="utf8") as read_file:
        jsonFile = json.load(read_file)
    if jsonFile:
        return jsonFile['criptogram']
    else:
        return ''


def getCurrentDictionary():
    jsonFile = {}
    with open(json_url, "r", encoding="utf8") as read_file:
        jsonFile = json.load(read_file)
    return jsonFile



# form class 
class TextForm(FlaskForm):
    criptogram = TextAreaField("", validators=[DataRequired()], default=getCurrentCriptogram)
    submit = SubmitField('Check frequency')
class KeySizeForm(FlaskForm):
    value = StringField()
    submit = SubmitField('Select Key')

class EncryptForm(FlaskForm):
    message = TextAreaField("", validators=[DataRequired()])
    key = TextAreaField("", validators=[DataRequired()])
    submit = SubmitField('Encrypt/Decrypt')

def checkMultiple(multiple, number):
    if multiple % number == 0:
        return ' x '
    else:
        return ' '
