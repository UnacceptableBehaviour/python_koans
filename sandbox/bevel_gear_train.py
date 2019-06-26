#! /usr/bin/env python

#import sys
#print("Python Version: "+sys.version_info[0]+sys.version_info[1])
#if sys.version_info[0] < 3:
#    raise Exception("Must be using Python 3")

# safe exit - raises exceprion, does cleanup
# import sys
# sys.exit(0)

# thin wrapper for libc exit - for debug
# import os
# os._exit(1)

from pprint import pprint

import math

print("BEVEL GEAR POWER TRAIN CALCS")


# (rear) drive bevel gear - dbg - applies torque from drive shaft to rear bevel gear - rbg
dbg_peripheral_cylinder_diameter = 6.0
dbg_peripheral_cylinder_gap = 1.0
dbg_peripheral_cylinder_depth = 5.0
dbg_peripheral_cylinder_count = 10

# cylinder holding a plurality of peripheral drive cylinders
dbg_cylinder_circumference = (dbg_peripheral_cylinder_count * dbg_peripheral_cylinder_diameter) + ((dbg_peripheral_cylinder_count - 1) * dbg_peripheral_cylinder_gap)

dbg_cylinder_radius = dbg_cylinder_circumference / ( 2 * math.pi )

print (f"For a {dbg_peripheral_cylinder_count} drive cylinder gear circumference is {dbg_cylinder_circumference}mm")


# (rear) wheel bevel gear
wbg_void_diameter = dbg_peripheral_cylinder_diameter 
#wbg_void_diameter = dbg_peripheral_cylinder_diameter + 0.2  # leave wiggle room for deformation in 3d print 
wbg_no_of_voids = 10
# cog with a plurality of drive voids
wbg_cog_circumference = (wbg_no_of_voids * wbg_void_diameter) + ((wbg_no_of_voids - 1) * dbg_peripheral_cylinder_gap)
wbg_min_cog_gap = 5.0
wbg_cog_thickness = 3.0

print (f"For a {wbg_no_of_voids} void cog circumference is {wbg_cog_circumference}mm")


def calc_cog_circ(no_of_voids, void_diameter, play_size):
  c = (no_of_voids * void_diameter) + ((no_of_voids - 1) * ( dbg_peripheral_cylinder_gap + play_size))
  return c

# r = c / 2pi
def calc_cog_radius(c):
  r = c / (2 * math.pi)
  return r


print("CALCULATING CIRCUMFERENCES & TEETH IN REAR BEVEL GEAR")
#
next_cog_radius = 10.9
for no_of_voids in range(10,100):
  c = calc_cog_circ(no_of_voids, dbg_peripheral_cylinder_diameter, 0.0)
  r = calc_cog_radius(c)  
  next_cog_radius = r + wbg_cog_thickness + wbg_min_cog_gap
  
  print(f"V: {no_of_voids}    C:{c} \tR:{round(r,2)}  \tNR:{round(next_cog_radius,2)}")

  
c_a = []  

next_cog_radius = 10.9
for no_of_voids in range(10,200):
  c = calc_cog_circ(no_of_voids, dbg_peripheral_cylinder_diameter, 0.0)
  r = calc_cog_radius(c)
  
  if (r > next_cog_radius):
    print(f"V: {no_of_voids}    C:{c} \tR:{round(r,2)} {round(r)}")
    c_a.append(round(r))
    next_cog_radius = r + wbg_cog_thickness + wbg_min_cog_gap

pprint(c_a)

arr_str = "["
for c in c_a:
    arr_str += f"{c},"
arr_str += f"]"

print(c_a)


