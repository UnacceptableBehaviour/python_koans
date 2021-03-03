#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# the journey to enlightenment starts with a single step . . 
#
# and lots of head scratching and tests!
#

from pprint import pprint 


class TopDog:
    "removes barriers"
    self._private_by_agreement = "secret orders"
    self.__private_still_accessible_through_magled_name = "more secret but not that secure"
    
    def __init__(self, new_orders):
      self._orders = "mentore organisation"
  
    class SubDog:
        "does as commanded"

        def __init__(self):    
            d = self.SubDog()
        
            print(d.__class__)
            print(d.__class__.__name__)
    

#dog = SubDog()               # NameError: name 'SubDog' is not defined
dog = TopDog.SubDog()

print(dog.__class__.__name__)

print(type(dog))

#print(dog.mro())             # AttributeError: 'SubDog' object has no attribute 'mro'
print(dog.__class__.mro())    # [<class '__main__.TopDog.SubDog'>, <class 'object'>]