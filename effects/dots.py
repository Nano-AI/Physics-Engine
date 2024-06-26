from effects.effect import Effect
import pygame
from utils import flip


class Dots(Effect):
    def __init__(self, screen, interval=100, limit=1000000, radius=7, color=(255, 0, 0)):
        super().__init__(screen)
        self.dots = []
        self.radius = radius
        self.limit = limit
        self.color = color
        self.screen = screen
        self.last_dot = pygame.time.get_ticks()
        self.interval = interval

    def render(self, entity):
        if pygame.time.get_ticks() - self.last_dot < self.interval:
            return
        self.last_dot = pygame.time.get_ticks()
        if entity.velocity.magnitude() != 0:
            self.dots.append([pygame.time.get_ticks(), entity.position])
        i = 0
        while i < len(self.dots):
            dot = self.dots[i][1]
            pygame.draw.circle(self.screen, self.color, flip(dot, self.screen.get_size()[1]), self.radius)

            if pygame.time.get_ticks() - self.dots[0][0] >= self.limit:
                self.dots.pop(i)
                i -= 1

            i += 1

        # if len(self.dots) >= self.limit:
        #     self.dots.pop(0)
