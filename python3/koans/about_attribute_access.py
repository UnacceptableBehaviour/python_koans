#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMessagePassing in the Ruby Koans
#

from runner.koan import *

class AboutAttributeAccess(Koan):

    class TypicalObject:
        pass

    def test_calling_undefined_functions_normally_results_in_errors(self):
        typical = self.TypicalObject()

        with self.assertRaises(AttributeError): typical.foobar()

    def test_calling_getattribute_causes_an_attribute_error(self):
        typical = self.TypicalObject()

        with self.assertRaises(AttributeError): typical.__getattribute__('foobar')

        # THINK ABOUT IT:
        #
        # If the method __getattribute__() causes the AttributeError, then
        # what would happen if we redefine __getattribute__()?

    # ------------------------------------------------------------------

    class CatchAllAttributeReads:
        def __getattribute__(self, attr_name):
            return "Someone called '" + attr_name + "' and it could not be found"

    def test_all_attribute_reads_are_caught(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobar, "Someone called 'foobar' and it could not be found")

    def test_intercepting_return_values_can_disrupt_the_call_chain(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobaz, "'foobaz' and it could not be found") # This is fine
                        #   ^ = getattr(catcher, 'foobaz')
        try:
            catcher.foobaz(1)               # retrieve attribute (method) w parameter
        except TypeError as ex:             # include trace 
            err_msg = ex.args[0]
            print("catcher.foobaz(1)")      # find me in shell
            print(ex)
            print(len(ex.args))
            print(self.CatchAllAttributeReads.mro())
            

        self.assertRegex(err_msg, "'str' object is not callable")

        # foobaz returns a string. What happens to the '(1)' part?
        # Try entering this into a python console to reproduce the issue:
        #
        #     "foobaz"(1)
        #        ^     ^
        #       str    call with arg=1
        #
        # >>> "foobaz"(1)
        # TypeError: 'str' object is not callable
        # "Someone called '" + 'foobaz'(1) + "' and it could not be found"

    def test_changes_to_the_getattribute_implementation_affects_getattr_function(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(getattr(catcher, 'any_attribute'), "Someone called 'any_attribute' and it could not be found")
        # __im_usually_a_private_hook__  < double underscore
        # usually reseved for hooks - and implementation - also private
        # built in getattr() will use the hook and therefore its behaviour is changed

    # ------------------------------------------------------------------

    class WellBehavedFooCatcher:
        def __getattribute__(self, attr_name):
            # >>> 'foo_bar'[:3]
            # 'foo'
            # >>> 'foo_bar'[:6]
            # 'foo_ba'
            # >>> 'foo_bar'[3:6]
            # '_ba'
            if attr_name[:3] == "foo":
                return "Foo to you too"
            else:
                return super().__getattribute__(attr_name)
                # See if base class has attribute
                # stop infinite recursion?
                # https://docs.python.org/3/reference/datamodel.html#object.__getattribute__
                # ? - see class RecursiveCatcher: 2 down

    def test_foo_attributes_are_caught(self):
        catcher = self.WellBehavedFooCatcher()

        self.assertEqual('Foo to you too', catcher.foo_bar)
        with self.assertRaises(AttributeError): catcher.doo_baz
        self.assertEqual('Foo to you too', catcher.foo_baz)

    def test_non_foo_messages_are_treated_normally(self):
        catcher = self.WellBehavedFooCatcher()

        with self.assertRaises(AttributeError): catcher.normal_undefined_attribute

    # ------------------------------------------------------------------

    global stack_depth                  # __main__.global
    #print(type(stack_depth))           # NameError: name 'stack_depth' is not defined
    
    stack_depth = 0
    
    print("stack_depth")
    print(type(stack_depth))            # <class 'int'>
    print(type(stack_depth).mro())      # [<class 'int'>, <class 'object'>]

    class RecursiveCatcher:
        def __init__(self):
            global stack_depth          # use global
            
            print("RecursiveCatcher: stack_depth")
            print(type(stack_depth))        # <class 'int'>
            print(type(stack_depth).mro())  # [<class 'int'>, <class 'object'>]
            
            stack_depth = 0             # using global - reset stack depth on ctor
            self.no_of_getattribute_calls = 0

        def __getattribute__(self, attr_name):
            # We need something that is outside the scope of this class:
            global stack_depth
            stack_depth += 1

            if stack_depth<=10: # to prevent a stack overflow
                self.no_of_getattribute_calls += 1
                # Oops! We just accessed an attribute (no_of_getattribute_calls)
                # Guess what happens when self.no_of_getattribute_calls is
                # accessed?

            # Using 'object' directly because using super() here will also
            # trigger a __getattribute__() call.
            return object.__getattribute__(self, attr_name)

        def my_method(self):
            pass

    def test_getattribute_is_a_bit_overzealous_sometimes(self):
        catcher = self.RecursiveCatcher()
        catcher.my_method()
        global stack_depth
        self.assertEqual(11, stack_depth)
        c2 = self.RecursiveCatcher()
        peek = c2.no_of_getattribute_calls
        self.assertEqual(11,stack_depth)
        self.assertEqual(10,peek)

    # ------------------------------------------------------------------

    class MinimalCatcher:
        class DuffObject: pass

        def __init__(self):
            self.no_of_getattr_calls = 0        # object var

        # https://docs.python.org/3/reference/datamodel.html#object.__getattr__
        def __getattr__(self, attr_name):   # called when AttributeError error
                                            # is raised from
                                            # __get__           descriptor (and @property)
                                            # or
                                            # __getattribute__  attribute

            self.no_of_getattr_calls += 1   # inc object var
                                            # object.__getattribute__(self, name)
            return self.DuffObject          # return class object DuffObject

        def my_method(self):
            print("CALLED my_method", self) # CALLED my_method <koans.about_attribute_access.AboutAttributeAccess.MinimalCatcher object at 0x10e05e198>
            pass

    def test_getattr_ignores_known_attributes(self):
        catcher = self.MinimalCatcher()     # create MinimalCatcher object
                                            # self.no_of_getattr_calls = 0
        catcher.my_method()                 # object.__getattribute__(self, name)
                                            # no exceptions __getattr__ NOT CALLED

        self.assertEqual(0, catcher.no_of_getattr_calls)

    def test_getattr_only_catches_unknown_attributes(self):
        catcher = self.MinimalCatcher()     # create MinimalCatcher object
        catcher.purple_flamingos()          # object.__getattribute__(self, purple_flamingos)
                                            # raise AttributeError > inc self.no_of_getattr_calls to 1
        catcher.free_pie()                  # object.__getattribute__(self, free_pie) 
                                            # raise AttributeError > inc self.no_of_getattr_calls to 2
                                            # no exceptions __getattr__ NOT CALLED
        self.assertEqual('DuffObject',      # same as last two, class object DuffObject returned
                                            # raise AttributeError > inc self.no_of_getattr_calls to 3
            type(catcher.give_me_duff_or_give_me_death()).__name__)

        self.assertEqual(3, catcher.no_of_getattr_calls)

    # ------------------------------------------------------------------

    # >>> long_name = '01234567889abcdefgh'
    # >>> len(long_name)
    # 19

    # >>> long_name[-2:]
    # 'gh'
    # >>> long_name[-1:]
    # 'h'
    # >>> long_name[:-1]
    # '01234567889abcdefg'
    # >>> long_name[-2:-1]
    # 'g'
    # >>> long_name[-2:2]             # WARNING doesn't wrap! :/ - expected 'gh01'
    # ''
    # >>> long_name[2:-1]
    # '234567889abcdefg'
    # >>> long_name[2:17]
    # '234567889abcdef'
    # >>> long_name[:17]
    # '01234567889abcdef'

    # note there is no __setattribute__
    class PossessiveSetter(object):
        
        #https://docs.python.org/3/reference/datamodel.html#object.__setattr__
        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[-5:] == 'comic':
                new_attr_name = "my_" + new_attr_name       # change name
            elif attr_name[-3:] == 'pie':
                new_attr_name = "a_" + new_attr_name        # change name

            object.__setattr__(self, new_attr_name, value)  # allocate attribute with new name
                                                            # in th base class object

    def test_setattr_intercepts_attribute_assignments(self):
        fanboy = self.PossessiveSetter()
        print(dir(fanboy))
        # ['__class__', . .  '__weakref__']                     # untouched class
        
        fanboy.comic = 'The Laminator, issue #1'
        print(dir(fanboy))
        #print(fanboy.comic)                                    # AttributeError: 'PossessiveSetter' object has no attribute 'comic'
        print(fanboy.my_comic)                                  # The Laminator, issue #1
        # ['__class__', . .  '__weakref__', 'my_comic']         # my_comic added
        
        fanboy.pie = 'blueberry'
        print(dir(fanboy))
        # ['__class__', . .  '__weakref__', 'a_pie', 'my_comic'] # a_pie added

        self.assertEqual('blueberry', fanboy.a_pie)

        #
        # NOTE: Change the prefix to make this next assert pass
        #

        prefix = 'my'
        self.assertEqual("The Laminator, issue #1", getattr(fanboy, prefix + '_comic'))
        #
        # getattr(x, 'foobar') is equivalent to x.foobar.
        # https://docs.python.org/3/library/functions.html#getattr
        #
        # print(f"fanboy.my_comic {fanboy.my_comic} - {getattr(fanboy, 'my_comic')}")
        # fanboy.my_comic The Laminator, issue #1 - The Laminator, issue #1

    # ------------------------------------------------------------------

    class ScarySetter:
        def __init__(self):
            self.num_of_coconuts = 9
            self._num_of_private_coconuts = 2

        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[0] != '_':                             # check  for private attribute
                new_attr_name = "altered_" + new_attr_name      # preceed public attribute names w/ altered

            object.__setattr__(self, new_attr_name, value)      # create new attribute in base object

    def test_it_modifies_external_attribute_as_expected(self):
        setter = self.ScarySetter()                             # create ScarySetter object
        setter.e = "mc hammer"                                  # object.__setattr__(self, attr_name, value)
                                                                # no _ at begining of name
                                                                # create attribute in object base class 'altered_e'
        self.assertEqual("mc hammer", setter.altered_e)

    def test_it_mangles_some_internal_attributes(self):
        setter = self.ScarySetter()
        # print('ScarySetter: dir(setter)')
        # print(dir(setter))
        # ScarySetter: dir(setter)
        # [ . .  '_num_of_private_coconuts', 'altered_num_of_coconuts']     # < num_of_coconuts changed in __init__

        try:
            coconuts = setter.num_of_coconuts   # < num_of_coconuts changed in __init__ to  altered_num_of_coconuts
            # print('try: dir(setter)')         # doesn't run 
            # print(dir(setter))
            
        except AttributeError:
            # print('except: dir(setter)')
            # print(dir(setter))
            # except: dir(setter)
            # [ . . '_num_of_private_coconuts', 'altered_num_of_coconuts']
            self.assertEqual(9, setter.altered_num_of_coconuts)

    def test_in_this_case_private_attributes_remain_unmangled(self):
        setter = self.ScarySetter()

        self.assertEqual(2, setter._num_of_private_coconuts)



    # TODO good overview of how it hangs together
    # access process
    # https://stackoverflow.com/questions/14787334/confused-with-getattribute-and-setattribute-in-python
