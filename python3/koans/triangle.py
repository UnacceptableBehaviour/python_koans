#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
from pprint import pprint

def triangle(a, b, c):
    triangle_sides = set([a,b,c])
    list_sides = [a,b,c]
    
    if 0 in triangle_sides:
        raise TriangleError('funky trianle: 0 length side means its a line!')
    
    if True in [i < 0 for i in triangle_sides]:
        raise TriangleError('funky trianle: -ve side means its in another dimension! (pay close attention..)')
    
    m = max(list_sides)          # get max value
    list_sides.remove(m)         # remove it from the set
    if m >= sum(list_sides):       # see its larger than the remaining set members
        raise TriangleError('funky trianle: 1 very long side!')
    
    triangle_type = ['no_exist','equilateral','isosceles','scalene']
    
    return( triangle_type[len(triangle_sides)] )


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
