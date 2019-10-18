#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Create a Proxy Class
#
# In this assignment, create a proxy class (one is started for you
# below).
#
# 1.
# You should be able to initialize the proxy object with any object.
#
# 2.
# Any attributes called on the proxy object should be forwarded
# to the target object.
#
# 3.
# As each attribute call is sent, the proxy should
# record the name of the attribute sent.
#
# 4.
# You will need to add a method missing handler and any other supporting
# methods.
#
# The specification of the Proxy class is given in the AboutProxyObjectProject koan.

# Note: This is a bit trickier than its Ruby Koans counterpart, but you
# can do it!

# revise L34 about_attribute_access.py
#
# Proxy Pattern  - Intermediary Interface 
# https://refactoring.guru/design-patterns/proxy  
#
# Object Proxying Recipe - Active State
# http://code.activestate.com/recipes/496741-object-proxying/

from runner.koan import *

print("Loading script: class Proxy:")

class Proxy: #(object):                            
    #__slots__ = ["_obj", "__weakref__"]     # replace __disct__ so __setattr__ can find _obj
    
    def __init__(self, target_object):
        # WRITE CODE HERE
        object.__setattr__(self, 'messages', [])
        
        #print("Proxy.messages", self.messages)
        print("Proxy.messages", object.__getattribute__(self, 'messages'))
        
        #initialize '_obj' attribute last. Trust me on this!
        print("Proxy.__init__ S")
        # self._obj = target_object   # << AttributeError: 'Proxy' object has no attribute '_obj'
        object.__setattr__(self, '_obj', target_object)
        print("Proxy.__init__ E")

    # WRITE CODE HERE
    def __getattribute__(self, name):
        print("__getattribute__", name)
        if name == 'messages':
            return object.__getattribute__(self, 'messages')
        else:    
            return getattr(object.__getattribute__(self, "_obj"), name)  # why doesn't this recurse?       
    
    # def __getattribute__(self, name):
    #     print("Proxy.__getattribute__", self, name, self._obj)  # <<< self._obj causes recurison
    #     print("Proxy.__getattribute__", self, name)
    #     
    #     if name in vars(self._obj):   <<< self._obj causes recurison
    #         print("Proxy.__getattribute__ name in __dict__", name)
    #         #if self._obj
    #     #return getattr(self._obj, name)()
    
    def __delattr__(self, name):
        delattr(object.__getattribute__(self, "_obj"), name)

    def __setattr__(self, name, value):
        #pass
        setattr(object.__getattribute__(self, "_obj"), name, value)
        

# The proxy object should pass the following Koan:
#
class AboutProxyObjectProject(Koan):
    def test_proxy_method_returns_wrapped_object(self):
        # NOTE: The Television class is defined below
        tv = Proxy(Television())
        print("AboutProxyObjectProject.isinstance(tv, Proxy)", isinstance(tv, Proxy))
        #print(vars(tv)) # TypeError: vars() argument must have __dict__ attribute < WTF?
        print(tv)
        print("AboutProxyObjectProject.isinstance(tv, Proxy) - E")
        self.assertTrue(isinstance(tv, Proxy))

    def test_tv_methods_still_perform_their_function(self):
        tv = Proxy(Television())

        tv.channel = 10
        tv.power()

        self.assertEqual(10, tv.channel)
        self.assertTrue(tv.is_on())

    def test_proxy_records_messages_sent_to_tv(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 10

        self.assertEqual(['power', 'channel'], tv.messages())

    def test_proxy_handles_invalid_messages(self):
        tv = Proxy(Television())

        ex = None
        with self.assertRaises(AttributeError):
            tv.no_such_method()


    def test_proxy_reports_methods_have_been_called(self):
        tv = Proxy(Television())

        tv.power()
        tv.power()

        self.assertTrue(tv.was_called('power'))
        self.assertFalse(tv.was_called('channel'))

    def test_proxy_counts_method_calls(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 48
        tv.power()

        self.assertEqual(2, tv.number_of_times_called('power'))
        self.assertEqual(1, tv.number_of_times_called('channel'))
        self.assertEqual(0, tv.number_of_times_called('is_on'))

    def test_proxy_can_record_more_than_just_tv_objects(self):
        proxy = Proxy("Py Ohio 2010")

        result = proxy.upper()

        self.assertEqual("PY OHIO 2010", result)

        result = proxy.split()

        self.assertEqual(["Py", "Ohio", "2010"], result)
        self.assertEqual(['upper', 'split'], proxy.messages())

# ====================================================================
# The following code is to support the testing of the Proxy class.  No
# changes should be necessary to anything below this comment.

# Example class using in the proxy testing above.
class Television:
    def __init__(self):
        print("Television.__init__", self)
        self._channel = None
        self._power = None

    @property
    def channel(self):
        print("Television.channel R")
        return self._channel

    @channel.setter
    def channel(self, value):
        print("Television.channel W:", value)
        self._channel = value

    def power(self):        
        if self._power == 'on':
            print("Television.OFF")
            self._power = 'off'
        else:
            print("Television.ON")
            self._power = 'on'

    def is_on(self):
        on = (self._power == 'on')
        print("Television. ON:", on)
        return on

# Tests for the Television class.  All of theses tests should pass.
class TelevisionTest(Koan):
    
    def test_it_turns_on(self):
        tv = Television()

        tv.power()
        self.assertTrue(tv.is_on())

    def test_it_also_turns_off(self):
        tv = Television()

        tv.power()
        tv.power()

        self.assertFalse(tv.is_on())

    def test_edge_case_on_off(self):
        tv = Television()

        tv.power()
        tv.power()
        tv.power()

        self.assertTrue(tv.is_on())

        tv.power()

        self.assertFalse(tv.is_on())

    def test_can_set_the_channel(self):
        tv = Television()

        tv.channel = 11
        self.assertEqual(11, tv.channel)



    
    # def __instancecheck__(obj_inst, class_info):
    #     '''
    #     implement isInstance - Return true if the object argument is an instance of the classinfo argument,
    #     or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type,
    #     the function always returns false. . . . Helps to know what youre aiming for!
    #     https://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass
    #     I says example is NAIVELY SIMPLE . .
    #     any(iterable) - Return True if any element of the iterable is true.
    #     '''
    #     print("Proxy.__instancecheck__")
    #     return false #isinstance(obj_inst, class_info)     # solution simpler than I thought, 