from pygame import Vector2
import pygame


class Entity:
    def __init__(self, x, y, width, height, mass, color, effects=None):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.forces = []
        self.mass = 0

        self.width = width
        self.height = height

        self.mass = mass
        self.effects = effects

        r, g, b, _ = color
        self.color = pygame.Color(r, g, b)

    def update(self, deltaT):
        self.acceleration = Vector2(0, 0)
        for force in self.forces:
            # print(type(force), type(force / self.mass * deltaT), type(self.acceleration))
            # print(force)
            self.acceleration += force / self.mass * deltaT

        self.forces.clear()

        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT

    def render_effect(self):
        if self.effects is None:
            return
        for effect in self.effects:
            effect.render(self)

    def render(self, screen):
        pass

    def add_force(self, force: Vector2):
        self.forces.append(force)
