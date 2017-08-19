#! /usr/bin/env python

"""
Demonstrate the collatz sequence. Any number you enter should return 1. How
does this work? Who the heck knows!?
"""


def collatz(number):
    #check for even-ness
    if number % 2 == 0:
        return (number // 2)
    if number % 2 == 1:
        return (3 * number + 1)


print('Please enter a number:')
numberInput = int(raw_input())
numberOutput = collatz(numberInput)
while (numberOutput != 1):
        numberOutput = collatz(numberOutput)
        print(numberOutput)
