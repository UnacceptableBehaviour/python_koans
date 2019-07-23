#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# the journey to enlightenment starts with a single step . . 
#
# and lots of head scratching and tests!
#

import sys
import json
from pprint import pprint 

    
class MyClass:
    def method(self_obj_ref):
        return 'instance method called', self_obj_ref

    @classmethod                                        # decorator
    def classMethod(class_obj_ref):
        return 'class method called', class_obj_ref

    @staticmethod                      # decorator
    def staticMethod():                # staticMethod(class_obj_ref):
        return 'static method called'  # return 'static method called', class_obj_ref
                                       # print( MyClass.staticMethod() )
                                       # TypeError: staticMethod() missing 1 required positional argument: 'class_obj_ref'
    
obj = MyClass()
print("Methods scope")
print("-- instance")
print( obj.method() )
print( MyClass.method(obj) )

print("-- class")
print( MyClass.classMethod() )
print( obj.classMethod() )

print("-- static")
print( MyClass.staticMethod() )
print( obj.staticMethod() )
print("<\n\n")

# whats the difference between a @classmethod & @staticmethod method?


# https://stackoverflow.com/questions/5690888/variable-scopes-in-python-classes

class Test:
    a = 9999                    # class scope visible in methods
    b = 'woof'

    def __init__(self, a):
        print(f"__init__ self.a {self.a}") # print self.a  < no brackets print statement removed in python 3
                                           # since no instance var exist the this retrieves the class var
        self.a = a                         # object scope a = a passed in
        print(f"__init__ self.a {self.a}") # print newly instantiated instance var - which now shadows class var
        print(f"__init__ Test.a {Test.a}") # class var now accessible with Test.a
        self._x = 123
        print(f"__init__ self._x {self._x}")
        self.__y = 345
        print(f"__init__ self.__y {self.__y}")
        print(f"__init__ self.b {self.b}")  # woof
        print(f"__init__ Test.b {Test.b}")  # woof
        b = 'meow'                          # var b local (assume on the stack) and
                                            # goes out of scope on exiting __init__
        print(f"__init__ self.b {self.b}")  # woof
        print(f"__init__ Test.b {Test.b}")  # woof
        print(f"__init__ b {b}")            # meow


print("-- class test")
tob = Test(4)
print( f"External Test.a {Test.a}" )            # 
print( f"External tob._x {tob._x}" )            # considered protected (underscore) - but no difference to self.a
#print( f"External Class Test._x {Test._x}" )   # AttributeError: type object 'Test' has no attribute '_x'
#print( f"External {tob.__y}" )                 # AttributeError: 'Test' object has no attribute '__y'
#print( f"External Class Test.__y {Test.__y}" ) # AttributeError: type object 'Test' has no attribute '__y'
print( f"External tob._Test__y {tob._Test__y}" ) # '__y' mangle to '_ClassName__y' in this case '_Test__y'
                                                # bad practice to access this way
print("<\n\n")







print("= = SHOW GLOBAL VARLIST")
pprint(globals())
print("<\n\n")