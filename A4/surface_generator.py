"""
Assignment 4: Agent-Based Model for Surface Panelization

Author: Nikolaj Rytter

Surface Generator

Description:
This code generates a surface

Note: This script is intended to be used within Grasshopper's Python
scripting component.
"""

## Libraries
import numpy as np
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs
import math
import random

O = (orix,oriy,oriz)
S = (sizex,sizey)

## Initial UV grid
def uv_grid(divU, divV):
    u = np.linspace(0.0, 1.0, divU)
    v = np.linspace(0.0, 1.0, divV)
    U, V = np.meshgrid(u, v)

    return U, V

## Heightmap
def heightmap(U, V, amplitude, frequency, phase):

    # Sine wave
    wave = np.sin((U * frequency + phase) * 2 * np.pi) * np.cos((V * frequency + phase) * 2 * np.pi)

    # Sine ridges 
    ridges = np.abs(np.sin(5 * U * np.pi)) * 0.5

    # Combining waves
    H = amplitude * (random.uniform(0.0,1.0)*wave + random.uniform(0.0,1.0)*ridges)

    return H

## Rectangular grid of points
def make_point_grid_xy(divU, divV, origin, size):

    ox, oy, oz = origin
    sx, sy = size

    step_u = 1.0 / (divU - 1) if divU > 1 else 0
    step_v = 1.0 / (divV - 1) if divV > 1 else 0

    grid = []
    for j in range(int(divV)):
        v = j * step_v
        row = []
        for i in range(int(divU)):
            u = i * step_u

            x = ox + u * sx
            y = oy + v * sy
            row.append((x, y, oz))
        grid.append(row)

    return grid

## Moving along z based on heightmap
def move_along_z(pts):
    pts_moved = [
        [
            (x, y, float(z + a[i, j]))
            for j, (x, y, z) in enumerate(row)
        ]
    for i, row in enumerate(pts)
    ]
    return pts_moved

## Surface from moved points
def surface_from_point_grid(point_grid):

    rows = len(point_grid)
    cols = len(point_grid[0])

    flat_points = [pt for row in point_grid for pt in row]

    srf_id = rs.AddSrfPtGrid((rows, cols), flat_points)
    return srf_id