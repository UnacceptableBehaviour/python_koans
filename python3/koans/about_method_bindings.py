#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# def function(): return "pineapple"
def function():
    return "pineapple"

def function2():
    return "tractor"

# class Class: def method(self): return "parrot"
class Class:
    def method(self):
        return "parrot"             # eaten by python! its dead now . . 

class AboutMethodBindings(Koan):
    def test_methods_are_bound_to_an_object(self):
        obj = Class()
        self.assertEqual(True, obj.method.__self__ == obj)

    def test_methods_are_also_bound_to_a_function(self):
        obj = Class()
        self.assertEqual("parrot", obj.method())
        self.assertEqual(obj.method.__func__.__name__, 'method')
        self.assertEqual(obj.method.__func__(obj), obj.method())        
        self.assertEqual(obj.method.__func__(obj), "parrot")
        # https://docs.python.org/3/reference/datamodel.html instance methods

    def test_functions_have_attributes(self):
        obj = Class()
        self.assertEqual(35, len(dir(function)))
        self.assertEqual(len(dir(obj.method.__func__)), len(dir(function)))

        # https://docs.python.org/3/library/functions.html#dir
        # dir([object])
        # Without arguments, return the list of names in the current local scope. With an argument,
        # attempt to return a list of valid attributes for that object.
        # 
        # If the object has a method named __dir__(), this method will be called and must return
        # the list of attributes. This allows objects that implement a custom __getattr__() or
        # __getattribute__() function to customize the way dir() reports their attributes.
        
        
        # TODO - ex - context where this is useful
        self.assertEqual(True, dir(function) == dir(obj.method.__func__))
        # >>> def function(): return "pineapple"
        # ... 
        # >>> class Class:
        # ...     def method(self):
        # ...         return "parrot"             # eaten by python! its dead now . . 
        # ... 
        # >>> dir(function)
        # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        # >>> 
        # >>> obj = Class()
        # >>> 
        # >>> dir(obj.method.__func__)
        # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        # >>>
        # >>> 
        # >>> id(obj.method.__func__)
        # 4468264744
        # >>> id(function)
        # 4468153608
        # >>>
        # Either this is saying that these both have function class context or I'm missing the point
        # >>>
        # >>> function.__class__.mro()
        # [<class 'function'>, <class 'object'>]
        # >>>
        # >>> obj.method.__func__.__class__.mro()
        # [<class 'function'>, <class 'object'>]
        # >>>        
        
    # TODO - revisit
    def test_methods_have_different_attributes(self):
        obj = Class()
        self.assertEqual(27, len(dir(obj.method)))
        # >>> dir(dir(obj.method))
        # len=46 ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
        # >>> len(dir([]))
        # 46

        # >>> dir(obj.method)
        # len=27 ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

        # >>> dir(function)
        # len=35 ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        # >>>
                                    # UNBOUND FUNCTION                  <<<
    def test_setting_attributes_on_an_unbound_function(self):
        function.cherries = 3
        self.assertEqual(3, function.cherries)                          # < EH?
                                                                        #
    def test_setting_attributes_on_a_bound_method_directly(self):       #
        obj = Class()                                                   #
        with self.assertRaises(AttributeError): obj.method.cherries = 3 # < EH? because obj method?
                                                                        # YES BOUND TO OBJECT
    def test_setting_attributes_on_methods_by_accessing_the_inner_function(self):
        obj = Class()
        obj.method.__func__.cherries = 3                # TODO
        self.assertEqual(3, obj.method.cherries)        # example of why this is useful would be good here

    def test_functions_can_have_inner_functions(self):
        function2.get_fruit = function
        self.assertEqual("pineapple", function2.get_fruit())

    def test_inner_functions_are_unbound(self):
        function2.get_fruit = function
        with self.assertRaises(AttributeError): cls = function2.get_fruit.__self__

        foff = function2.__init__()          # OK
        # >>> function()
        # 'pineapple'
        # >>> foff = function.__init__()
        # >>> type(foff)
        # <class 'NoneType'>
        #self.assertEqual(foff.getfruit(),__) # AttributeError: 'NoneType' object has no attribute 'getfruit'

        #foff.get_fruit = function
        #self.assertEqual(foff.getfruit(),__) # AttributeError: 'NoneType' object has no attribute 'getfruit'
        #with self.assertRaises(AttributeError): cls = foff.get_fruit.__self__

    # ------------------------------------------------------------------

    # TODO TODO Go through these examples
    # https://docs.python.org/3.7/howto/descriptor.html 
    
    class BoundClass:
        def __get__(self, obj, cls):
            return (self, obj, cls)

    binding = BoundClass()

    def test_get_descriptor_resolves_attribute_binding(self):
        bound_obj, binding_owner, owner_type = self.binding
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls

        self.assertEqual("BoundClass", bound_obj.__class__.__name__)
        self.assertEqual(__, binding_owner.__class__.__name__)
        self.assertEqual(AboutMethodBindings, owner_type)

    # ------------------------------------------------------------------

    class SuperColor:
        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

    color = SuperColor()

    def test_set_descriptor_changes_behavior_of_attribute_assignment(self):
        self.assertEqual(None, self.color.choice)
        self.color = 'purple'
        self.assertEqual(__, self.color.choice)

