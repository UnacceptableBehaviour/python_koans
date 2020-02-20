#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'Matunas', 'Ramirez', 'Malcolm', 'MacLeod'}, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual(set([1,2,3]), {1, 2, 3})
        self.assertEqual(set(), set())  # no idea what is being got at here!?

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(dict, {}.__class__)

    def test_creating_sets_using_strings(self):
        self.assertEqual({'12345'}, {'12345'})
        self.assertEqual({'5', '2', '1', '3', '4'}, set('12345'))   # set order picked by python console!?

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('12345')))   # returns list
        # set(sorted(set('12345'))) > {'5', '2', '1', '3', '4'}             # tree?
        # ^ ^        ^ ^
        #
        # >>> sorted(set('12345'))
        # ['1', '2', '3', '4', '5']
        # >>> type( sorted(set('12345')))
        # <class 'list'>
        # >>> set(sorted(set('12345')))
        # {'5', '2', '1', '3', '4'}

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}
                                                                                             # non-commutative?
        self.assertEqual({'Willie'}, scotsmen - warriors)                                    # difference - has direction A-B B-A
        self.assertEqual({'Leonidas', 'MacLeod', 'Wallace', 'Willie'}, scotsmen | warriors)  # union                (U)
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors)                        # intersection         (upside down U)
        self.assertEqual({'Leonidas', 'Willie'}, scotsmen ^ warriors)                        # symmetric difference (sign is delta)
                                                                                             # both side sides intead of one 

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )

    def test_we_can_compare_subsets(self):
        # >>> set('cherry cake')
        # {'k', 'a', 'y', 'h', 'c', ' ', 'r', 'e'}
        # >>> set('cake')
        # {'k', 'e', 'c', 'a'}        
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )

        # self.assertEqual(True, set('cake') > set('pie'))    # False
        # self.assertEqual(True, set('cake') < set('pie'))    # False

        self.assertEqual(False, set('cake') > set('pie'))        # NO understanD    TODO
        self.assertEqual(False, set('pie cake') < set('pie'))    # NO understanD
        self.assertEqual(True, set('pie cake') > set('pie'))     # NO understanD