#### file to calculate frequency of letters in messages


def frequencyLetters(message):

    """string -> dictionary of frequency of each letter"""
    # turn all letters to upper case:
    message = message.upper()
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
    first_index= message.find(trigram) + 3
    new_string = message[first_index:]
    second_index = new_string.find(trigram) + first_index
    if second_index != -1:
       return second_index - first_index 
    else:
        return second_index



def trigram_counter(s):
    # CODE FROM: https://stackoverflow.com/questions/74087541/bigrams-of-letters
    if len(s := s.upper()) > 1:
        c = {}
        for i in range(len(s)-1):
            if len(bi := s[i:i+3].strip('. ')) == 3:
                c[bi] = c.get(bi, 0) + 1
        return [(t) for t in c.items()]





