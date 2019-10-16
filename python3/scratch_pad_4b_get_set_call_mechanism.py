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


class OO1(object):
    def holly_cow(self):
        return 'moo'

    def poke_pig(self, times=1):
        return ['squeal' for i in range(times)]
        
    def __getattr__(self, name):                                                # called when AttributeError error
        return "__getattr__ has the lowest priority to find {}".format(name)    # is raised from
                                                                                # __get__           descriptor (and @property)
                                                                                # or
                                                                                # __getattribute__  attribute

class O1(object):
    def __getattr__(self, name):                                                # called when AttributeError error
        return "__getattr__ has the lowest priority to find {}".format(name)    # is raised from
                                                                                # __get__           descriptor (and @property)
                                                                                # or
                                                                                # __getattribute__  attribute

class O2(O1):
    var = "Class variables and non-data descriptors are low priority"
    def method(self): # functions are non-data descriptors
        return self.var
    
    
# TODO egs in link    
o1 = O1()
print(o1.var)               # '__getattr__ has the lowest priority to find var'
print(getattr(o1, 'var'))   # getattr(o1, 'var')  =equivalent to=  o1.var

print(":\n:OO1")
oo1 = OO1()
print(oo1.holly_cow)                    # <bound method OO1.holly_cow of <__main__.OO1 object at 0x1035c1d90>>
print(oo1.holly_cow())                  # 'moo'
print( getattr(oo1, 'holly_cow')   )    # <bound method OO1.holly_cow of <__main__.OO1 object at 0x1035c1d90>>
print( getattr(oo1, 'holly_cow')() )    # 'moo'
print( oo1.poke_pig(3) )                # ['squeal', 'squeal', 'squeal']
print(oo1.i_dont_exist)                 # __getattr__ has the lowest priority to find i_dont_exist
print(getattr(oo1, 'i_dont_exist'))     # __getattr__ has the lowest priority to find i_dont_exist
                                        # WERIDLY getattr() calls __getattribute__
                                        # ONLY WHEN that FAILS and an exception is raised is __getattr__ called
print(":\n:O2")
o2 = O2()
print(o2.var)                   # Class variables and non-data descriptors are low priority
print(o2.method)                # <bound method O2.method of <__main__.O2 object at 0x101432dd0>>
print(o2.method())              # Class variables and non-data descriptors are low priority
o2.var = 3
print(O2.var)                   # Class variables and non-data descriptors are low priority
print(o2.var)                   # 3
print(o2.i_dont_exist)          # '__getattr__ has the lowest priority to find i_dont_exist'  << FROM O1.__getattr__()
                                # WERIDLY getattr() calls __getattribute__                                  |
                                # ONLY WHEN that FAILS and an exception is raised is __getattr__ called - - /

class O3(O2):
    def __init__(self):
        self.var = "instance variables have medium priority"
        self.method = lambda: self.var # doesn't recieve self as arg

class O4(O3):
    @property # this decorator makes this instancevar into a data descriptor
    def var(self):
        return "Data descriptors (such as properties) are high priority"
        #return self.var    # RuntimeError: maximum recursion depth exceeded while calling a Python object
                            # causes call to @property . . . recursively

    @var.setter # I'll let O3's constructor set a value in __dict__
    def var(self, value):
        self.__dict__["var"]  = value # but I know it will be ignored       # TODO - WHY?
                                
print(":\n:O3")
o3 = O3()
print(o3.method)                # <function <lambda> at 0x10e530b18>                          < < < #
print(o3.method())              # instance variables have medium priority                           #
print(o3.var)                   # instance variables have medium priority                           #
                                                                                                    # different location
print(":\n:O4")                                                                                     # returning local var data
o4 = O4()                                                                                           # allocated in super class
                                #   method() inherited from O3                                      #
                                #   the lambda returns self.var accessed through @property in O4    #
print(o4.method())              # Data descriptors (such as properties) are high priority           #
                                #   assuming a unique lambda is assigen per object?                 #
print(o4.method)                # <function <lambda> at 0x10b3a80c8>                          < < < #
print(o4.var)                   # Data descriptors (such as properties) are high priority

print(o4.__dict__["var"])       # instance variables have medium priority
pprint(o4.__dict__)             # {'method': <function O3.__init__.<locals>.<lambda> at 0x109043b90>,
                                #  'var': 'instance variables have medium priority'}
#pprint(getattr(o4, '__dict__')) # same as ^
#pprint(vars(o4))                # same as ^

#print(dir(o4))                 # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'method', 'var']
show_selected = ['__class__', '__delattr__', '__dict__',  '__doc__', '__getattr__', '__getattribute__', '__init__', '__module__',  '__repr__', '__setattr__',  'method', 'var']
#for attribute in dir(o4):
for attribute in show_selected:
    print(f"\n{attribute}")
    pprint(getattr(o4, attribute)) 

