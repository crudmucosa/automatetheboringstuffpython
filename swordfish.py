#! /usr/bin/env python

oneTrueName = 'Schmo'
oneTruePassword = 'swordfish'

while True:
    print('Who are you?')
    name = raw_input()
    if name !=  oneTrueName:
        continue
    print('Hello %s. What is the password? (It is a fish)' % oneTrueName)
    password = raw_input()
    if password == oneTruePassword:
        break
print('Access granted.')
