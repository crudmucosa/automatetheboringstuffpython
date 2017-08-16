#! /usr/bin/env python

total = 0
print('Gimme a range (number)')
rangeTarget = int(raw_input())

for num in range(rangeTarget):
    total = total + num
print(total)
print('The range sum of 0 to %d is: %d' % (rangeTarget, total) )
