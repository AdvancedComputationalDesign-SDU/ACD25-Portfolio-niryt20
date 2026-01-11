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

# -----------------------------------------------------------------------------
# 1. Heightmap Generation
# -----------------------------------------------------------------------------
def generate_heightmap(shape=(50, 50), params=None):
    """Create a heightmap array from input data."""
    # TODO: generate and return a NumPy heightmap array
    raise NotImplementedError("Implement generate_heightmap(...)")


# -----------------------------------------------------------------------------
# 2. Uniform Surface Sampling
# -----------------------------------------------------------------------------
def sample_surface_uniform(surface, shape=(50, 50)):
    """Sample a surface uniformly in its UV domain."""
    # TODO: generate UV grid, evaluate surface points, return as NumPy array
    raise NotImplementedError("Implement sample_surface_uniform(...)")


# -----------------------------------------------------------------------------
# 3. Grid Manipulation (apply heightmap to grid)
# -----------------------------------------------------------------------------
def manipulate_point_grid(heightmap, point_grid, scalar):
    """Apply heightmap values to a sampled point grid."""
    # TODO: modify point_grid using heightmap and return it
    raise NotImplementedError("Implement manipulate_point_grid(...)")


# -----------------------------------------------------------------------------
# 4. Build Surface from Manipulated Points
# -----------------------------------------------------------------------------
def build_surface(point_grid):
    """Build a surface from a point grid."""
    # TODO: use Rhino.Geometry to construct a surface from the point grid
    raise NotImplementedError("Implement build_surface(...)")

heightmap = generate_heightmap(shape=(U,V))
pt_grid = sample_surface_uniform(surface, shape=(U,V))
manip_pt_grid = manipulate_point_grid(heightmap, pt_grid, scalar)
manip_srf = build_surface(pt_grid)