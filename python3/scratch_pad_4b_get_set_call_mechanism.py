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
    #  GET/SET call mechanism: Attributes / Descriptor protocol
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# see about_attribute_access.py ln:166

# TODO instrument
# https://stackoverflow.com/questions/14787334/confused-with-getattribute-and-setattribute-in-python

class O1(object):
    def __getattr__(self, name):
        return "__getattr__ has the lowest priority to find {}".format(name)

class O2(O1):
    var = "Class variables and non-data descriptors are low priority"
    def method(self): # functions are non-data descriptors
        return self.var

class O3(O2):
    def __init__(self):
        self.var = "instance variables have medium priority"
        self.method = lambda: self.var # doesn't recieve self as arg

class O4(O3):
    @property # this decorator makes this instancevar into a data descriptor
    def var(self):
        return "Data descriptors (such as properties) are high priority"

    @var.setter # I'll let O3's constructor set a value in __dict__
    def var(self, value):
        self.__dict__["var"]  = value # but I know it will be ignored

class O5(O4):
    def __getattribute__(self, name):
        if name in ("magic", "method", "__dict__"): # for a few names
            return super(O5, self).__getattribute__(name) # use normal access

        return "__getattribute__ has the highest priority for {}".format(name)
    
    
# TODO egs in link    
    