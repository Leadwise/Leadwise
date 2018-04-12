
#get text and split into tokens and parts of speech
import nltk
from nltk import pos_tag, word_tokenize, WhitespaceTokenizer
import sys
from sys import stdin
import random
from nltk.corpus import wordnet
from termcolor import cprint, colored

color = ["white", "yellow"]
on_color = ["on_red", "on_magenta", "on_blue", "on_grey"]

def tags(tag):
    if tag in {"NNP","NNS","NN","NNPS"}:
        POS_tag = 'noun'
    elif tag in {'VB','VBD','VBG','VBN','VBP','VBZ'}:
        POS_tag = 'verb'
    elif tag in {'RB','RBR','RBS','WRB', 'RP'}:
        POS_tag = 'adverb'
    elif tag in {'PRP','PRP$'}:
        POS_tag = 'pronoun'
    elif tag in {'JJ','JJR','JJS'}:
        POS_tag = 'adjective'
    elif tag == 'IN':
        POS_tag = 'preposition'
    elif tag == 'WDT':
        POS_tag = 'determiner'
    elif tag in {'WP','WP$'}:
        POS_tag = 'pronoun'
    elif tag == 'UH':
        POS_tag = 'interjection'
    elif tag == 'POS':
        POS_tag = 'possesive ending'
    elif tag == 'SYM':
        POS_tag = 'symbol'
    elif tag == 'EX':
        POS_tag = 'existential there'
    elif tag == 'DT':
        POS_tag = 'determiner'
    elif tag == 'MD':
        POS_tag = 'modal'
    elif tag == 'LS':
        POS_tag = 'list item marker'
    elif tag == 'FW':
        POS_tag = 'foreign word'
    elif tag == 'CC':
        POS_tag = 'coordinating conjunction '
    elif tag == 'CD':
        POS_tag = 'cardinal number'
    elif tag == 'TO':
        POS_tag = 'to'
    elif tag == '.':
        POS_tag = 'line ending'
    elif tag == ',':
        POS_tag = 'comma'
    else:
        POS_tag = tag
    return POS_tag

def POS_tagger(words):
    taggedwordlist = nltk.pos_tag(words)

    taglist = [pos for word,pos in taggedwordlist]
    POS_tags = []

    for item in taggedwordlist:
        postag = tags(item[1])
        POS_tags.append([item[0], postag])

    return POS_tags

def givemeone(postag, allthewords):
    filtered = []
    for wordgroup in allthewords:
        if wordgroup[1] == postag:
            filtered.append(wordgroup[0])
    return random.choice(filtered)

def alltags(allthewords):
    return [t[1] for t in allthewords]

def doslogan1():
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []
    structure1 = ['verb', 'noun', 'determiner', 'verb', 'determiner', random.choice(syns)]
    for index, item in enumerate(structure1):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))

def doslogan2():
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []
    structure1 = ['verb', 'preposition', 'determiner', random.choice(syns)]
    for index, item in enumerate(structure1):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))

def doslogan3():
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []
    structure1 = ['adjective', 'determiner', random.choice(syns)]
    for index, item in enumerate(structure1):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))

def doslogan4():
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []
    structure1 = ['verb', 'determiner', random.choice(syns)]
    for index, item in enumerate(structure1):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))

def doslogan5():
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []
    structure1 = [random.choice(syns), 'preposition', 'noun']
    for index, item in enumerate(structure1):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))



answer= input('Would you like to generate random slogans from the dataset? (y/n) ')
if answer == 'y' or answer == 'Y':
    syns = []
    syns.append('noun')
    print ('\nVery well, here is what I have for now:\n')
    for _ in range(0,5):
        doslogan1() 
        doslogan2() 
        doslogan3() 
        doslogan4() 
        doslogan5()
elif answer == 'n' or answer == 'N':
    topic = input('What topic would you like your slogan to have?\n ')
    syns = []
    for syn in wordnet.synsets(topic):
     
        for lemma in syn.lemmas():
     
            syns.append(lemma.name())
    print ('Ok then, here are your slogans:\n')
    for _ in range(0,5):
        doslogan1() 
        doslogan2() 
        doslogan3() 
        doslogan4() 
        doslogan5() 

print ('\nCopy your best slogans in a textfile with "CTRL+SHIFT+C"\n')

print ('\n\nDo you want to try one more time? \nThen, run "python3 generator.py" in the terminal (this black screen that you see) one more time.\n')
 



#ANOTHER VERSION OF OUTCOME
# inputnoun = input('Would you like to use your noun? Then type it now. If not type 2 ')
# if inputnoun != '2':
#     for _ in range(0,5):
#         doslogan5() 
# else:
#     inputverb = input('Would you like to use your verb? Then type it now. If not type 3 ')
#     if inputverb != '3':
#         for _ in range(0,5):
#             doslogan4()
#     else:
#         print ('Then let me do random slogans for you')
#         for _ in range(0,5):
#             doslogan1()
#             doslogan2()
#             doslogan3()
#             # doslogan4()
#             # doslogan5()




