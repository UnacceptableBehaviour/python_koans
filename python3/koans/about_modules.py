#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This is very different to AboutModules in Ruby Koans
# Our AboutMultipleInheritance class is a little more comparable
#

from runner.koan import *

from .another_local_module import *
from .local_module_with_all_defined import *


class AboutModules(Koan):
    def test_importing_other_python_scripts_as_modules(self):
        from . import local_module  # local_module.py                       . this directory
        # from ..   => ValueError: attempted relative import beyond top-level package
        # TODO test if this works from deeper dir

        duck = local_module.Duck()
        self.assertEqual("Daffy", duck.name)

    def test_importing_attributes_from_classes_using_from_keyword(self):
        from .local_module import Duck      # no module qualifier needed to use Duck class
        #      ^^

        duck = Duck()  # no module qualifier needed this time
        self.assertEqual("Daffy", duck.name)

    def test_we_can_import_multiple_items_at_once(self):
        from . import jims, joes

        jims_dog = jims.Dog()
        joes_dog = joes.Dog()
        self.assertEqual("jims dog", jims_dog.identify())
        self.assertEqual("joes dog", joes_dog.identify())

    def test_dual_import_conflict_resolution(self):
        from .jims import Dog
        from .joes import Dog

        whos_dog = Dog()
        print("whos_dog:")
        print(type(whos_dog))   # last imported - koans.joes.Dog in this case
        print(Dog.mro())
        self.assertEqual("joes dog", whos_dog.identify())

    def test_importing_all_module_attributes_at_once(self):
        """
        importing all attributes at once is done like so:
            from .another_local_module import *
        The import wildcard cannot be used from within classes or functions.
        """

        goose = Goose()
        hamster = Hamster()

        self.assertEqual("Mr Stabby", goose.name)
        self.assertEqual("Phil", hamster.name)

    def test_modules_hide_attributes_prefixed_by_underscores(self):
        #private_squirrel = SecretSquirrel()
        #self.assertEqual("Mr Anonymous", private_squirrel.name)
        
        with self.assertRaises(NameError):
            private_squirrel = _SecretSquirrel()        # 

        lizard = _Velociraptor()                        # not hidden?
        self.assertEqual("Cuddles", lizard.name)        # _Velociraptor is listed in the module tuple __all__ (attribute I think)
                                                        # NameError: name '_Velociraptor' is not defined if removed from __all__

    def test_private_attributes_are_still_accessible_in_modules(self):
        from .local_module import Duck  # local_module.py

        duck = Duck()
        self.assertEqual('password', duck._password)
        
        #self.assertEqual('password', duck._Duck__password)  # accessing mangled double underscore
                                                             # note NO dot - _Duck.__password
                                                             #                    ^
                                                             
        # module level attribute hiding doesn't affect class attributes
        # (unless the class itself is hidden).

    def test_a_module_can_limit_wildcard_imports(self):
        """
        Examine results of:
            from .local_module_with_all_defined import *
        """

        # 'Goat' is on the __all__ list
        goat = Goat()
        self.assertEqual("George", goat.name)

        # How about velociraptors? underscore so shoul be private right!? WRONG!
        lizard = _Velociraptor()
        self.assertEqual("Cuddles", lizard.name)
        # It goes back to privet ive removed from __all__ (attribute - I think)
        # NameError: name '_Velociraptor' is not defined if removed from __all__

        # SecretDuck? Never heard of her!
        with self.assertRaises(NameError):
            duck = SecretDuck()
