import pygame.draw

from entity.entity import Entity


class Ball(Entity):
    def __init__(self, x, y, radius, mass, color):
        super().__init__(x, y, radius * 2, radius * 2, mass, color)
        self.radius = radius

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, screen.get_size()[1] - self.position.y), self.radius)