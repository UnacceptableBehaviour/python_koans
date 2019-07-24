#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    def test_iterators_are_a_type(self):
        it = iter(range(1,6))

        total = 0

        for num in it:
            total += num

        # >>> [x for x in range(1,6)]
        # [1, 2, 3, 4, 5]

        self.assertEqual(15, total)

    def test_iterating_with_next(self):
        stages = iter(['alpha','beta','gamma'])

        try:
            self.assertEqual('alpha', next(stages))
            next(stages)
            self.assertEqual('gamma', next(stages))
            next(stages)
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertRegex(err_msg, 'Ran out of iterations')

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):              
        seq = [1, 2, 3]
        mapped_seq = list()

        mapping = map(self.add_ten, seq)

        self.assertNotEqual(list, mapping.__class__)
        self.assertEqual(map, mapping.__class__)
        # In Python 3 built in iterator funcs return iterable view objects
        # instead of lists

        for item in mapping:
            mapped_seq.append(item)

        self.assertEqual([11, 12, 13], mapped_seq)

        # Note, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    def test_filter_selects_certain_items_from_a_list(self):
        # >>> seq = [1, 2, 3, 4, 5, 6]
        # >>> def is_even(item): return (item % 2) == 0
        # ... 
        # >>> f = filter(is_even, seq)
        # >>> type(f)
        # <class 'filter'>
        # >>> type(list(f))
        # <class 'list'>
        # >>> list(f)
        # []                                # NOPE
        # >>> f
        # <filter object at 0x10a41e908>
        # >>> iter(f)
        # <filter object at 0x10a41e908>
        # >>> [x for x in f]                     # STILL NOPE
        # []
        # >>> [x for x in filter(is_even, seq)]     # OK
        # [2, 4, 6]


        # >>> f = filter(is_even, seq)
        # >>> next(f)
        # 2
        # >>> next(f)
        # 4
        # >>> next(f)
        # 6
        # >>> next(f)
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # StopIteration
        
        def is_even(item):
            return (item % 2) == 0
            
        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item)

        self.assertEqual([2, 4, 6], even_numbers)

    def test_just_return_first_item_found(self):
        def is_big_name(item):
            return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli","BadBoyBuba"]
        name = None

        iterator = filter(is_big_name, names)
        try:
            name = next(iterator)
            print(f"next: {name}")          # next: Clarence
            name = next(iterator)
            print(f"next: {name}")          # next: BadBoyBuba
            name = next(iterator)           # trigger exception
            print(f"next: {name}")
        except StopIteration:
            msg = 'Ran out of big names'
            print(f"StopIteration: {msg}")

        self.assertEqual('BadBoyBuba', name)


    # ------------------------------------------------------------------

    def add(self,accum,item):
        return accum + item

    def multiply(self,accum,item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(int, result.__class__)
        # Reduce() syntax is same as Python 2

        self.assertEqual(9, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(24, result2)

        # Extra Credit:
        # Describe in your own words what reduce does.
        # take first 2 parameters and pass to function
        # use the retuned value an the next parameter and pass to function
        # keep going until no more parameters left, return final value.


    # ------------------------------------------------------------------

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1,5):
            pass

        self.assertEqual(4, num)

    # ------------------------------------------------------------------

    def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
        # Ranges are an iterable sequence
        # filter(by_this_function, data_to_filter)
        # map(apply_this_function, data_to_process)        

        result = map(self.add_ten, range(1,4))
        self.assertEqual([11,12,13], list(result))

        try:
            file = open("example_file.txt")
            # contains:
            # this
            # is
            # a
            # test            

            try:
                def make_upcase(line):
                    return line.strip().upper()
                
                upcase_lines = map(make_upcase, file.readlines())
                
                self.assertEqual(['THIS', 'IS', 'A', 'TEST'], list(upcase_lines))
            
            finally:
                # Arg, this is ugly.
                # We will figure out how to fix this later.
                file.close()
        except IOError:
            # should never happen
            self.fail()


    def test_quick_re_write_of_previous_test(self):
        # Ranges are an iterable sequence
        # filter(by_this_function, data_to_filter)
        # map(apply_this_function, data_to_process)        

        try:                                           # this this should close the file on a raise - test?
            with open("example_file.txt") as f:
                def make_upcase(line):
                    return line.strip().upper()
                
                upcase_lines = map(make_upcase, f.readlines())
                
                self.assertEqual(['THIS', 'IS', 'A', 'TEST'], list(upcase_lines))
            
        except IOError:
            # should never happen
            self.fail()
