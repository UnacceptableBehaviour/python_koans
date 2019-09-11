#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims
from . import joes

counter = 0 # Global

class AboutScope(Koan):
    #
    # NOTE:
    #   Look in jims.py and joes.py to see definitions of Dog used
    #   for this set of tests
    #

    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(NameError): fido = Dog()

    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        fido = jims.Dog()
        # name 'jims' module name is taken from jims.py filename

        rover = joes.Dog()
        self.assertEqual("jims dog", fido.identify())
        self.assertEqual("joes dog", rover.identify())
        
        print(type(fido))
        print(type(rover))
        self.assertEqual(False, type(fido) == type(rover))
        self.assertEqual(False, jims.Dog == joes.Dog)

    # ------------------------------------------------------------------

    class str:
        pass

    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        self.assertEqual(self.str, AboutScope.str)
        self.assertEqual(False, AboutScope.str == str)

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        print(self.str)
        print(type(self.str))
        print(self.str.__name__)
        print(type("HI"))        
        self.assertEqual(False, self.str == type("HI"))

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(True, str == type("HI"))

    # ------------------------------------------------------------------

    PI = 3.1416

    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        self.assertAlmostEqual(3.1416, self.PI)
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    def test_constants_are_assumed_by_convention_only(self):
        self.PI = "rhubarb"
        print(self.PI)
        self.assertEqual("rhubarb", self.PI)
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them. V.POOR, no privacy either f*** a d***

    # ------------------------------------------------------------------

    def increment_using_local_counter(self, counter):
        print(f"arg local counter ID:{id(counter)} VAL:{counter}")
        counter = counter + 1
        print(f"new local counter ID:{id(counter)} VAL:{counter}")
        # arg local counter ID:4512182464 VAL:1
        # new local counter ID:4512182496 VAL:2

    def increment_using_global_counter(self):
        global counter
        counter = counter + 1

    def test_incrementing_with_local_counter(self):
        global counter                      # defined at top
        start = counter                     # start refers to global counter < is that right? TODO
        print(f"global counter ID:{id(counter)} VAL:{counter}")
        print(f"start ID:{id(start)} VAL:{start}")
        # global counter ID:4512182464 VAL:1
        #          start ID:4512182464 VAL:1
        self.increment_using_local_counter(start)
        self.assertEqual( id(counter), id(start))
        self.assertEqual(False, counter == start + 1)   # global != ref to same global +1

    def test_incrementing_with_global_counter(self):        # 
        global counter
        print
        start = counter
        print(f"t2 - global counter ID:{id(counter)} VAL:{counter}")
        print(f"t2 - start ID:{id(start)} VAL:{start}")
        # t2 - global counter ID:4512182432 VAL:0                           << global counter ID different????
        # t2 -          start ID:4512182432 VAL:0         
        self.increment_using_global_counter()
        print(f"t3 - global counter ID:{id(counter)} VAL:{counter}")
        print(f"t3 - start ID:{id(start)} VAL:{start}")
        # t3 - global counter ID:4512182464 VAL:1                           << global counter ID different???? TODO
        # t3 -          start ID:4512182432 VAL:0
        self.assertEqual(True, counter == start + 1)

    # ------------------------------------------------------------------

    def local_access(self):
        stuff = 'eels'
        def from_the_league():
            stuff = 'this is a local shop for local people'
            return stuff
        
        return from_the_league() # ret stuff = 'this is a local shop for local people'

    def nonlocal_access(self):
        stuff = 'eels'
        def from_the_boosh():
            nonlocal stuff              # << whats going on here TODO
            #print(type(nonlocal))
            print(stuff)
            return stuff
        
        return from_the_boosh()

    def test_getting_something_locally(self):
        self.assertEqual('this is a local shop for local people', self.local_access())

    def test_getting_something_nonlocally(self):
        self.assertEqual('eels', self.nonlocal_access())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(42, deadly_bingo[5])
