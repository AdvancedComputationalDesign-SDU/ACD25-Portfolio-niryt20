"""
Assignment 4: Agent-Based Model for Surface Panelization

Author: Nikolaj Rytter

Agent Builder and simulator

Description:
Defines the core Agent class and factory methods for constructing an
agent-based system. Provides a high-level OOP structure for sensing,
decision-making. 

Note: Both agent builder and simulator is part of the same grasshopper component. therfore agent_simulator is empty.
This script is intended to be used within Grasshopper's Python scripting component.
"""

## Imported libraries
import scriptcontext as sc
import rhinoscriptsyntax as rs
import random
import numpy as np
import Rhino.Geometry as rg


## Core agent class
class Agent:
    def __init__(self, srf, position):
        self.Position = position
        self.velocity = [0, 0, 0]
        self.srf = srf
        self.local_curvature = 1
        self.point = []
        self.alive = True

    def dist(self, agent):
        curvature_factor = np.interp(agent.local_curvature, [-0.015, 0.015], [1, 5])
        return rs.Distance(self.Position, agent.Position) * curvature_factor
    
    def sorted_neighbors(self, agents):
        return sorted(agents, key=self.dist)
    
    def separation(self, agents, force_intensity, n):
        self.velocity = [0, 0, 0]
        sorted_neighbors = self.sorted_neighbors(agents)

        for i in range(min(n, len(sorted_neighbors))):
            agent = sorted_neighbors[i]
            if agent == self:
                continue

            distance_vec = rs.VectorCreate(self.Position, agent.Position)
            if rs.VectorLength(distance_vec) == 0:
                distance_vec = [random.uniform(-1, 1),
                                random.uniform(-1, 1),
                                0]

            inverse_dist = np.interp(
                rs.VectorLength(distance_vec),
                [0, 1],
                [force_intensity, 0]
            )

            inverse_distance_vec = rs.VectorUnitize(distance_vec)
            inverse_distance_vec = rs.VectorScale(inverse_distance_vec, inverse_dist)

            self.velocity = rs.VectorAdd(self.velocity, inverse_distance_vec)

    def check_if_dead(self):
        u, v = self.Position[0], self.Position[1]

        if u <= 0 or u >= 1 or v <= 0 or v >= 1:
            self.alive = False

    def update(self):

        if not self.alive:
            return 

        # Move in UV (0-1)
        self.Position = rs.VectorAdd(self.Position, self.velocity)
        self.Position = np.clip(list(self.Position), 0, 1).tolist()

        # Convert UV→3D and store in point
        scaled_u = self.Position[0] * rs.SurfaceDomain(self.srf, 0)[1]
        scaled_v = self.Position[1] * rs.SurfaceDomain(self.srf, 1)[1]

        pt3d = rs.EvaluateSurface(self.srf, scaled_u, scaled_v)

        # Store the point
        self.point.append(pt3d)

        # Update curvature at new spot
        scaled_u = self.Position[0] * rs.SurfaceDomain(self.srf, 0)[1]
        scaled_v = self.Position[1] * rs.SurfaceDomain(self.srf, 1)[1]
        self.local_curvature = rs.SurfaceCurvature(self.srf, (scaled_u, scaled_v))[6]


## Factory for creating agents

def build_agents(srf, num_agents):
    agents = []
    for _ in range(num_agents):
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        point = [u, v]
        ag = Agent(srf, point)
        agents.append(ag)
    return agents

##Agent Storage
if reset or "agents" not in sc.sticky:
    sc.sticky["agents"] = build_agents(srf, N)

agents = sc.sticky["agents"]

## agent simulation tick updates
for ag in agents:
    if ag.alive:
        ag.separation(agents, force_intensity, neighbor_count)

for ag in agents:
    ag.update()
    ag.check_if_dead()

## Visualization (in grasshopper)

P = []           # live agent positions
T = []           # ALL trails (alive & dead)
TrailPoints = [] # flattened points
SlopeValues = []

vertical = rg.Vector3d(0, 0, 1)

for ag in agents:

    if ag.alive:
        u = ag.Position[0] * rs.SurfaceDomain(srf, 0)[1]
        v = ag.Position[1] * rs.SurfaceDomain(srf, 1)[1]
        pt3d = rs.EvaluateSurface(srf, u, v)
        P.append(pt3d)

    
    if len(ag.point) > 1:
        poly = rg.Polyline(ag.point)
        T.append(rg.PolylineCurve(poly))

        for p in ag.point:
            TrailPoints.append(p)

            uv = rs.SurfaceClosestPoint(srf, p)
            if uv:
                normal = rs.SurfaceNormal(srf, uv)
                if normal:
                    angle = rg.Vector3d.VectorAngle(normal, vertical)
                    SlopeValues.append(angle)
                else:
                    SlopeValues.append(0.0)
            else:
                SlopeValues.append(0.0)

sc.sticky["agents"] = agents