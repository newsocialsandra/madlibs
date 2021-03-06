"""A madlibs machine."""

import shelve
import re
import random

# Open and save text in variable
textfile = open('text.txt')
oldtext = textfile.readlines()
textfile.close()

# Open shelve database to store user input
shelffile = shelve.open('words', writeback=True)

# If shelffile is empty, set it up with these keys
if not shelffile:
    adjectives = []
    nouns = []
    verbs = []
    shelffile['adjectives'] = adjectives
    shelffile['nouns'] = nouns
    shelffile['verbs'] = verbs

# Prompt user for adjective, noun, verb and noun
shelffile['adjectives'].append(input('Type an adjective: '))
shelffile['nouns'].append(input('Type a noun: '))
shelffile['verbs'].append(input('Type a verb: '))
shelffile['nouns'].append(input('Type another noun: '))

# Comment these three out to see all stored words
# print (shelffile["adjectives"])
# print (shelffile["nouns"])
# print (shelffile["verbs"])


# Find and replace placeholders in text with randon choices from db
newtext = []
for line in oldtext:
    line = re.findall(r"[\w']+", line)
    for word in line:
        if word == 'ADJECTIVE':
            newtext.append(random.choice(shelffile['adjectives']))
        elif word == 'NOUN':
            newtext.append(random.choice(shelffile['nouns']))
        elif word == 'VERB':
            newtext.append(random.choice(shelffile['verbs']))
        else:
            newtext.append(word)

# Print new text and save to text file
# TODO: Add formatting so new text matches old text
print (' '.join(newtext))

newfile = open('newtext.txt', 'w')
newfile.write(' '.join(newtext))

newfile.close()
shelffile.close()
