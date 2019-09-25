#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO - if it's not in __all__ it's not exposed by wildcard *
# EG
# form ./local_module_with_all_defined import *
# imports classes  Goat & _Velociraptor
# NOTE _Velociraptor would be private because of underscore
#      but isn't because it's included in __all__

__all__ = (
    'Goat',
    '_Velociraptor'
)

print(f"__all__ even underscore! {type(__all__)} (for added confusion)")

class Goat:
    @property
    def name(self):
        return "George"

class _Velociraptor:
    @property
    def name(self):
        return "Cuddles"

class SecretDuck:
    @property
    def name(self):
        return "None of your business"
