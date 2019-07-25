#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# the journey to enlightenment starts with a single step . . 
#
# and lots of head scratching and tests!
#

from pprint import pprint 

s = [2, 3, 4, 6, 6, 1]

print(s)

print("comprehension")

print( [x for x in s if x != 2] )   # remove 2's

print( [x for x in s if x != 6] )   # remove 6's

print('filter')
print( list(filter(lambda x: x != 2, s)) )

print( list(filter(lambda x: x != 6, s)) )

print("generator - slice")
x = [2, 3, 4, 6, 6, 1]

x[:] = (value for value in x if value != 2)         # notation??
print(x)
x[:] = (value for value in x if value != 6)
print(x)

print("generator - list")
x = [2, 3, 4, 6, 6, 1]
print(list( (value for value in x if value != 2) ))
print(list( (value for value in x if value != 6) ))

print("what? . . ")
print( (value for value in x if value != 2) )   # <generator object <genexpr> at 0x1049b41b0>
print( (value for value in x if value != 6) )   # <generator object <genexpr> at 0x1049b41b0>
# oh!
print( list( (value for value in x if value != 2) ) )   # <generator object <genexpr> at 0x1049b41b0>
print( list( (value for value in x if value != 6) ) )   # <generator object <genexpr> at 0x1049b41b0>


print('for - range')
for number in range(1,7):                          # range(1-7) = range(0, -6) try range(1,7)
    print(f"number: {number}")
print('for - range done')


def score(immutable_dice):
    # You need to write this method
    score = 0
    dice = immutable_dice
    
    # count the 3 offs
    for number in range(1,7):
        print(f"number: {number}")
        if dice.count(number) >= 3:
            score += (number * 100)
            print(f"number: {number}")
            print(dice)
            print(score)
            
            if number == 1: score += 900                # 3 1's is a 1000, not 100!!
            
            for r in range(0-3): dice.remove(number)    # remove 3 dice - of relevant number
    
    # counte whats left, only 1's and 5's are worth anything
    values = { 1:100, 2:0, 3:0, 4:0, 5:50, 6:0 }
    
    for die in dice:
        try:
            score += values[die]
            
        except KeyError:
            print("Hold the dodgey die high in the air for all in the saloon to see and start blasting")
    
    return score

print( score([1,1,5,5,5]) )

print( score([1,1,1]) )

