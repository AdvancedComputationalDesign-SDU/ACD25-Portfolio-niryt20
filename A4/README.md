---
layout: default
title: Project Documentation
parent: "A4: Agent-Based Modeling for Surface Panelization"
nav_order: 2
nav_exclude: false
search_exclude: false
---

# Assignment 4: Agent-Based Modeling for Surface Panelization

[View on GitHub]({{ site.github.repository_url }})

## Table of Contents

- [Objective](#objective)
- [Project Overview](#project-overview)
- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Design Variations](#design-variations)
- [AI Acknowledgments](#ai-acknowledgments)
- [References](#references)

## Objective

In this assignment, you will develop an **agent-based system for surface rationalization** using **Object-Oriented Programming (OOP)** in Python. Building on the surface you generated in Assignment 3 (or a comparable heightmap-driven surface), you will design agents that respond to geometric signals and collectively produce **panelization patterns**. The core idea is that agents move, interact, and make decisions based on how they sample the geometry, and their trajectories and interactions become the basis for a rationalized panelization of that surface.

Your implementation must incorporate **at least two types of geometric signals** (chosen from curvature, slope, vector fields, scalar fields, and spatial influences) when defining agent behavior. The primary outputs of this assignment are: (1) a rationalized panelization of your surface and (2) simulated agent trajectories and fields that you document and analyze.

## Project Overview

- Heightmap from assignment 3
- Movement of agents based on proximity of other agents and a curvature factor
- Slope data is stored and agents generate visual representation of slope based on position on a given surface

## Pseudo-Code

### Agent Class
class Agent
    distance to other agents
        curvature veight
        returns distance weighted with curvature

    sorted neighbors
        returns a sorted list of neigboring agents

    separation
        Get N nearest neighboring agents
        compute separation vector
    
    agent at edge check
        if u,v = 0 or 1 kill agent
    
    move agent
        position + velocity 

### Build Agents
 agents
    empty list of agents
    repeat:
        random UV coordinate
        create agent at coord
        add to list of agents
    return list of agents

### Storage
if reset pressed OR no agent list exists:
    sticky["agents"] = build_agents(surface, N)

agents = sticky["agents"]

### simulation
for each agent in agents:
    if alive:
        agent.separation(agents, force_intensity, neighbor_count)

for each agent in agents:
    agent.update()
    agent.check_if_dead()

### Visualitation

P = live agent position
T = trails polyline
TrailPoints = trail points history
SlopeValues = all empty lists

for each agent:
    
    if agent.alive:
        convert UV → XYZ
        add to P
    
    if agent.trail has more than 1 point:
        create polyline from trail
        add to T

        for each point in trail:
            calculate slope from surface normal
            add slope to SlopeValues
            add point to TrailPoints

### save updated agents
sticky["agents"] = agents


## Repository Structure

```
A4/
├── index.md                    # Do not edit front matter or content
├── README.md                   # Project documentation; Keep front matter, replace the rest with your project documentation
├── BRIEF.md                    # Assignment brief; Do not edit front matter or content
├── agent_panelization.gh       # Your grasshopper definition
├── surface_generator.py        # Your surface_generator implementation
├── agent_builder.py            # Your agent_builder implementation
├── agent_simulator.py          # Your agent_simulator implementation
├── ...                         # Any additional implementation
└── images/                     # Add diagram, intermediary, and final images here
    ├── agent_based.png         # Assignment brief image; Do not delete
    └── ...
```
---