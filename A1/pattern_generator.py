## Importing numpy libraries
import numpy as np
import matplotlib.pyplot as plt

## Sin function frequency
ff = (1/(1.5*3.14))

## Number of attractor points
attr_n = 7

## Canvas dimensions
width = 200
height = 200

## Setting up the canvas
canvas = np.zeros((height, width)) 

## Creating a given number of random attractor points
attractors = np.random.random((attr_n, 2)) * 200

## Defining function for euclidean distance
def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2, axis=1))