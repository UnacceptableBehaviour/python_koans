#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"          # get outa here double underscore's a variable = duh!

class ___(Exception):               # tripple underscore's a class inheriting from Exception
    pass

____ = "-=> TRUE OR FALSE? <=-"     # quad underscore - hint

_____ = 0                           # quit underscore is zero!


class Koan(unittest.TestCase):
    pass
