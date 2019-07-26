#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutSandwichCode in the Ruby Koans
#

from runner.koan import *

import re # For regular expression string comparisons

class AboutWithStatements(Koan):
    def count_lines(self, file_name):
        try:
            file = open(file_name)
            try:
                return len(file.readlines())
            finally:
                file.close()
        except IOError:
            # should never happen
            self.fail()

    def test_counting_lines(self):
        self.assertEqual(4, self.count_lines("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line(self, file_name):
        try:
            file = open(file_name)
            try:
                for line in file.readlines():
                    match = re.search('e', line)
                    if match:
                        return line
            finally:
                file.close()
        except IOError:
            # should never happen
            self.fail()

    def test_finding_lines(self):
        self.assertEqual("test\n", self.find_line("example_file.txt"))

    ## ------------------------------------------------------------------
    ## THINK ABOUT IT:
    ##
    ## The count_lines and find_line are similar, and yet different.
    ## They both follow the pattern of "sandwich code".
    ##
    ## Sandwich code is code that comes in three parts: (1) the top slice
    ## of bread, (2) the meat, and (3) the bottom slice of bread.
    ## The bread part of the sandwich almost always goes together, but
    ## the meat part changes all the time.
    ##
    ## Because the changing part of the sandwich code is in the middle,
    ## abstracting the top and bottom bread slices to a library can be
    ## difficult in many languages.
    ##
    ## (Aside for C++ programmers: The idiom of capturing allocated - TODO
    ## pointers in a smart pointer constructor is an attempt to deal with
    ## the problem of sandwich code for resource allocation.) 
    ##
    ## Python solves the problem using Context Managers. Consider the
    ## following code:
    ##

    class FileContextManager():
        def __init__(self, file_name):              # contructor
            print("FileContextManager: __init__")
            self._file_name = file_name
            self._file = None
            

        def __enter__(self):                        # entry hook
            print("FileContextManager: __enter__")
            self._file = open(self._file_name)            
            return self._file

                    # these are for tracing back an exit due to an exception
                    # they are None on a successful exit
        def __exit__(self, cls, value, tb):         # destructor / exit hook
            print("FileContextManager: __exit__")
            self._file.close()
            # what do we need any values passed in? part of __exit__ function signature?
            # self,  object instance        # part of every function in a aclass - except static?
            # cls,   exception type
            # value, exception value
            # tb     traceback
    # TODO - Context Manager Protocol - Ex
    # https://alysivji.github.io/managing-resources-with-context-managers-pythonic.html

    # Now we write:

    def count_lines2(self, file_name):
        with self.FileContextManager(file_name) as file:
            # __init__
            #   __enter__
            #   __exit__
            return len(file.readlines())

    def test_counting_lines2(self):
        self.assertEqual(4, self.count_lines2("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line2(self, file_name):
        # Using the context manager self.FileContextManager, rewrite this
        # function to return the first line containing the letter 'e'.
        with self.FileContextManager(file_name) as file:
            for line in file.readlines():
                match = re.search('e', line)
                if match:
                    return line    
        return None

    def test_finding_lines2(self):
        self.assertNotEqual(None, self.find_line2("example_file.txt"))
        self.assertEqual('test\n', self.find_line2("example_file.txt"))

    # ------------------------------------------------------------------

    def count_lines3(self, file_name):
        with open(file_name) as file:
            return len(file.readlines())

    def test_open_already_has_its_own_built_in_context_manager(self):
        self.assertEqual(4, self.count_lines3("example_file.txt"))
