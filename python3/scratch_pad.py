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

# whats the difference between a class & static method?


# https://stackoverflow.com/questions/5690888/variable-scopes-in-python-classes

class Test:
    a = None
    b = None

    def __init__(self, a):
        print(self.a)           # print self.a  < no brackets print statement remove in python 3
        self.a = a
        self._x = 123
        self.__y = 123
        b = 'meow'








def return_nutrinfo_dictionary():
    return {
            'servings': 0,
            'serving_size': 0,
            'yield': '0g',
            'units': 'g',
            'density': 1,            
            'n_En':0, 'n_Fa':0, 'n_Fs':0, 'n_Fm':0, 'n_Fp':0, 'n_Fo3':0, 'n_Ca':0,
            'n_Su':0, 'n_Fb':0, 'n_St':0, 'n_Pr':0, 'n_Sa':0, 'n_Al':0
            }
            
print("Nutridict")
# create content for json file
pprint({ 'sugar':return_nutrinfo_dictionary() })
pprint({ 'eggs':return_nutrinfo_dictionary() })
pprint({ 'flour':return_nutrinfo_dictionary() })
pprint({ 'milk':return_nutrinfo_dictionary() })
pprint({ 'pancakes':return_nutrinfo_dictionary() })



print("<\n\n")
            
# {'serving_size': 100.0, 'units':'g', 'n_En':0.0}
#nutrient = Nutrients('sugar', {'serving_size': 100.0, 'units':'g', 'n_En':400.0})
#pprint(nutrient)

print("= = SHOW GLOBAL VARLIST")
pprint(globals())
print("<\n\n")