#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(True, isinstance(None, object))
        # isinstance(obeject under test, class)

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(True, None is None)
        # is - check id same object IE allocated same place in memory
        # == - ar they the same type and value

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        # I believe the above notation is part of the autmated documentation
        # ``` documentation ``` just insude the method declaration
        try:            
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     http://bit.ly/__class__

        self.assertEqual(AttributeError, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        print("ex2 & args[0]")
        print(ex2)
        print(ex2.args[0])
        print(len(ex2.args))
        self.assertRegex(ex2.args[0], 'some_method_none_does_not_know_about')
        # assertRegex(s, r)                 - check r.search(s)
        # match (string, pattern)             pattern.search(string)

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(True, None is not 0)
        self.assertEqual(True, None is not False)
