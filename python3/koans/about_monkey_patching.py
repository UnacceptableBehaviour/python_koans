#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Related to AboutOpenClasses in the Ruby Koans
#

from runner.koan import *

class AboutMonkeyPatching(Koan):
    class Dog:
        def bark(self):
            return "WOOF"

    def test_as_defined_dogs_do_bark(self):
        fido = self.Dog()
        self.assertEqual("WOOF", fido.bark())

    # ------------------------------------------------------------------

    # Add a new method to an existing class.
    def test_after_patching_dogs_can_both_wag_and_bark(self):
        def wag(self): return "HAPPY"
        self.Dog.wag = wag                      # add method to class
    
        fido = self.Dog()
        self.assertEqual("HAPPY", fido.wag())   # run it - what about defining vars accessin class vars etc?
        self.assertEqual("WOOF", fido.bark())

        def fart(self, eaten):
            belly_do = {'beans':'giant wiffy fart', 'bone': 'sqeaky fart'}
            return belly_do[eaten] 
        
                
        #print(fart('beans')) # TypeError: fart() missing 1 required positional argument: 'eaten'
        print(fart(self,'beans'))        
        print(fart(self,'bone'))
        self.Dog.fart = fart

        dido = self.Dog()
        self.assertEqual('giant wiffy fart', dido.fart("beans"))   # run it - what about defining vars accessin class vars etc?
        self.assertEqual('sqeaky fart', dido.fart('bone'))

        # self.Dog.fart = lambda self, eaten: belly_do = {'beans':'giant wiffy fart', 'bone': 'sqeaky fart'}; return belly_do[eaten] 
        # self.Dog.fart = lambda self, eaten: belly_do = {'beans':'giant wiffy fart', 'bone': 'sqeaky fart'}; return belly_do[eaten] 
        #                ^
        # SyntaxError: can't assign to lambda- TODO Fix

    # ------------------------------------------------------------------

    def test_most_built_in_classes_cannot_be_monkey_patched(self):
        try:
            int.is_even = lambda self: (self % 2) == 0
        except Exception as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, "can't set attributes of built-in/extension type 'int'")

    # ------------------------------------------------------------------

    class MyInt(int): pass

    def test_subclasses_of_built_in_classes_can_be_be_monkey_patched(self):
        self.MyInt.is_even = lambda self: (self % 2) == 0

        self.assertEqual(False, self.MyInt(1).is_even())
        self.assertEqual(True, self.MyInt(2).is_even())
