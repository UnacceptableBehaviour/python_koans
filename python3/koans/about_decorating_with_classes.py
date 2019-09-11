#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

import functools

class AboutDecoratingWithClasses(Koan):
    def maximum(self, a, b):
        if a>b:
            return a
        else:
            return b

    def test_partial_that_wrappers_no_args(self):
        """
        Before we can understand this type of decorator we need to consider
        the partial.
        """
        max = functools.partial(self.maximum)

        self.assertEqual(23, max(7,23))
        self.assertEqual(10, max(10,-10))

    def test_partial_that_wrappers_first_arg(self):
        max0 = functools.partial(self.maximum, 0)
        # 0 passed as left most argument to, self.maximum( 0, arg_from_max0 )

        self.assertEqual(0, max0(-4))
        self.assertEqual(5, max0(5))

    def test_partial_that_wrappers_all_args(self):
        always99 = functools.partial(self.maximum, 99, 20)
        # 99 passed as left most argument then 20 as next arg to, self.maximum( 99, 20 )
        # pointless - example use?
        
        always20 = functools.partial(self.maximum, 9, 20)
        # as above

        self.assertEqual(99, always99())
        self.assertEqual(20, always20())

    # ------------------------------------------------------------------

    class doubleit:
        def __init__(self, fn):
            self.fn = fn                                        # store decorated function

        def __call__(self, *args):                              # on call func()
            return self.fn(*args) + ', ' + self.fn(*args)       # call it twice rurn w/ a comma separator

        def __get__(self, obj, cls=None):                       
            if not obj:
                # Decorating an unbound function - IE doesn't belong to a class
                print(f"Decorating an unbound function - IE doesn't belong to a class > {self.fn.__name__} < {self.fn}")
                return self
            else:
                # Decorating a bound method  - runs on access or call to foo - self.foo self.foo()
                print(f"Decorating a bound method > {self.fn.__name__} < {self.fn}")
                return functools.partial(self, obj)



    print(dir())
    print(f"decorating w class doubleit - STEP1 >> {doubleit} <<")    
    # ['__module__', '__qualname__', 'doubleit', 'maximum', 'test_partial_that_wrappers_all_args', 'test_partial_that_wrappers_first_arg', 'test_partial_that_wrappers_no_args']
    # decorating w class doubleit - STEP1 >> <class 'koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit'> <<

    #print(f"decorating w class doubleit - STEP1 >> {doubleit.fn} <<")  # AttributeError: type object 'doubleit' has no attribute 'fn'



    @doubleit
    def foo(self):              # AboutDecoratingWithClasses.foo
        return "foo"

    print(dir())
    # ['__module__', '__qualname__', 'doubleit', 'foo', 'maximum', 'test_partial_that_wrappers_all_args', 'test_partial_that_wrappers_first_arg', 'test_partial_that_wrappers_no_args']
    #                                              ^^
    
    print(f"decorating w class doubleit - STEP2 foo >> {foo} <<")    
    print(f"decorating w class doubleit - STEP2 foo.fn >> {foo.fn} <<")
    # decorating w class doubleit - STEP2 foo >> <koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x108749898> <<
    #                                                                                                                       ^^
    # decorating w class doubleit - STEP2 foo.fn >> <function AboutDecoratingWithClasses.foo at 0x108752598> <<
    #                                                   ^^


    @doubleit
    def parrot(self, text):
        return text.upper()

    print(dir())
    # ['__module__', '__qualname__', 'doubleit', 'foo', 'maximum', 'parrot', 'test_partial_that_wrappers_all_args', 'test_partial_that_wrappers_first_arg', 'test_partial_that_wrappers_no_args']
    #                                                                 ^^
    
    print(f"decorating w class doubleit - STEP3 parrot >> {parrot} <<")    
    print(f"decorating w class doubleit - STEP3 parrot.fn >> {parrot.fn} <<")
    # decorating w class doubleit - STEP3 parrot >> <koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x1087498d0> <<
    #                                                                                                                         ^^
    # decorating w class doubleit - STEP3 parrot.fn >> <function AboutDecoratingWithClasses.parrot at 0x1087527b8> <<    
    #                                                     ^^

    def test_decorator_with_no_arguments(self):
        # To clarify: the decorator above the function has no arguments, even
        # if the decorated function does
        print("= = = > test_decorator_with_no_arguments - - - - S")
        print(dir())
        print(f"decorating w class doubleit>> {AboutDecoratingWithClasses.foo} <<")
            # <koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x106149fd0>
        print(f"decorating w class doubleit self.foo >> {self.foo} <<")
            # functools.partial(<koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x1032fc828>, <koans.about_decorating_with_classes.AboutDecoratingWithClasses testMethod=test_decorator_with_no_arguments>) <<
        self.foo        # causes output: Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x107dd7598>
        self.foo        # causes output: Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x107dd7598>
        self.foo()      # causes output: Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x107dd7598>
        self.foo()      # causes output: Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x107dd7598>

        # Thinking AboutDecoratingWithClasses
        # = = = > test_decorator_with_no_arguments - - - - S
        # ['self']
        # Decorating an unbound function - IE doesn't belong to a class > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # decorating w class doubleit>> <koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x1093d1860> <<
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # decorating w class doubleit self.foo >> functools.partial(<koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x1093d1860>, <koans.about_decorating_with_classes.AboutDecoratingWithClasses testMethod=test_decorator_with_no_arguments>) <<
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # Decorating a bound method > foo < <function AboutDecoratingWithClasses.foo at 0x1093da598>
        # Decorating a bound method > parrot < <function AboutDecoratingWithClasses.parrot at 0x1093da7b8>
        # = = = > test_decorator_with_no_arguments - - - - E

        self.assertEqual('foo, foo', self.foo())
        self.assertEqual('PIECES OF EIGHT, PIECES OF EIGHT', self.parrot('pieces of eight'))
        
        print("= = = > test_decorator_with_no_arguments - - - - E")

    # ------------------------------------------------------------------

    def sound_check(self):
        #Note: no decorator
        return "Testing..."

    def test_what_a_decorator_is_doing_to_a_function(self):
        #wrap the function with the decorator
        print(f"PRE wrap - {self.sound_check}")
        self.sound_check = self.doubleit(self.sound_check)  # see scratch_pad_4_descriptors_vs_decorators.py - ln 112
        print(f"POST wrap - {self.sound_check}")
        # PRE wrap - <bound method AboutDecoratingWithClasses.sound_check of <koans.about_decorating_with_classes.AboutDecoratingWithClasses testMethod=test_what_a_decorator_is_doing_to_a_function>>
        # POST wrap - <koans.about_decorating_with_classes.AboutDecoratingWithClasses.doubleit object at 0x10c67b160>
        
        self.assertEqual('Testing..., Testing...', self.sound_check())

    # ------------------------------------------------------------------

    class documenter:
        def __init__(self, *args):
            self.fn_doc = args[0]

        def __call__(self, fn):
            def decorated_function(*args):          # the decorated function definintion
                return fn(*args)

            if fn.__doc__:                          # check to see if already had docs
                decorated_function.__doc__ = fn.__doc__ + ": " + self.fn_doc    # YES - Add docs passed into decorator
            else:
                decorated_function.__doc__ = self.fn_doc                        # NO - Use docs passed into decorator
                
            return decorated_function               # return the decorated function definintion with added docs

    @documenter("Increments a value by one. Kind of.")  # args[0]
    def count_badly(self, num):
        #"Sucks thumb"      # ahead of myself tested with idler!!
        num += 1
        if num==3:
            return 5
        else:
            return num
        
    @documenter("Does nothing")
    def idler(self, num):
        "Idler"
        pass

    def test_decorator_with_an_argument(self):
        self.assertEqual(5, self.count_badly(2))
        #self.assertEqual("Sucks thumb: Increments a value by one. Kind of.", self.count_badly.__doc__)        
        self.assertEqual("Increments a value by one. Kind of.", self.count_badly.__doc__)

    def test_documentor_which_already_has_a_docstring(self):
        self.assertEqual("Idler: Does nothing", self.idler.__doc__)

    # ------------------------------------------------------------------

    @documenter("DOH!")
    @doubleit
    @doubleit
    def homer(self):
        return "D'oh"

    def test_we_can_chain_decorators(self):
        self.assertEqual("D'oh, D'oh, D'oh, D'oh", self.homer())
        self.assertEqual("DOH!", self.homer.__doc__)

