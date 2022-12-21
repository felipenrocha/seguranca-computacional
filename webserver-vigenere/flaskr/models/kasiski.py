## kasiski attack:


from unidecode import unidecode
import string
alfabeto = 'abcdefghijklmnopqrstuvxwyz'



def trigramCounter(message):
    """Function to return the spacing between each repeated trigram and the % of times that numbers from 2-20 are multiples from each spacing"""
    
    trigrams = [] # all trigrams from message ex.:[{"name": KIE, "position": 0}, ...]
    frequencyTrigrams = {} # dictionary used to calculate spacing ex.: "KIE": {"position":[1,6,19], "frequency": 3}:
    spacingList = [] # array to get spacing between each trigram ex.:[{name: KIE, "spacing": 353, "name": IEG, "spacing": 40, ...}]
    multiplesDict = {} # dictionary that has how many spacings are multiples of numbers from range to 2-20 ex.:{"2": 10%, "3":12%, ...}



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
            frequencyTrigrams[name] = {"position": [], "frequency": 0 }
        frequencyTrigrams[name]['position'].append(i)
        frequencyTrigrams[name]['frequency'] = frequencyTrigrams[name]['frequency'] + 1
<<<<<<< HEAD:webserver-vigenere/flaskr/models/kasiski.py
        
=======
    

>>>>>>> main:webserver-vigenere/flaskr/models/frequency.py
    # remove frequencies == 1 
    for name in list(frequencyTrigrams):
        trigram = frequencyTrigrams[name]
        if trigram['frequency'] == 1:
            del frequencyTrigrams[name]
    

    # find spacing between them:
    for name in list(frequencyTrigrams):
        trigram = frequencyTrigrams[name]
        # get spacing between positions:
        for i in range(len(trigram['position'])-1):
            spacing = trigram['position'][i+1] - trigram['position'][i]
            spacingList.append({"name": name, "spacing": spacing})
    


    # get most common divider between 2-20:  
    # push all spacings
    for i in range(len(spacingList)):
        spacing = spacingList[i]['spacing']
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
    return [spacingList, multiplesDict]





def getFrequencies(criptogram, currentLetterIndex, keySize):
    """Function to return the frequency of each letter in positions [currentLetterIndex, currentLetterIndex + keySize, ...]"""

    criptogram = normalize_string(criptogram)   # normalize string
    i = currentLetterIndex - 1 # index = currentLetterIndex - 1    
    freqLetters = {} # freqLetters = {"a": 10.2, "b": 3.5, ...  }
    totalCharacters = len(criptogram) / keySize # total number of charecters scanned (number of characters / size of key)
    


    # push all letters to dict
    for letter in alfabeto:
        freqLetters[letter] = 0

    #get frequencies    
    while i < len(criptogram):
        letter = criptogram[i]
        freqLetters[letter] = freqLetters[letter]+1

        
        i = i + keySize # add loop to key size

    # transform into %
    for letter in freqLetters:
        freqLetters[letter] = round((freqLetters[letter] / totalCharacters) * 100, 2)

    return freqLetters


# support functions

def normalize_string(criptogram):
    """Remove undesired characters from criptogram"""
    criptogram = criptogram.lower()
    # remove spaces
    criptogram = criptogram.replace(" ","")
    # remove punctuation
    criptogram = criptogram.translate(str.maketrans('', '', string.punctuation))
    # remove numbers
    criptogram = ''.join([i for i in criptogram if not i.isdigit()])
    criptogram = remove_non_ascii(criptogram)

    return criptogram


def remove_non_ascii(string):
    return ''.join(char for char in string if ord(char) < 128)
