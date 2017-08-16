#! /usr/bin/env python

# Take user input to geuss a randomly determined number
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Go ahead and take a guess, fool')
    guess = int(raw_input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # guessed correctly
if guess == secretNumber:
    print('Well done. You are officially psychic now. It took you ' +
          '%d guesses to get the answer which of course was: %d. ' %
          (guessesTaken, secretNumber))
else:
        print('You fool! The number is %d.' % secretNumber)
