#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutExceptions(Koan):

    class MySpecialError(RuntimeError):                     # inherits from RuntimeError
        pass

    def test_exceptions_inherit_from_exception(self):
        # >>> class MySpecialError(RuntimeError):pass;
        # ... 
        # >>> MySpecialError.mro()                          # mro - method resolution order - query inheritance chain
        # [<class '__main__.MySpecialError'>, <class 'RuntimeError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
        # >>> type(MySpecialError.mro())
        # <class 'list'>
        # >>> len(MySpecialError.mro())
        # 5
        # >>> type(MySpecialError.mro()[0].__name__)
        # <class 'str'>

        mro = self.MySpecialError.mro()                     # mro - method resolution order - query inheritance chain
        self.assertEqual('MySpecialError', mro[0].__name__)
        self.assertEqual('RuntimeError', mro[1].__name__)
        self.assertEqual('Exception', mro[2].__name__)
        self.assertEqual('BaseException', mro[3].__name__)
        self.assertEqual('object', mro[4].__name__)

    def test_try_clause(self):
        from pprint import pprint
        result = None
        try:
            self.fail("Oops")                                           # whats this?
        except Exception as ex:
            result = 'exception handled'
            print("--investigating--")
            pprint(ex)
            ex2 = ex

        # >>> m = MySpecialError('bla')
        # >>> isinstance(m, MySpecialError)
        # True
        # >>> isinstance(m, RuntimeError)
        # True
        # >>> m
        # MySpecialError('bla')
        # >>> issubclass(RuntimeError, Exception)
        # True
        # >>> type(m.args)
        # <class 'tuple'>
        # >>> len(m.args)
        # 1
        # >>> m.args[0]
        # 'bla'
        # >>> isinstance(m, RuntimeError)                               # < < < < < < !! ?? TODO
        # True                                                                      #
                                                                                    #
        self.assertEqual('exception handled', result)                               #
                                                            # https://docs.python.org/3/tutorial/errors.html#exceptions
        self.assertEqual(True, isinstance(ex2, Exception))                          #
        self.assertEqual(False, isinstance(ex2, RuntimeError))          # < < < < < < !!

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual('Oops', ex2.args[0])

    def test_raising_a_specific_error(self):
        result = None
        ex_dbg = None
        try:
            #pass
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]
            ex_dbg = ex
            #print("- - i - -")
            #print(type(ex_dbg))
            #print(ex_dbg.mro())

        self.assertEqual('exception handled', result)
        self.assertEqual("My Message", msg)
        #self.assertEqual(True, isinstance(ex_dbg, RuntimeError))       # PASS
        #self.assertEqual(True, isinstance(ex_dbg, MySpecialError))     # FAILS          TODO - WHY?
                                                            # NameError: name 'MySpecialError' is not defined
                                                            # https://docs.python.org/3/tutorial/errors.html#exceptions
    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'                                   # TODO - Ex to test

        self.assertEqual('no damage done', result)


    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual('always run', result)
