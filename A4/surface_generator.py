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

### initial UV grid
def uv_grid(divU, divV):
    u = np.linspace(0.0, 1.0, divU)
    v = np.linspace(0.0, 1.0, divV)
    U, V = np.meshgrid(u, v)

    return U, V

