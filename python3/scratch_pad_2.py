#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# the journey to enlightenment starts with a single step . . 
#
# and lots of head scratching and tests!
#

from pprint import pprint 



t = set([1,2,-3])               # create a set t
t = set([1,2,3])               # create a set t
t = set([-1,-2,-3])               # create a set t
t2 = set([1,2,3])               # create a set t

type(list(t))                   # covert it to a list
 
for i in t:                     # iterate trhough set
    print(i)
    
print([i < 0 for i in t])       # use a list comprehension to scan it for -ve no's

print(set([i < 0 for i in t]))  # flatten the results

if True in set([i < 0 for i in t]):  # there's a -ve number in the set
    print("funky triangle")
    
if True in [i < 0 for i in t]:  # there's a -ve number in the set
    print("funky triangle")
    

# print(t)                        # set
# 
# print(max(t))                   # max vlue in set
# 
# print(t.remove(max(t)))         # remove it from set
# 
# print(t)                        # set
# 
# print(sum(t))                   # sum contents of set

t = list(t)


m = max(t)          # get max value
t.remove(m)         # remove it from the set

print(t)

if m >= sum(t):       # see its larger than the remaining set members
    print("funky triangle")
else:
    print("Aesome a triangle")

# in one line = we know the size

if max(t2)*2 >= sum(t2):         # sum(t2) include max(t2) so multiply max(2) to balance
    print("funky triangle")
    
    