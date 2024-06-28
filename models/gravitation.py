from models.model import Model
from math import atan2, sin, cos, pi

from pygame import Vector2

from entity.entity import Entity


class Gravitation(Model):
    def __init__(self, G, r_power = 2):
        super().__init__()
        self.G = G
        self.r_power = r_power

    def simulate(self, entities):
        for i in range(len(entities)):
            for j in range(len(entities)):
                if i == j:
                    continue
                a: Entity = entities[i]
                b: Entity = entities[j]

                r2 = a.position.distance_to(b.position) ** self.r_power

                F = self.G * a.mass * b.mass / r2

                dx = b.position[0] - a.position[0]
                dy = b.position[1] - a.position[1]

                theta = atan2(dy, dx) + 2 * pi

                a.add_force(Vector2(F * cos(theta), F * sin(theta)))

