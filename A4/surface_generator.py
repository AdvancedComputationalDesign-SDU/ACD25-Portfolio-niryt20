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