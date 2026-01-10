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
canvas = np.zeros((height, width, 3)) 

## Creating a given number of random attractor points
attractors = np.random.random((attr_n, 2)) * 200

## Defining function for euclidean distance
def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2, axis=1))

## A loop, distance check for each pixel, convertions to sin function and coloring the canvas
for x in range(width):
    for y in range(height):
        # Calculating distance from pixel to all attractors
        dists = distance(np.array([x, y]), attractors)

        #Sin function for distance
        s = np.sin(dists*ff)

        # Summation of the sine of distances to get interference
        s = np.array(s)

        ss = sum(s)

        # RGB channels
        r = (np.sin(ss+1))
        g = (np.cos(ss+1))
        b = (dists)

        ## Updating the canvas with final summed values
        canvas[y, x, 0] = r
        canvas[y, x, 1] = g

## hsv to show values
plt.imshow(canvas)
## Hiding axis
plt.axis('off') 
## Printing the plot in new window
plt.show() 