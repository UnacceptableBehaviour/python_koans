#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

    def test_parallel_assignments_with_extra_values(self):
        # >>> c,d,e = [1,2,3,4,[5,6],7,8]
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # ValueError: too many values to unpack (expected 3)
        #
        # but add *
        #
        # >>> c,*d,e = [1,2,3,4,[5,6],7,8]                      # 8 will consume left over of the unpacking
        # >>> c
        # 1
        # >>> d
        # [2, 3, 4, [5, 6], 7]
        # >>> e
        # 8
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)

