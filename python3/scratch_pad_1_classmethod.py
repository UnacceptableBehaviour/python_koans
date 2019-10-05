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

class Error(Exception):
    '''Move this and other error classes to separate file: exceptions.py'''
    pass

class AccessError(Error):
    '''Raised when interface used incorrectly'''
    pass

class DemoMultipleCatch(Error):
    '''How to catch multiple exception types'''
    pass

class ResourceLocked(Error):
    '''No other threads yet so should not happen!'''
    pass
    

# Singleton interface for the NutrientsDB
class NutrientsDB:
    __nutrients_db_file = 'ingredient_db.json'
    __nutrients_db = {}
    __seek_misses = []
    __nutrients_loaded = False
    __instance = None
    __file_lock = False # threading.Lock()  # import threading

    @classmethod
    def getInstance(cls):
        '''Return handle to Nutrients Databas - simple file'''
        if NutrientsDB.__instance == None:
            NutrientsDB()
            
        return NutrientsDB.__instance

    @classmethod
    def get(cls, ingredient):
        '''Retrieve nutrients for an ingredient - local version'''
        if ingredient in NutrientsDB.__nutrients_db:
            return NutrientsDB.__nutrients_db[ingredient]
        else:
            NutrientsDB.__seek_misses.append(ingredient)
            return None
    
    @classmethod
    def set(cls, ingredient, nutridict={}):
        '''Shallow write to DB - locally stored'''
        NutrientsDB.__nutrients_db[ingredient] = nutridict


    @classmethod
    def commit(cls):
        '''Write the local version back to DB'''        
        # NutrientsDB.__file_lock.acquire()     # lock resource
        if NutrientsDB.__file_lock == False:
            NutrientsDB.__file_lock = True
            try:
                with open('ingredient_db.json', 'w') as f:
                    f.write(json.dumps(ingredient_db))
                
            except (NotImplementedError, DemoMultipleCatch) as e:
                print("WARNING FAILED to commit DB to disk")
                print(f"\n***\n{e} \n<")

            finally:
                f.close()
                # NutrientsDB.__file_lock.release()
                NutrientsDB.__file_lock = False
        else:
            raise ResourceLocked("Something unexpected going on squire.")
            
        
    # load DB if not loaded
    def __init__(self):
        if NutrientsDB.__instance != None:
            raise AccessError("Access NutrientsDB via getInstance() class method")
        else:
            NutrientsDB.__instance = self

        if NutrientsDB.__nutrients_loaded == False:
            try:
                with open(NutrientsDB.__nutrients_db_file, 'r') as f:
                    json_db = f.read()
                    NutrientsDB.__nutrients_db = json.loads(json_db)                    
                    NutrientsDB.__nutrients_loaded = True                    
            
            except NotImplementedError as e:
                print("WARNING Exception raised: getInstance FAILED to load DB")
                print(f"\n***\n{e} \n<")                        
    
    @classmethod
    def __len__(cls):
        return len(NutrientsDB.__nutrients_db.keys()) 





# creating ingredientes
class Ingredient:    
    
    # load DB if not loaded
    def __init__(self, ingredient, nutridict):
        self.name = ingredient
        self.nutrients = Nutrients(ingredient, nutridict)


ingredient_db = NutrientsDB.getInstance()
ingredient_db2 = NutrientsDB.getInstance()      # should be the same DB
#ingredient_db3 = NutrientsDB()                 # Exception: Access NutrientsDB via getInstance class method

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

