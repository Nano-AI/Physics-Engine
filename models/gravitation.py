from models.model import Model
from math import atan2, sin, cos, pi

from pygame import Vector2


class Gravitation(Model):
    def __init__(self, G):
        super().__init__()
        self.G = G

    def simulate(self, entities):
        for i in range(len(entities)):
            for j in range(len(entities)):
                if i == j:
                    continue
                a = entities[i]
                b = entities[j]

                r2 = a.position[0]**2 + b.position[0]**2

                F = self.G * a.mass * b.mass / r2

                dx = b.position[0] - a.position[0]
                dy = b.position[1] - a.position[1]

                theta = atan2(dy, dx) + 2 * pi

                a.add_force(Vector2(F * cos(theta), F * sin(theta)))

