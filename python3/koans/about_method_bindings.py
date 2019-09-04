#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# def function(): return "pineapple"
def function():
    return "pineapple"

def function2():
    return "tractor"

class Class:
    def method(self):
        return "parrot"             # eaten by python! its dead now . .
    
    def turkey(self):
        return(self)
    
    @staticmethod        
    def croissant():
        return(self)        # thought this would return instance of class object Class . but. .
                            # Class.croissant() > NameError: name 'self' is not defined

class AboutMethodBindings(Koan):
    def test_methods_are_bound_to_an_object(self):
        obj = Class()
        obj2 = Class()
        
        self.assertEqual(True, obj.method.__self__ == obj)
        # >>> obj = Class()
        # >>> obj
        # <__main__.Class object at 0x10a5410f0>
        # >>> obj.method.__self__
        # <__main__.Class object at 0x10a5410f0>
        # >>> hex(id(obj))
        # '0x10a5410f0'
        # >>> obj.__self__                          # NO make sense since obj is __self__
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # AttributeError: 'Class' object has no attribute '__self__'        <<< ??? TODO
                                                                                      #
        # >>> Class                                                                  <<
        # <class '__main__.Class'>
        # >>> Class.__self__
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # AttributeError: type object 'Class' has no attribute '__self__'


        #self.assertEqual(True, obj.__self__ == obj)    # AttributeError: 'Class' object has no attribute '__self__'

        

    def test_methods_are_also_bound_to_a_function(self):
        obj = Class()
        self.assertEqual("parrot", obj.method())
        self.assertEqual(obj.method.__func__.__name__, 'method')
        self.assertEqual(obj.method.__func__(obj), obj.method())    # call func on obj    
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
        obj = Class()                                   # way around the above restriction
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
    # Descriptor How To Guide
    # https://docs.python.org/3.7/howto/descriptor.html
    # Quickly:
    # In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has
    # been overridden by methods in the descriptor protocol. Those methods are __get__(), __set__(), and
    # __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.
    # 
    # The default behavior for attribute access is to get, set, or delete the attribute from an object’s
    # dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], then
    # type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.
    # If the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined.
    # 
    # Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods,
    # static methods, class methods, and super(). They are used throughout Python itself to implement the new
    # style classes introduced in version 2.2. Descriptors simplify the underlying C-code and offer a flexible
    # set of new tools for everyday Python programs.
        
    class BoundClass:
        def __get__(self, obj, cls):
            print(f"BoundClass.__get__ \n\tOBJ: {obj}\n\tCLS:  {cls}")
            return (self, obj, cls)
    
    # inside AboutMethodBindings
    binding = BoundClass()          # < accessed w/ self.binding # within class AboutMethodBindings
                                    

    def test_get_descriptor_resolves_attribute_binding(self):
        print("---S")
        print(f"test_get_descriptor_resolves_attribute_binding {self.__class__.__name__}")
        print("-A")
        print(f"test_get_descriptor_resolves_attribute_binding {self.binding.__class__.__name__}")
        print("-B")
        print(f"test_get_descriptor_resolves_attribute_binding {self.binding}")
        print("---E")
                # ---
                # test_get_descriptor_resolves_attribute_binding AboutMethodBindings
                # -
                # BoundClass.__get__ <class 'koans.about_method_bindings.AboutMethodBindings'>
                # test_get_descriptor_resolves_attribute_binding tuple
                # -
                # BoundClass.__get__ <class 'koans.about_method_bindings.AboutMethodBindings'>
                # test_get_descriptor_resolves_attribute_binding
# bound_ob      #      (<koans.about_method_bindings.AboutMethodBindings.BoundClass object at 0x10f2d7dd8>,
# binding_owner #       <koans.about_method_bindings.AboutMethodBindings testMethod=test_get_descriptor_resolves_attribute_binding>,
# owner_type    #       <class 'koans.about_method_bindings.AboutMethodBindings'>)
                # ---
                # BoundClass.__get__ <class 'koans.about_method_bindings.AboutMethodBindings'>        
        
        
        # self > AboutMethodBindings
        # self.binding > tuple        
        bound_obj, binding_owner, owner_type = self.binding # return a tuple (immutable list)
                                                            # assigns it to each item on the left
        
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls
                                                                        #   name => it's a string not a type!
        self.assertEqual("BoundClass", bound_obj.__class__.__name__)    #  /
        self.assertEqual('AboutMethodBindings', binding_owner.__class__.__name__) # <koans.about_method_bindings.AboutMethodBindings testMethod=test_get_descriptor_resolves_attribute_binding>
        self.assertEqual(AboutMethodBindings, owner_type) # <class 'koans.about_method_bindings.AboutMethodBindings'>

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
        self.assertEqual('purple', self.color.choice)





# Experiments:
# >>> Class
# <class '__main__.Class'>
# >>> Class.__self__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'Class' has no attribute '__self__'
# 
# >>> id(Class)
# 140409156202520
# >>> type(Class)
# <class 'type'>
# >>> 
# 
# >>> dir
# <built-in function dir>
# >>> dir()
# ['BoundClass', 'Class', 'MySpecialError', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'binding', 'c', 'cc', 'comprehension', 'count_of_three', 'd', 'decimal_places', 'e', 'empty_method', 'f', 'feast', 'foff', 'function', 'highlanders', 'i', 'is_even', 'list_of_eggs', 'list_of_meats', 'm', 'math', 'method_with_var_args', 'my_global_function', 'obj', 'one', 'p', 'pprint', 'random', 's', 'scotsmen', 'seq', 'string', 't', 'warriors']
# 
# >>> [type(x) for x in dir()] 
# [<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>]
# 
# >>> dir(140409156202520)    # this is same as dir(int)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# >>> dir(Class)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'method']
# >>> dir(int)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


