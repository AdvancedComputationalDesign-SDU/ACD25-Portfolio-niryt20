"""
Assignment 2: Fractal Generator

Author: Nikolaj Rytter

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

## Import necessary libraries
import math
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point

## Number of generations
gen = 5

## Branch length generation parameters
max_length = 1.5
min_length = 0.3
length_factor = 0.5

## Attractor point
attractor = Point(-2, 2)
attractor_strength = 0.1

## 1st branch conditions
A = (0, 0)
V = (0, 1)

## List containing branch geometry
Lines = []
## Function for rotating a given vector
def rotate_vector(v, angle_deg):
    angle_red = math.radians(angle_deg)
    x, y = v
    xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (xr, yr)

def normalize(v):
    l = math.hypot(v[0], v[1])
    return (v[0]/l, v[1]/l)

