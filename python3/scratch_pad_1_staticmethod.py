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

    
# 
# def return_nutrinfo_dictionary(ingredient='name'):
#     return {
#             'name': ingredient,
#             'servings': 0,
#             'serving_size': 0,
#             'yield': '0g',
#             'units': 'g',
#             'density': 1,            
#             'n_En':0, 'n_Fa':0, 'n_Fs':0, 'n_Fm':0, 'n_Fp':0, 'n_Fo3':0, 'n_Ca':0,
#             'n_Su':0, 'n_Fb':0, 'n_St':0, 'n_Pr':0, 'n_Sa':0, 'n_Al':0
#             }
#             
# print("Nutridict")
# # create content for json file
# pprint({ 'sugar':return_nutrinfo_dictionary('sugar') })
# pprint({ 'eggs':return_nutrinfo_dictionary('eggs') })
# pprint({ 'flour':return_nutrinfo_dictionary('flour') })
# pprint({ 'milk':return_nutrinfo_dictionary('milk') })
# pprint({ 'pancakes':return_nutrinfo_dictionary('pancakes') })
# print("<\n\n")
            
# {'serving_size': 100.0, 'units':'g', 'n_En':0.0}
#nutrient = Nutrients('sugar', {'serving_size': 100.0, 'units':'g', 'n_En':400.0})
#pprint(nutrient)


class Nutrients:
    def __init__(self, ingredient='name_of_ingredient', nutridict={}): # nutridict={}):
        self.nutridict = {                  # self.nutridict - instance var
            'name': ingredient,
            'servings': 0,
            'serving_size': 0.0,
            'yield': '0g',
            'units': 'g',
            'density': 1, 
            'n_En':0.0,   # energy
            'n_Fa':0.0,   # fat
            'n_Fs':0.0,   # fat-saturates
            'n_Fm':0.0,   # fat-mono-unsaturates
            'n_Fp':0.0,   # fat-poly-unsaturates
            'n_Fo3':0.0,  # fat-omega_3
            'n_Ca':0.0,   # carbohydrates
            'n_Su':0.0,   # sugars
            'n_Fb':0.0,   # fibre
            'n_St':0.0,   # starch
            'n_Pr':0.0,   # protein
            'n_Sa':0.0,   # salt
            'n_Al':0.0    # alcohol
        }.update(nutridict)  #(nutridict - passed in)
        
        #self.ri_id = Ingredient.ingredientLookUp(ingredient, self.nutridict) 


# How to create a singleton for the Nutrients DB?
class IngredientsDB:
    __ingredient_db_file = 'ingredient_db.json'
    __ingredient_db = {}
    __ingredients_loaded = False
    __instance = None
    __file_locked = False

    @staticmethod
    def getInstance():
        if IngredientsDB.__instance == None:
            IngredientsDB()
            
        return IngredientsDB.__instance

    @staticmethod
    def get(ingredient):                
        if ingredient in IngredientsDB.__ingredient_db:
            return IngredientsDB.__ingredient_db[ingredient]
        else:
            return None
    
    @staticmethod
    def set(ingredient, nutridict={}):
        
        # lock resource
        if IngredientsDB.__file_locked == False:
            IngredientsDB.__ingredient_db[ingredient] = nutridict
        else:
            # learn about threads & resource locks in python!
            raise NotImplementedError("Surprise in a sequential environment!")

    @staticmethod
    def commit():        
        # lock resource
        IngredientsDB.__file_locked = True
                    
        try:
            with open('ingredient_db.json', 'w') as f:
                f.write(json.dumps(ingredient_db))
        
        # https://realpython.com/the-most-diabolical-python-antipattern/    
        except Exception as e:
            print("WARNING FAILED to commit DB to disk")
            print(f"\n***\n{e} \n<")

        else:
            IngredientsDB.__file_locked = False
        
    # load DB if not loaded
    def __init__(self):
        if IngredientsDB.__instance != None:
            raise Exception("Access IngredientsDB via getInstance() class method")
        else:
            IngredientsDB.__instance = self

        if IngredientsDB.__ingredients_loaded == False:
            try:
                with open(IngredientsDB.__ingredient_db_file, 'r') as f:
                    json_db = f.read()
                    IngredientsDB.__ingredient_db = json.loads(json_db)                    
                    IngredientsDB.__ingredients_loaded = True                    
            
            # https://realpython.com/the-most-diabolical-python-antipattern/
            except Exception as e:
                print("WARNING Exception raised: getInstance FAILED to load DB")
                print(f"\n***\n{e} \n<")                        
    
    @staticmethod
    def __len__():
        return len(IngredientsDB.__ingredient_db.keys()) 





# creating ingredientes
class Ingredient:    
    
    # load DB if not loaded
    def __init__(self, ingredient, nutridict):
        self.name = ingredient
        self.nutrients = Nutrients(ingredient, nutridict)


ingredient_db = IngredientsDB.getInstance()
ingredient_db2 = IngredientsDB.getInstance()      # should be the same DB
#ingredient_db3 = IngredientsDB()                 # Exception: Access IngredientsDB via getInstance class method

print("= = SHOW GLOBAL VARLIST")
pprint(globals())
print("<\n\n")

print("= = SHOW protagonists")
print("--> ingredient_db")
print(type(ingredient_db))
print(len(ingredient_db))
print(id(ingredient_db))

print("\n--> ingredient_db2")
print(type(ingredient_db2))
print(len(ingredient_db2))
print(id(ingredient_db2))

# print("\n--> ingredient_db3")
# print(type(ingredient_db3))
# print(len(ingredient_db3))
# print(id(ingredient_db3))
# 
pprint( ingredient_db.get('flour') )


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
print("\n\n== SuperColor.mro()")
print(SuperColor.mro())
print("\n\n== dir(SuperColor)")
print(dir(SuperColor))
print("\n\n== dir(color)")
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
