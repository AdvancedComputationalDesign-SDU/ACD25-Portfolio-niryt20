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

## creating a given number of random attractor points
attractors = np.random.random((attr_n, 2)) * 200