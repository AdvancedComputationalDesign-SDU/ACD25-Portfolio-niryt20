---
layout: default
title: Project Documentation
parent: "A2: Exploring Fractals through Recursive Geometric Patterns"
nav_order: 2
nav_exclude: false
search_exclude: false
---

# Assignment 2: Exploring Fractals through Recursive Geometric Patterns

[View on GitHub]({{ site.github.repository_url }})

## Table of Contents

- [Objective](#Objective)
- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Geometric Influences](#Geometric-influences)
- [Results](#results)
- [References](#references)

## Objective

In this assignment you will implement a **recursive generator** and enrich it with **geometric influences** that shape how the structure grows in space. You will work with geometric primitives (lines, polylines) using **Shapely** and render the results (e.g., with Matplotlib). The core of the assignment is to **couple formal grammar growth with spatial rules** such as attractor/repulsor points, fields, and collision constraints to produce expressive, controllable patterns.

While the branching or growth approach can be inspired by L-systems, it does not have to be strictly L-system based. You are encouraged to explore recursive generation methods influenced by spatial constraints and geometric rules that govern how the fractal develops and interacts with its environment. This opens opportunities to experiment with recursive branching logic, adaptive scaling, and spatial modulation beyond formal grammar rewriting.

## Pseudo-Code

1. **Initialize Variables**
   - Set canvas dimensions (height and width).
   - Define color values.
   - Set number of attractor points

2. **Create Blank Canvas**
   - Initialize a 2D NumPy array filled with zeros.

3. **Generate Attractor Points**
    -  Generate random attractor points within canvas dimensions

4. **Define Distance Function**
    - Compute euclidian distance to attractor point

5. **Generate Pattern**
    - **For** each pixel in canvas_
        - Compute distance to attractor points
        - Apply sine to distances
        - Sum sine values
        - Map normalized values to RGB channels
        - Store values in canvas

6. **Visualize Canvas as Image**
    - matplotlib.pyplot as plt

## Technical Explaination

## Geometric Influences

## Results

## References
