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

## Surface from moved points
def surface_from_point_grid(point_grid):

    rows = len(point_grid)
    cols = len(point_grid[0])

    flat_points = [pt for row in point_grid for pt in row]

    srf_id = rs.AddSrfPtGrid((rows, cols), flat_points)
    return srf_id

## Uniform grid from srf
def sample_uniform_grid(surface, U, V):
    du0, du1 = rs.SurfaceDomain(surface, 0)
    dv0, dv1 = rs.SurfaceDomain(surface, 1)

    pu = [du0 + (du1 - du0)*(i/float(U)) for i in range (U+1)]
    pv = [dv0 + (dv1 - dv0)*(i/float(V)) for i in range (V+1)]

    pts = []

    for u in pu:
        row = []
        for v in pv:
            tmp_pt = rs.EvaluateSurface(surface, u, v)
            row.append(tmp_pt)
        pts.append(row)
    
    return pts

## Tri mesh from surface points
def tri_mesh_from_points(pts):

    rows = len(pts)
    cols = len(pts[0])

    vertices = [pts[i][j] for i in range(rows) for j in range (cols)]

    faces = []
    vcols = cols

    for i in range(rows - 1):
        for j in range(cols - 1):
            a = i * vcols + j
            b = a + 1
            c = b + vcols
            d = c - 1

            faces.append([a, b, c])
            faces.append([a, d, c])

    mesh = rs.AddMesh(vertices, faces)
    return mesh

## Branching structure
def Grow(pt, v, length, g):
    if g >= gen:
        return

    plane = rs.PlaneFromNormal(pt, v)
    random_pt = rs.EvaluatePlane(plane, [random.uniform(-1, 1), random.uniform(-1, 1)])
    rot_axis = rs.VectorCreate(random_pt, pt)

    V1 = rs.VectorRotate(v, random.uniform(-angle,0), rot_axis)
    pt1 = rs.PointAdd(pt, rs.VectorScale(V1, length))

    if g + 1 == gen:
        pt1 = rs.MeshClosestPoint(mesh, pt1)[0]

    L1 = rs.AddLine(pt, pt1)
    Lines.append(L1)

    Grow(pt1, V1, length * random.uniform(0.75,0.95), g+1)

    V2 = rs.VectorRotate(v, random.uniform(0,angle), rot_axis)
    pt2 = rs.PointAdd(pt, rs.VectorScale(V2, length))

    if g + 1 == gen:
        pt2 = rs.MeshClosestPoint(mesh, pt2)[0]

    L2 = rs.AddLine(pt, pt2)
    Lines.append(L2)

    Grow(pt2, V2, length * random.uniform(0.75,0.95), g+1)

##Inputs

#U and V
dU = int(dU)
dV = int(dV)

U1 = int(U1)
V1 = int(V1)

#Seed
random.seed(seed)

#Size and origin of canopy
O = (orix,oriy,oriz)
S = (sizex,sizey)

#Branching input
V = [0,0,1]
Lines = []

###Run Functions###

# UV grid
U_grid, V_grid = uv_grid(dU, dV)

# Heightmap
a = heightmap(U_grid, V_grid, amp, frq, pha)

# Grid of points
pts = make_point_grid_xy(dU, dV, O, S)

# Moving grid points along z
pts_moved = move_along_z(pts)

# Surface from moved points
srf = surface_from_point_grid(pts_moved)

# Surface sampling
pts_grid_UV = sample_uniform_grid(srf, U1, V1)

# Creating tri meshes
mesh = tri_mesh_from_points(pts_grid_UV)

# Anchor points from boundingbox    
a_pts = boundingbox_anchor_pts(mesh)