#### file to calculate frequency of letters in messages
from unidecode import unidecode
import string
alfabeto = 'abcdefghijklmnopqrstuvxwyz'



def trigramCounter(message):
    trigrams = []
    frequencyTrigrams = {}
    message =  unidecode(message)
    message = message.replace(" ", "")
    message = message.translate(str.maketrans('', '', string.punctuation))

    # push all trigrams: 
    for i in range(len(message)):
        trigram = message[i:i+3]
        trigrams.append({"name": trigram, "position": i})
    
    # check for repeated ones 
    for i in range(len(trigrams)):
        trigram = trigrams[i]
        name = trigram['name']
        if name not in frequencyTrigrams.keys():
            frequencyTrigrams[name] = {"position": [i], "frequency": 1 }
        else:
            frequencyTrigrams[name]['position'].append(i)
            frequencyTrigrams[name]['frequency'] = frequencyTrigrams[name]['frequency'] + 1
    

    # remove frequencies == 1 
    for name in list(frequencyTrigrams):
        trigram = frequencyTrigrams[name]
        if trigram['frequency'] == 1:
            del frequencyTrigrams[name]
    chartList = []
    # find spacing between them:
    for name in list(frequencyTrigrams):
        trigram = frequencyTrigrams[name]
        # get spacing between positions:
        for i in range(len(trigram['position'])-1):
            spacing = trigram['position'][i+1] - trigram['position'][i]
            chartList.append({"name": name, "spacing": spacing})
    


    # get most common multiple between 2-20
    multiplesDict = {}
    # push all spacings
    for i in range(len(chartList)):
        spacing = chartList[i]['spacing']
        for j in range(2,20):
            if str(j) not in multiplesDict.keys():
                multiplesDict[str(j)] = 0  
            if spacing % j == 0:
                multiplesDict[str(j)] = multiplesDict[str(j)] + 1
    # transform into %
    total = 0
    for number in multiplesDict:
        total = total + multiplesDict[number]
    for number in multiplesDict:
        multiplesDict[number] = round((multiplesDict[number] / total) * 100,  2)
    
    print("MultiplesDict", multiplesDict)
    return [chartList, multiplesDict]




def getChartValues(criptogram, currentLetter, keySize):
       
    criptogram = criptogram.lower()
    # remove spaces
    criptogram = criptogram.replace(" ","")
    # remove punctuation
    criptogram = criptogram.translate(str.maketrans('', '', string.punctuation))
    # remove numbers
    criptogram = ''.join([i for i in criptogram if not i.isdigit()])
    criptogram = remove_non_ascii(criptogram)



    # index = index - 1 
    i = currentLetter - 1 
    freqLetters = {}
    for letter in alfabeto:
        freqLetters[letter] = 0
    while i < len(criptogram):
        letter = criptogram[i]
        freqLetters[letter] = freqLetters[letter]+1
        i = i + keySize
    total = len(criptogram) / keySize
    for letter in freqLetters:
        freqLetters[letter] = round((freqLetters[letter] / total) * 100, 2)

    print(freqLetters)
    return freqLetters


def remove_non_ascii(string):
    return ''.join(char for char in string if ord(char) < 128)
