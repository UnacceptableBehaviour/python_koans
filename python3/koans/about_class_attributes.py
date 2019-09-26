#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutClassAttributes(Koan):
    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()                 # fido is an object of type Dog
                                          #       package?    module(filename)      class            class
        # print(fido.__class__)           # <class 'koans.about_class_attributes.AboutClassAttributes.Dog'>
        # print(fido.__class__.__name__)  # Dog

        #print(self.Dog.mro()) # show class hierarchy
        #[<class 'koans.about_class_attributes.AboutClassAttributes.Dog'>, <class 'object'>]
        self.assertEqual(True, isinstance(fido, object))

    def test_classes_are_types(self):       # self.Dog is a type (a class object)
        # print(self.Dog.__class__)           # <class 'type'>
        # print(self.Dog.__class__.__name__)  # type
        self.assertEqual(True, self.Dog.__class__ == type)

    def test_classes_are_objects_too(self):
        self.assertEqual(True, issubclass(self.Dog, object))

    def test_objects_have_methods(self):
        fido = self.Dog()
        print('dir(fido)')
        print(dir(fido)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
                         # '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
        # '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
        # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
        # '__subclasshook__', '__weakref__']
        print('fido.__dir__')
        print(fido.__dir__())
        self.assertEqual(26, len(dir(fido)))
        # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']        
        self.assertEqual(26, len(fido.__dir__())) # 26 but not the same 26! TODO
        # ['__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

    def test_classes_have_methods(self):
        self.assertEqual(26, len(dir(self.Dog)))

    def test_creating_objects_without_defining_a_class(self):
        singularity = object()
        print('dir(singularity)')
        print(dir(singularity))                      # attributes
        # fido:         ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
        # singularity:  ['__class__', '__delattr__',             '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',               '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        self.assertEqual(23, len(dir(singularity)))

    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4                                   # creates an attribute legs in the fido OBJECT ONLY
        #self.assertEqual(__, fido.__weakref__) # None
        self.assertEqual('koans.about_class_attributes', fido.__module__)
        self.assertEqual(4, fido.__dict__['legs'])
        self.assertEqual(4, fido.legs)

    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        # lambda function object -   lambda x: return(do something with x)
        #
        # def square_root(x): return math.sqrt(x)       # < using def
        #
        # square_root = lambda x: math.sqrt(x)          # < equivalent lambda        
        
        def bark():
            return 'bark, bark, bark . . WOOF!'

        fido.bark = bark        
        fido.wag = lambda : 'fidos wag'             # lambda x=null: return 'fidos wag'

        self.assertEqual('fidos wag', fido.wag())
        self.assertEqual('bark, bark, bark . . WOOF!', fido.bark())

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        rover = self.Dog()

        def wag():
            return 'fidos wag'
        fido.wag = wag                                         # singleton function 
                                                               # 
        with self.assertRaises(AttributeError): rover.wag()    # so rover wont do fidos wag!!
        # type(fido.wag) =>  <class 'function'>
        self.assertEqual('function',type(fido.wag).__name__)

    # ------------------------------------------------------------------

    class Dog2:
        def wag(self):
            return 'instance wag'

        def bark(self):
            return "instance bark"

        def growl(self):                    # whats the point of this if class method runs instead?#
            return "instance growl"                                                                #
                                                                                                   #
        @staticmethod                                                                              #
        def bark():                                                                                #
            return "staticmethod bark, arg: None"                                                  #
                                                                                                   #
        @classmethod                                                                               #
        def growl(cls):                                                                            #
            return "classmethod growl, arg: cls=" + cls.__name__                                   #
                                                                                                   #
    def test_since_classes_are_objects_you_can_define_singleton_methods_on_them_too(self):         #
        self.assertRegex(self.Dog2.growl(), "classmethod growl, arg: cls=Dog2")                    #
                                                                                                   #
    def test_classmethods_are_not_independent_of_instance_methods(self):                           #
        fido = self.Dog2()                                                                         #
        self.assertRegex(fido.growl(), "classmethod growl, arg: cls=Dog2")          # TODO why not "instance growl" ??
        self.assertRegex(self.Dog2.growl(), "classmethod growl, arg: cls=Dog2")                    #
                                                                                                   #
    def test_staticmethods_are_unbound_functions_housed_in_a_class(self):                          #
        self.assertRegex(self.Dog2.bark(), "staticmethod bark, arg: None")                         #
                                                                                                   #
    def test_staticmethods_also_overshadow_instance_methods(self):                                 #
        fido = self.Dog2()                                                                         #
        self.assertRegex(fido.bark(), "staticmethod bark, arg: None")    # unexpected behaviour - ?? NO "instance bark"

    # ------------------------------------------------------------------

    class Dog3:
        #_name = None                   # serves same function as init: self._name = None
                                        # issues with super()? TODO
        def __init__(self):
            self._name = None

        def get_name_from_instance(self):
            return self._name

        def set_name_from_instance(self, name):
            self._name = name

        @classmethod
        def get_name(cls):
            return cls._name

        @classmethod
        def set_name(cls, name):
            cls._name = name

        name = property(get_name, set_name)     # @classmethods         - creating a class property
        
                                                # instance methods      - creating a instance property
        name_from_instance = property(get_name_from_instance, set_name_from_instance)

    def test_classmethods_can_not_be_used_as_properties(self):
        fido = self.Dog3()                                      # no name passed in - no needed - init to None
        kali = self.Dog3()
        with self.assertRaises(TypeError): fido.name = "Fido"   # classmethod called on object - WRITE - NO
        self.Dog3.breed = "Retriever"                           # This creates an attribute 'breed' in the Dog3 class object
        self.assertEqual("Retriever", self.Dog3.breed)          # this retrieves it
        self.assertEqual("Retriever", kali.breed)  # Looks for attribute 'breed' in kali object, when not found goes to class level attribute
        kali.breed = 'Poodle'                                   # creates object level attribute, assigns 'Poodle'
        self.assertEqual("Retriever", self.Dog3.breed)          # class attribute remains 'Retriever'
        self.assertEqual('Poodle', kali.breed)                  # object level attribute remains 'Poodle' 
                                                                
                                                                                    #
    def test_classes_and_instances_do_not_share_instance_attributes(self):          #
        fido = self.Dog3()                                                          #
        fido.set_name_from_instance("Fido")                                         #
        fido.set_name("Rover")                                                      #
        self.assertEqual("Fido", fido.get_name_from_instance())                     #
        self.assertEqual("Rover", self.Dog3.get_name())                             #
        #self.assertEqual("Rover", self.Dog3.name)             # AssertionError: 'Rover' != <property object at 0x10b0d52c8>

    def test_classes_and_instances_do_share_class_attributes(self):
        fido = self.Dog3()
        fido.set_name("Fido")
        self.assertEqual("Fido", fido.get_name())
        self.assertEqual("Fido", self.Dog3.get_name())

    # ------------------------------------------------------------------

    class Dog4:
        def a_class_method(cls):
            return 'dogs class method'

        def a_static_method():
            return 'dogs static method'

        a_class_method = classmethod(a_class_method)
        a_static_method = staticmethod(a_static_method)
                                                            # what happened to in Python you can only do things one way
                                                            # the obvious way !! :/
    def test_you_can_define_class_methods_without_using_a_decorator(self):
        self.assertEqual('dogs class method', self.Dog4.a_class_method())

    def test_you_can_define_static_methods_without_using_a_decorator(self):
        self.assertEqual('dogs static method', self.Dog4.a_static_method())

    # ------------------------------------------------------------------

    def test_heres_an_easy_way_to_explicitly_call_class_methods_from_instance_methods(self):
        fido = self.Dog4()
        self.assertEqual('dogs class method', fido.__class__.a_class_method())


    # ------------------------------------------------------------------
    # -- ADDED ---------------------------------------------------------
    # https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute
    
    
    class A(object):        # A inherits object (this is implicitic anyway)
        #self._x = -1                        # NameError: name 'self' is not defined
        
        _x = -1                              # referenced by self._x in methods  
        '''A._x is an attribute'''           # A._x   - class variable (co-exists w/ object var across objects)
                                             # a._x   - object variable when a = A()
        @property
        def x(self):
            '''
            A.x is a property
            This is the getter method
            '''
            return self._x
    
        @x.setter
        def x(self, value):
            """
            This is the setter method
            where I can check it's not assigned a value < 0
            """
            if value < 0:
                raise ValueError("Must be >= 0")
            self._x = value
    
    # >>> a = A()
    # >>> a._x = -1
    # >>> a.x = -1
    # Traceback (most recent call last):
    #   File "ex.py", line 15, in <module>
    #     a.x = -1
    #   File "ex.py", line 9, in x
    #     raise ValueError("Must be >= 0")
    # ValueError: Must be >= 0
    a = A()
    print('----- class A(object): -----S')   # ----- class A(object): -----S
    print(A._x)                              # -1           class attribute - mnainained separately from each object
    print(a._x)                              # -1           object attribute (retrieved from class attribute)
    print(id(A._x))                          # 4395528320 <-----\  
    print(id(a._x))                          # 4395528320 <------\---------------------------------# same
                                                                                                   #
    a._x = 10                                                                                      #
    print(a._x)                              # 10           object attribute  <#  new allocation   #
    print(id(a._x))                          # 4395528512                      #                   #
    a.x = 5                                                                    #                   #
    print(a._x)                              # 5            object attribute   #                   #
    print(a.x)                               # 5            object attribute  <#-same object       #
    print(id(A._x))                          # 4395528320 <----------------------------------------#
    print(id(a._x))                          # 4395528512
    print(id(a.x))                           # 4395528512   
    print(type(a._x))                        # <class 'int'>
    print(type(a.x))                         # <class 'int'>

    print(A._x)                              # -1
    b = A()
    b._x = 40
    b.x = 14
    print(b._x)                              # 14
    print(b.x)                               # 14
    print(A._x)                              # -1
    print('----- class A(object): -----E')   # ----- class A(object): -----E

    # same as above w/o the id info - bit clearer
    print('----- class A(object): -----S')   # ----- class A(object): -----S
    print(A._x)                              # -1           class attribute - mnainained separately from each object
    print(a._x)                              # -1           object attribute (retrieved from class attribute)
    a._x = 10                                                                                    
    print(a._x)                              # 10           object attribute  <#  new allocation 
    a.x = 5                                                                    #                 
    print(a._x)                              # 5            object attribute   #                 
    print(a.x)                               # 5            object attribute  <#-same object     
    print(A._x)                              # -1
    b = A()
    b._x = 40
    b.x = 14
    print(b._x)                              # 14
    print(b.x)                               # 14
    print(A._x)                              # -1
    b._y = 99
    b.y =  16
    print(b._y)                              # 99       # _y attribute added on the fly
    print(b.y)                               # 16       # y attribute added on the fly   - no property define so values differ
    print(dir(a))           # ['__class__', '__delattr__', . . . '__weakref__', '_x', 'x']
    print(dir(b))           # ['__class__', '__delattr__', . . . '__weakref__', '_x', '_y', 'x', 'y']
    #print(a._y)                             # AttributeError
    #print(a.y)                              # AttributeError
    print('- - - weirdly')
    b.__y = 127                                          # double underscore private
    print(b.__y)                             # 127       # __y attribute added on the fly
    print(dir(b))           # ['_AboutClassAttributes__y', '__class__', . . . '__weakref__', '_x', '_y', 'x', 'y']
                            #     ^ A class in mangled name TODO
    print('----- class A(object): -----E')   # ----- class A(object): -----E