# of interest:
# __getattr__
# <bound method O1.__getattr__ of <__main__.O4 object at 0x10449a250>>
#               ^
# __getattribute__
# <method-wrapper '__getattribute__' of O4 object at 0x10449a250>
# 
# __init__
# <bound method O3.__init__ of <__main__.O4 object at 0x10449a250>>
#               ^
# __repr__
# <method-wrapper '__repr__' of O4 object at 0x10449a250>
# 
# __setattr__
# <method-wrapper '__setattr__' of O4 object at 0x10449a250>
# 
# __dict__                                                                  __dict__ from O4
# {'method': <function O3.__init__.<locals>.<lambda> at 0x10449cb90>,       
#  'var': 'instance variables have medium priority'}                        attribute inherited from O3
#                                                                            - overriden by @property from O4    
#                                                                                                          |
# method                                                                    method from O3                 |
# <function O3.__init__.<locals>.<lambda> at 0x10449cb90>                                                  |
#                                                                                                          |
# var                                                                       @property from O4  < - - - - - /         
# 'Data descriptors (such as properties) are high priority'

# TODO - Deep dive on inspect module
#print("\n\n\nhttps://docs.python.org/3/library/inspect.html\n")

class O5(O4):
    def __getattribute__(self, name):
        if name in ("magic", "method", "__dict__"): # for a few names
            
            print("O5__getattribute__ S")
            pprint(self)
            pprint(super(O5, self).__getattribute__)
            print(name)
            print("O5__getattribute__ E")
            
            return super(O5, self).__getattribute__(name) # use normal access

        return "__getattribute__ has the highest priority eep {}".format(name)

print("\n:\n:O5")
o5 = O5()
print(o5.method)            # <function O3.__init__.<locals>.<lambda> at 0x104baec20>
                                # O5__getattribute__ S
                                    # <__main__.O5 object at 0x10a2a2410>
                                    # <method-wrapper '__getattribute__' of O5 object at 0x10a2a2410>
                                    # __dict__                  << 1st - - - - - < <
                                # O5__getattribute__ E
                                # O5__getattribute__ S
                                    # <__main__.O5 object at 0x10a2a2410>
                                    # <method-wrapper '__getattribute__' of O5 object at 0x10a2a2410>
                                    # method                    << using __dict__['method'] ? - - - - - < <
                                # O5__getattribute__ E
                                # <function O3.__init__.<locals>.<lambda> at 0x10a2a4c20>
print("-\n")                    # -

print(o5.var)               # __getattribute__ has the highest priority eep var   < < < \
print("-\n")                # -                                                          | 
                            #                                                            | same as trying to access var
print(o5.method())          # __getattribute__ has the highest priority eep var < < < < /
                                # O5__getattribute__ S
                                    # <__main__.O5 object at 0x10a2a2410>
                                    # <method-wrapper '__getattribute__' of O5 object at 0x10a2a2410>
                                    # method
                                # O5__getattribute__ E
                                # __getattribute__ has the highest priority eep var
print("-\n")                    # -

print(o5.__dict__["var"])   # instance variables have medium priority
print("-\n")
print(o5.magic)             # __getattr__ has the lowest priority to find magic
                                # super doesn't find, raises exception and finally executes
                                # O1.__getattr__()


print("\n\n")
for attribute in show_selected:
    print(f"\n{attribute}")
    pprint(getattr(o5, attribute)) 

# __class__
# '__getattribute__ has the highest priority eep __class__'
# 
# __delattr__
# '__getattribute__ has the highest priority eep __delattr__'
# 
# __dict__
# O5__getattribute__ S
# <__main__.O5 object at 0x102ef9590>
# <method-wrapper '__getattribute__' of O5 object at 0x102ef9590>
# __dict__
# O5__getattribute__ E
# {'method': <function O3.__init__.<locals>.<lambda> at 0x102efbc20>,
#  'var': 'instance variables have medium priority'}
# 
# __doc__
# '__getattribute__ has the highest priority eep __doc__'
# 
# __getattr__
# '__getattribute__ has the highest priority eep __getattr__'
# 
# __getattribute__
# '__getattribute__ has the highest priority eep __getattribute__'
# 
# __init__
# '__getattribute__ has the highest priority eep __init__'
# 
# __module__
# '__getattribute__ has the highest priority eep __module__'
# 
# __repr__
# '__getattribute__ has the highest priority eep __repr__'
# 
# __setattr__
# '__getattribute__ has the highest priority eep __setattr__'
# 
# method
# O5__getattribute__ S
# <__main__.O5 object at 0x102ef9590>
# <method-wrapper '__getattribute__' of O5 object at 0x102ef9590>
# method
# O5__getattribute__ E
# <function O3.__init__.<locals>.<lambda> at 0x102efbc20>
# 
# var
# '__getattribute__ has the highest priority eep var'
