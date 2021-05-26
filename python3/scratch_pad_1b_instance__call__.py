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




# How to reference variables in different namespaces / scopes
# https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example
# https://stackoverflow.com/questions/2010692/what-does-mro-do
# -
class SuperColor:
    base_choice = False                             # find with dir(SuperColor)

    def __init__(self):
        print(f"ctor: {self}")
        self.choice = 'yella' # by default

    def __set__(self, obj, val):                   # comment in
        self.choice = val

color = SuperColor()                                # create an instance of SuperColor
#color = 'purple'                                    # what is this being assigned to?
                                                    # overwrite with a string 'purple'
                                                    # leads to AttributeError: 'str' object has no attribute 'choice'
                                                    # TODO why does this work in about_method_bindings (last test)
                                                    # and not here?

print("\n\n== SuperColor ==")
print(SuperColor)
print("\n\n== SuperColor.mro()")
print(SuperColor.mro())
print("\n\n== dir(SuperColor)")
print(dir(SuperColor))
print("\n\n== dir(color)")
print(dir(color))
print(id(color))
print(type(color))
print(color)
# == SuperColor ==
# <class '__main__.SuperColor'>
#
# == SuperColor.mro()
# [<class '__main__.SuperColor'>, <class 'object'>]
#
# == dir(SuperColor)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'base_choice']   << base_choice ******
#
# == dir(color)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'base_choice', 'choice']   << choice  *******
# 4460028592
# <class '__main__.SuperColor'>
# <__main__.SuperColor object at 0x109d6a2b0>
# yella

print(color)
print(color.choice)


class Color(SuperColor):
    def __init__(self, c):
        super()






# https://stackoverflow.com/questions/5824881/python-call-special-method-practical-example

print('\n\n> - - - - - - - - memoization example using __call__  - - \\ ')

class Factorial:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]

fact = Factorial()

for i in range(10):
    print(f"{i}! = {fact(i)}")


print('\n\n> - - - - - - - - library wrapper example using __call__  - - \\ ')
import hashlib
# file: filehash.py
class Hasher(object):
    """
    A wrapper around the hashlib hash algorithms that allows an entire file to
    be hashed in a chunked manner.
    """
    def __init__(self, algorithm):
        self.algorithm = algorithm
        print(f"create Hasher {str(algorithm)}")

    def __call__(self, f_name):
        hash_alg = self.algorithm()
        c = 0
        with open(f_name, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), ''):    # < something wrong here ? goes for ever?
                c += 1
                print(c)
                if c > 5: break
                hash_alg.update(chunk)
        return hash_alg.hexdigest()

md5    = Hasher(hashlib.md5)
sha1   = Hasher(hashlib.sha1)
sha224 = Hasher(hashlib.sha224)
sha256 = Hasher(hashlib.sha256)
sha384 = Hasher(hashlib.sha384)
sha512 = Hasher(hashlib.sha512)

print(sha1('./data/sous_vide_shor-rib_red_pepper_shitake_SML.png'))



