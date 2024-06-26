from pygame import Vector2
from models.model import Model

"""
setup:
window.set_model(Kinematics(GRAVITY))

update:
window.mode.simulate(window.entities)
"""


class Kinematics(Model):
    def __init__(self, g):
        super().__init__()
        self.g = g

    def simulate(self, entities):
        for e in entities:
            e.acceleration.y += self.g
