---
layout: default
title: Project Documentation
parent: "A3: Parametric Structural Canopy"
nav_order: 2
nav_exclude: false
search_exclude: false
---

# Assignment 3: Parametric Structural Canopy

[View on GitHub]({{ site.github.repository_url }})

## Table of Contents

- [Objective](#objective)
- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Design Variations](#design-variations)
- [References and AI Acknowledgments](#references-and-ai-acknowledgments)

## Objective

In this assignment you will design and generate a **parametric structural canopy** in **Grasshopper** using the **GhPython (Python 3)** component. You will combine: (1) a **NumPy-driven heightmap** that modulates a NURBS surface, (2) **tessellation** of the resulting surface, and (3) **recursive, branching vertical supports** with controlled randomness. Your goal is to produce a small **family of design solutions** by varying parameters and algorithms, then communicate your process and results in a clear, reproducible report. You are asked to present **three** visually distinct designs. Each design must vary at least **two** of the implemented computational logic (heightmap-based surface geometry, tessellation strategy, branching supports).

## Pseudo-Code

`boundingbox_anchor_pts(mesh)`
    rs.BoundingBox(mesh) to get 4 appropriate anchorpoints
    loop through each anchor point, average coordinates to get a center point
    rg.Transform.Rotation(angle, center point) rotates anchorpoints around center point
returns anchor points

`heightmap(U, V, amplitude, frequency, phase)`
    np.sin wave in U direction
    np.cos wave in V direction

    addition of simple np.sin ridges parallel to V
returns height values in numpy array shaped as U,V

`make_point_grid_xy(divU, divV, origin, size)`
    1/(divU divV) normalized distance between points

    loops through normalized spacing, multiply by grid size to get real x, y coordinates
returns grid of points

`move_along_z(grid of points)`
    loops through each point 
        add heightmap value to z coordinate
returns moved grid of points

`surface_from_point_grid(moved grid of points)`
    loops through moved grid of points
        flatten data structure
    retruns flattened list of points

    rs.AddSrfPtGrid(data structure information ,flattened list of points) generates a surface from moved grid of points
returns surface

`sample_uniform_grid(surface, U, V)`
    rs.SurfaceDomain obtains start and end domains in U and V direction
    i/(U and V) for U and V + 1 produces evenly spaced U and V parameters
        returns lists of evenly spaved U and V parameters
    
    loops through U and V parameter
        rs.EvaluateSurface returns 3d points for the given U and V coordinate
returns grid of surface points

`tri_mesh_from_points(grid of surface points)`
    vertices = [pts[i][j] for i in range(rows) for j in range (cols)] devolves datastructure into a 1d list
    for each quad cell in grid of surface points
        a = i * vcols + j
        b = a + 1
        c = b + vcols
        d = c - 1

        creates two triangle cells via
            faces.append([a, b, c])
            faces.append([a, d, c])
    rs.AddMesh constructs a mesh from the list of vertices and the triangular faces
returns mesh

`Grow(starting point, starting direction, length, number of generations)`
    rs.PlaneFromNormal to generate a plane with current direction as the normal
    rs.EvaluatePlane generates a random point on plane for rotation
    rs.VectorCreate creates the current rotation axis
    rs.MeshClosestPoint locates closest point on mesh from branch
        at last gen - generates branch from endpoint to mesh

    for A in a_pts:
        B = rs.PointAdd(A, rs.VectorScale(V, L))
        Lines.append(rs.AddLine(A, B))
        Grow(B, V, L, 0)
    loop through each anchor point
returns list of lines

## Technical Explanation

The structural canopy is based on a heightmap generated from simple sine and cosine wave functions combined with custom ridges along U direction. The Canopy is controlled with amplitude, frequency and phase inputs. Randomness is introduced with different weighted wave and ridge values for each heightmap generation.

To create the tesselation of the structural canopy, the surface obtained from the heightmap is reparameterized and uniformly partitioned into a grid of points, each cell is divided into two triagular faces and a triangular mesh is made.

The structural branches are recursively generated from anchor points. Each iteration randomly rotates the current branch in 3d space. Last interation finds closest point on the canopy mesh and snaps onto it.

---

## Repository Structure

```
A3/
├── index.md                    # Do not edit front matter or content
├── README.md                   # Project documentation; Keep front matter, replace the rest with your project documentation
├── BRIEF.md                    # Assignment brief; Do not edit front matter or content
├── parametric_canopy.py        # Your code implementation
├── parametric_canopy.gh        # Your grasshopper definition
└── images/                     # Add diagram, intermediary, and final images here
    ├── canopy.png              # Assignment brief image; Do not delete
    └── ...
```

---