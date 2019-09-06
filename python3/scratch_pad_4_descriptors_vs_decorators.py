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
    #  Descriptor protocol
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# How to reference variables in different namespaces / scopes
# https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example
# https://stackoverflow.com/questions/2010692/what-does-mro-do
# -
class SuperColor:
    base_choice = False                             # find with dir(SuperColor)
    
    def __init__(self):
        print(f"ctor: {self}")
        self.choice = 'yella' # by default
        
    def __set__(self, obj, val):                   # comment in
        self.choice = val

color = SuperColor()                                # create an instance of SuperColor
#color = 'purple'                                    # what is this being assigned to?
                                                    # overwrite with a string 'purple'
                                                    # leads to AttributeError: 'str' object has no attribute 'choice'
                                                    # TODO why does this work in about_method_bindings (last test)
                                                    # and not here?

print("\n\n== SuperColor ==")
print(SuperColor)
print("\n== SuperColor.mro()")
print(SuperColor.mro())
print("\n== dir(SuperColor)")
print(dir(SuperColor))
print("\n== dir(color)")
print(dir(color))
print(id(color))
print(type(color))
# == SuperColor ==
# <class '__main__.SuperColor'>
# 
# == SuperColor.mro()
# [<class '__main__.SuperColor'>, <class 'object'>]
# 
# == dir(SuperColor)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'base_choice']   << base_choice ******
# 
# == dir(color)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'base_choice', 'choice']   << choice  *******
# 4460028592
# <class '__main__.SuperColor'>
# <__main__.SuperColor object at 0x109d6a2b0>
# yella


print(color)
print(color.choice)
print("\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 
    #  Decorators - https://www.datacamp.com/community/tutorials/decorators-python
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def print_message(message):
    decorate = "Outer Limits"                   # functions declared in same scope have access to this scope
    
    def message_sender():
        #decorate = "Inner Limits"              # < comment#
        print(message, decorate)                           #  
                                                           #  
    message_sender()                                       #  
                                                           #  
print_message("Welcome to the")                 # Welcome to the Outer limits


# # # # # # # # # # # # # # # # # # # # # # # #
# implementin a decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

print(say_hi())                                 # runs decorator - other code still works!
print()
# # # # # # # # # # # # # # # # # # # # # # # #

pancakes_w_each = '''200g flour     # sieved
220g (4) eggs   # beaten
200g     milk
3g salt    # all whisked together'''

pancakes = '''200g flour     # sieved
220g eggs   # beaten
200g     milk
3g salt    # all whisked together'''


def split_lines_into_qty_ingredient_prep(f):
    def wrapper():
        list_of_lines = f()                     # 
        list_of_ingredients = []
        
        for l in list_of_lines:
            qty_ingredient = l
            prep = ''
            match = re.match(r'^(.*?)#(.*?)$', l, re.DOTALL )
            if match:
                prep = match.group(2)
                qty_ingredient = match.group(1).strip()
            
            match = re.match(r'^(\d+g|kg|l|ml)(.*?)$', qty_ingredient, re.DOTALL)
            if match:
                list_of_ingredients.append({"qty": match.group(1), "ingredient": match.group(2).strip(), "prep":prep })
                        
        return list_of_ingredients
    
    return wrapper


def split_recipe_into_lines(f):
    def wrapper():
        recipe = f().lower()
        return recipe.split("\n")

    return wrapper


@split_lines_into_qty_ingredient_prep
@split_recipe_into_lines
def get_recipe():
    data_stream = pancakes
    return data_stream


for line in get_recipe():
    print(line)

