import shelve
import re
import random

# Open and save text in variable

textfile = open('text.txt')
oldtext = textfile.readlines()
textfile.close()

# Prompt user for adjective, noun, verb and noun
# Save user input in shelve databse
shelffile = shelve.open('words', writeback=True)

# TODO: add an if-statement that skips these six lines
# if the database isn't empty
adjectives = []
nouns = []
verbs = []
shelffile['adjectives'] = adjectives
shelffile['nouns'] = nouns
shelffile['verbs'] = verbs

shelffile['adjectives'].append(input('Type an adjective: '))
shelffile['nouns'].append(input('Type a noun: '))
shelffile['verbs'].append(input('Type a verb: '))
shelffile['nouns'].append(input('Type another noun: '))

print (shelffile["adjectives"])
print (shelffile["nouns"])
print (shelffile["verbs"])


# Find and replace placeholders in text with users input
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

print (newtext)

newfile = open('newtext.txt', 'w')
newfile.write(' '.join(newtext))
newfile.close()

shelffile.close()
