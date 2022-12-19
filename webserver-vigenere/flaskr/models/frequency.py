#### file to calculate frequency of letters in messages
from unidecode import unidecode
import string
alfabeto = 'abcdefghijklmnopqrstuvxwyz'


def frequencyLetters(message):

    """string -> dictionary of frequency of each letter"""
    # turn all letters to upper case:
    message = message.upper()
    message = unidecode(message)
    frequencyDictionary = dict()
    for letter in message:
        if letter in frequencyDictionary.keys():
            #todo refactor
            # soma um da frequencia de cada letra
            frequencyDictionary[letter] = frequencyDictionary[letter] + 1
        else:
            frequencyDictionary.update({letter: 1})
    return frequencyDictionary


def frequencyTrigrams(message):
    message = message.upper()
    frequencyTrigrams = list()
    for b, c in trigram_counter(message):
        if c > 1 and ' ' not in b:
            frequencyTrigrams.append({"name": b,  "frequency": c, "spacing": findSpacing(b, message)})
    return frequencyTrigrams

def findSpacing(trigram, message):
    first_index= message.find(trigram)
    new_string = message[first_index+1:]
    second_index = new_string.find(trigram) + first_index + 1
    if second_index != -1:
       return second_index - first_index 
    else:
        return second_index



def trigram_counter(s):
    
    s = unidecode(s)
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("\r", "")
    # CODE FROM: https://stackoverflow.com/questions/74087541/bigrams-of-letters
    if len(s := s.upper()) > 1:
        c = {}
        for i in range(len(s)-1):
            if len(bi := s[i:i+3].strip('. ')) == 3 and (' ' or '  ') not in bi:
                c[bi] = c.get(bi, 0) + 1
        return [(t) for t in c.items()]




def getChartValues(criptogram, currentLetter, keySize):
    criptogram = unidecode(criptogram)
    criptogram = criptogram.translate(str.maketrans('', '', string.punctuation))
    criptogram = criptogram.lower()
    criptogram = criptogram.replace(" ", "")
    criptogram = criptogram.replace("\n", "")
    criptogram = criptogram.replace("\r", "")



    i = currentLetter - 1
    freqLetters = {}
    for letter in alfabeto:
        freqLetters[letter] = 0
    while i < len(criptogram):
        if criptogram[i] in freqLetters.keys():
            freqLetters[criptogram[i]] = freqLetters[criptogram[i]]+1
        i = i+keySize

    return freqLetters