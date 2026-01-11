"""
Assignment 3: Parametric Structural Canopy

Author: Nikolaj Rytter
"""

## Importing libraries
import numpy as np
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs
import math
import random

## function for anchor points using rs.BoundingBox
def boundingbox_anchor_pts(mesh):

    pts8 = rs.BoundingBox(mesh)
    pts4 = pts8[-4:]

    out_pts = []
    for pts0 in pts4:
        out_pts.append(rg.Point3d(pts0.X, pts0.Y, 0))
    
    x = sum([pt.X for pt in out_pts]) / 4.0
    y = sum([pt.Y for pt in out_pts]) / 4.0
    z = sum([pt.Z for pt in out_pts]) / 4.0

    bounds_center = rg.Point3d(x, y, z)

    anchor_pts = []

    angle_rad = math.radians(anchor_rot_angle)
    rot = rg.Transform.Rotation(angle_rad, bounds_center)

    for pt in out_pts:
        v_anchor_center = pt - bounds_center
    
        v_scaled = v_anchor_center * anchor_scale
    
        moved_pt = bounds_center + v_scaled
    
        moved_pt_rot = moved_pt
        moved_pt_rot.Transform(rot)
    
        anchor_pts.append(moved_pt_rot)
    return (anchor_pts)

## initial UV grid
def uv_grid(divU, divV):
    u = np.linspace(0.0, 1.0, divU)
    v = np.linspace(0.0, 1.0, divV)
    U, V = np.meshgrid(u, v)

    return U, V

## Heightmap
def heightmap(U, V, amplitude, frequency, phase):

    # sine wave
    wave = np.sin((U * frequency + phase) * 2 * np.pi) * np.cos((V * frequency + phase) * 2 * np.pi)

    # sine ridges 
    ridges = np.abs(np.sin(5 * U * np.pi)) * 0.5

    # combining waves
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

## surface from moved points
def surface_from_point_grid(point_grid):

    rows = len(point_grid)
    cols = len(point_grid[0])

    flat_points = [pt for row in point_grid for pt in row]

    srf_id = rs.AddSrfPtGrid((rows, cols), flat_points)
    return srf_id