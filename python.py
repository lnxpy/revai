# File: geometry_calculator.py

import math

def calculate_area_of_circle(radius):
    '''Calculate the area of a circle.'''
    if radius < 0:
        raise ValueError('Radius must be non-negative.')
    return math.pi * radius**2

def calculate_circumference_of_circle(radius):
    '''Calculate the circumference of a circle.'''
    if radius < 0:
        raise ValueError('Radius must be non-negative.')
    return 2 * math.pi * radius

def calculate_volume_of_sphere(radius):
    '''Calculate the volume of a sphere.'''
    if radius < 0:
        raise ValueError('Radius must be non-negative.')
    return (4/3) * math.pi * radius**3

