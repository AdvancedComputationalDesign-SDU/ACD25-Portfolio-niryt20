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

- [Project Overview](#project-overview)
- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Design Variations](#design-variations)
- [AI Acknowledgments](#ai-acknowledgments)
- [References](#references)


## Project Overview

- Heightmap from assignment 3
- Movement of agents based on proximity of other agents and a curvature factor
- Slope data is stored and agents generate visual representation of slope based on position on a given surface

## Pseudo-Code

1. **Define Agent Class**
    - class Agent
        - distance to other agents
            - curvature veight
            - returns distance weighted with curvature
        - sorted neighbors
            - returns a sorted list of neigboring agents
        - separation
            - Get N nearest neighboring agents
            - compute separation vector
        - agent at edge check
            - if u,v = 0 or 1 kill agent
        - move agent
            - position + velocity 

2. **Build Agents**
    - agents
        - empty list of agents
        - repeat:
            - random UV coordinate
            - create agent at coord
            - add to list of agents
        - return list of agents

3. **Storage**
    - if reset pressed OR no agent list exists:
        - sticky["agents"] = build_agents(surface, N)
    - agents = sticky["agents"]

4. **Simulation**
    - for each agent in agents:
        - if alive:
            - agent.separation(agents, force_intensity, neighbor_count)
    - for each agent in agents:
        - agent.update()
        - agent.check_if_dead()

5. **Visualitation**
    - P = live agent position
    - T = trails polyline
    - TrailPoints = trail points history
    - SlopeValues = all empty lists
    - for each agent: 
        - if agent.alive:
            - convert UV → XYZ
            - add to P
        - if agent.trail has more than 1 point:
            - create polyline from trail
            - add to T
            - for each point in trail:
                - calculate slope from surface normal
                - add slope to SlopeValues
                - add point to TrailPoints

6. **Save updated agents**
    - sticky["agents"] = agents

## Technical Explanation
The heightmap also used in assignment 3 provides an environment where multible agents with different encoded behaviors interact with each other. The Agents' movement between each tick is controlled by their proximity to a set number of close entities. Based on proximity a separation force is generated. When agents reach surface boundary, it is killed. Each tick is recorded via Sticky. Each agent records slope data at their location on the given surface and is thus visualized in grasshopper

## Design Variations

### Variation 1
|Number of agents|Separation force intensity|Neighbor count|Seed|
|----|----|----|----|
|100|0.005|3|42|

![Variation 1](images/Design_1.gif)

### Variation 2
|Number of agents|Separation force intensity|Neighbor count|Seed|
|----|----|----|----|
|100|0.005|10|42|

![Variation 2](images/Design_2.gif)

### Variation 3
|Number of agents|Separation force intensity|Neighbor count|Seed|
|----|----|----|----|
|50|0.01|3|42|

![Variation 3](images/Design_3.gif)

## AI Acknowledgments

# ChatGPT
- Agent Storage: storing information between tics and storing agents' paths was difficult. ChatGPT suggested using sticky when promted.
    - if reset or "agents" not in sc.sticky: sc.sticky["agents"] = build_agents(srf, N)

- Visualization
    - Translating data from inside a python component into something visible in the grasshopper environment often with ChatGPT

## References
- W10 and W11 ACD material.
