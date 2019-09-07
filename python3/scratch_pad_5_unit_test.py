#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# the journey to enlightenment starts with a single step . . 
#
# and lots of head scratching and tests!
#
import re
import sys
import json
from pprint import pprint 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 
    #  unit test:
    #  https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# check if a string has duplicate letters (an isogram has no duplicates) - kata from codewars.com 
def is_isogram(string):
    freq = {}                                   # frequency dictionary
    
    def is_duplicate(letter):                   # add occurance if not present
        if letter.lower() in freq:
            return True
        else:
            freq[letter] = 1
            return False    
    
    for c in string:                            # scan string
        if is_duplicate(c): return False
    
    return True
    pass

# conceptually
print(is_isogram("Dermatoglyphics") == True )
print(is_isogram("isogram") == True )
print(is_isogram("aba") == False )
print(is_isogram("moOse") == False )
print(is_isogram("isIsogram") == False )
print(is_isogram("") == True )

# implemenrtations?
# https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/
# Robot
# PyTest
# PyUnit
# Behave
# Lettuce