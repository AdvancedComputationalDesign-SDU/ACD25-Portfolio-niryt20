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

