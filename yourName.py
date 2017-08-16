#! /usr/bin/env python

name = ''
while True:
    print('Please type your name.')
    name = raw_input() # use raw_input not input
    if name == 'your name':
        break
print('Awww break out! Thank you!')
