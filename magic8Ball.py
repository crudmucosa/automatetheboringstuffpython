#! /usr/bin/env python

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'NO'
    elif answerNumber == 2:
        return 'Oh most definitely'
    elif answerNumber == 3:
        return 'Sure, why not?'
    elif answerNumber == 4:
        return 'YES'
    elif answerNumber == 5:
        return 'Why not ask again?'
    elif answerNumber == 6:
        return 'Use the Force...then ask someone else'
    elif answerNumber == 7:
        return 'Nope. No fricking way.'
    elif answerNumber == 8:
        return 'Prospects aren\'t great'
    elif answerNumber == 9:
        return 'Doubtful'
    elif answerNumber == 10:
        return 'Doubtful'

r = random.randint(1, 10)
fortune = getAnswer(r)
#print('The number is ' + str(r))
print(fortune)
