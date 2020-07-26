"""
Write a Python program to find the volume of a sphere with diameter 12 cm
Formula: V=4/3 * π * r 3
"""
import math
diameter = 12
# calculate radius
radius = diameter/2
# V=4/3 * π * r 3
volumeOfSphere = (4/3) * math.pi * radius**3
print("Volume Of Sphere (radius=",radius,"cm)= ", volumeOfSphere,"cubic centimeter(cm3)")