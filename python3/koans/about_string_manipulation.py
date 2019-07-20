#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        # string = "The values are {0} and {1}".format(value1, value2)  # WORKS
        string = f"The values are {value1} and {value2}"                # also WORKS
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions
                                                                                        # nested substitution!
        # >>> "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),decimal_places)   # .nf limit decimal places to n
        # 'The square root of 5 is 2.2361'
        # >>> "The square root of 5 is {0}".format(math.sqrt(5),decimal_places)         # just square root
        # 'The square root of 5 is 2.23606797749979'
        # >>> "The square root of 5 is {1}f".format(math.sqrt(5),decimal_places)        # 
        # 'The square root of 5 is 4f'
        # >>> "The square root of 5 is {0:.2f}".format(math.sqrt(5),decimal_places)     # so 0:.2f is 0 to 2 dec places
        # 'The square root of 5 is 2.24'

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual('The square root of 5 is 2.2361', string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))                                  # unicode value - inverse chr()
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(["Sausage","Egg","Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')                             # , or ; compiled regex 

        words = pattern.split(string)

        self.assertListEqual(["the","rain","in","spain"], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'       # ah yes look!

    def test_raw_strings_do_not_interpret_escape_characters(self):
    # >>> len(string)                               # string is not a type it's str
    # NameError: name 'string' is not defined
    # >>> len(type(string))
    # NameError: name 'string' is not defined
    # >>> len(type('\n'))
    # TypeError: object of type 'type' has no len()
    # >>> '\n'
    # '\n'
    # >>> type('\n')
    # <class 'str'>
    # >>> string = r'\n'
    # >>> type(string)
    # <class 'str'>
    # >>> len(str)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: object of type 'type' has no len()        
    # >>> string
    # '\\n'                 
                                                    # r'' or r"" denotes string literal - not a regex
                                                    # r'this is interpreted literally'
        string = r'\n'                              # this is not a regex this is a string of type str
        #pattern = re.compile(',|;')                # need to  import re  for this but not  string = r'\n'
        self.assertNotEqual('\n', string) 
        self.assertEqual(type('\n'), str)
        self.assertNotEqual(type('\n'), string)
        self.assertEqual("\\n", string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
