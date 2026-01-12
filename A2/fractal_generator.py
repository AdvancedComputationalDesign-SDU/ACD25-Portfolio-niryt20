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

## Initial branching angle
ini_angle = 15

## Branch length generation parameters
max_length = 2.5
min_length = 0.3
length_factor = 0.5

## Attractor point
attractor = Point(2, 2)
attractor_strength = 0.0

## 1st branch conditions
A = (0, 0)
V = (0, 1)

## List containing branch geometry
Lines = []

## Function for rotating a given vector
def rotate_vector(v, angle_deg):
    angle_rad = math.radians(angle_deg)
    x, y = v
    xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (xr, yr)

## Normalize vectors
def normalize(v):
    l = math.hypot(v[0], v[1])
    return (v[0]/l, v[1]/l)

## Exponential decay of branch length
def step_length(g):
    return 1.0 * (0.7 ** g)

## Length field based on distance from attractor point
def length_field(pt):
    d = math.hypot(pt[0] - attractor.x, pt[1] - attractor.y)
    return max(min_length, max_length - length_factor * d)

## Growth function
def Grow(pt, v, g):
    if g < gen:

        # Vector toward attractor
        to_attr = (attractor.x - pt[0], attractor.y - pt[1])

        # Biased growth towards attractor point
        v = (v[0] + attractor_strength * to_attr[0], v[1] + attractor_strength * to_attr[1],)

        v = normalize(v)
        L = length_field(pt)

        V1 = rotate_vector(v, -ini_angle)
        pt1 = (pt[0] + V1[0]*L, pt[1] + V1[1]*L)    

        V2 = rotate_vector(v, ini_angle)
        pt2 = (pt[0] + V2[0]*L, pt[1] + V2[1]*L)

        L1 = LineString([pt, pt1])
        L2 = LineString([pt, pt2])

        Lines.append(L1)
        Lines.append(L2)

        Grow(pt1, V1, g + 1)
        Grow(pt2, V2, g + 1)

## 1st branch Generation
B = (A[0] + V[0], A[1] + V[1])
Lines.append(LineString([A, B]))

Grow(B, V, 0)

## Visualization
fig, ax = plt.subplots()

for line in Lines:
    x, y = line.xy
    ax.plot(x, y, color='green', linewidth=1)

# Attractor
ax.scatter(attractor.x, attractor.y, color='red')

ax.set_aspect('equal')
plt.axis('off')
plt.show()
