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

    

# def return_nutrinfo_dictionary():
#     return {
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
# pprint({ 'sugar':return_nutrinfo_dictionary() })
# pprint({ 'eggs':return_nutrinfo_dictionary() })
# pprint({ 'flour':return_nutrinfo_dictionary() })
# pprint({ 'milk':return_nutrinfo_dictionary() })
# pprint({ 'pancakes':return_nutrinfo_dictionary() })
# print("<\n\n")
            
# {'serving_size': 100.0, 'units':'g', 'n_En':0.0}
#nutrient = Nutrients('sugar', {'serving_size': 100.0, 'units':'g', 'n_En':400.0})
#pprint(nutrient)


class Nutrients:
    def __init__(self, ingredient, nutridict={}): # nutridict={}):
        self.nutridict = {                  # self.nutridict - instance var
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
class IngredientDB:
    __ingredient_db_file = 'ingredient_db.json'
    __ingredient_db = {}
    ingredients_loaded = False
    
        
    # load DB if not loaded
    def __init__(self):
        IngredientDB.loadIngredientsDB()                    


    @staticmethod
    def loadIngredientsDB():
        if IngredientDB.ingredients_loaded == False:
            try:
                with open(IngredientDB.__ingredient_db_file, 'r') as f:
                    json_db = f.read()
                    IngredientDB.__ingredient_db = json.loads(json_db)
                    IngredientDB.ingredients_loaded = True
            
            # https://realpython.com/the-most-diabolical-python-antipattern/
            except Exception as e:
                print("WARNING Exception raised: loadIngredientsDB")
                print(f"\n***\n{e} \n<")
            
        return( IngredientDB.__ingredient_db )
    

    @staticmethod
    def ingredientLookUp(ingredient, nutridict={}):
                
        if ingredient in IngredientDB.__ingredient_db:
            return IngredientDB.__ingredient_db[ingredient]
        else:
            #addIngredientToDB(ingredient, nutridict)
            print("Err . . implement addIngredientToDB() please")
    
    # @staticmethod
    # def addIngredientToDB(ingredient, nutridict={}):
    #     ingredient_db[ingredient] = len(ingredient_db.keys) + 1
    #     try:
    #         with open('ingredient_db.json', 'w') as f:
    #             f.write(json.dumps(ingredient_db))
    #     
    #     # https://realpython.com/the-most-diabolical-python-antipattern/    
    #     except Exception as e:
    #         print("WARNING Exception raised")
    #         print(f"\n***\n{e} \n<")

# creating ingredientes
class Ingredient:    
    
    # load DB if not loaded
    def __init__(self, ingredient, nutridict):
        self.name = ingredient
        self.nutrients = Nutrients(ingredient, nutridict)


ingredient_db = IngredientDB.loadIngredientsDB()
ingredient_db2 = IngredientDB.loadIngredientsDB()            # should be the same DB
print("ingredient_db")
print(type(ingredient_db))
print(len(ingredient_db))
print(id(ingredient_db))
print("ingredient_db2")
print(type(ingredient_db2))
print(len(ingredient_db2))
print(id(ingredient_db2))


print("= = SHOW GLOBAL VARLIST")
pprint(globals())
print("<\n\n")