# get data from json file
import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # for close matches
    elif len(get_close_matches(word, data.keys()))>0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input('Press y for yes or n for no')
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return 'Invalid word...Please check this once'
        else:
            return 'You have entered wrong input. Please enter just y or n'
    else:
        return 'Invalid word...Please check this once'

word = input('Enter word:')
output = translate(word)
#print(output)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)

