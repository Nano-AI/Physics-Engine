import pygame

from models.kinematics import Kinematics


class Window:
    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = None
        self.running = False
        self.entities = []
        self.model = Kinematics(-9.8)
        self.fps = FPS
        self.dt = 0

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

    def render(self):
        height = self.screen.get_size()[1]

        for e in self.entities:
            e.render(self.screen)
            # draw_arrow(self.screen, Vector2(0, height) - e.position, Vector2(0, height) - (e.position + e.acceleration), Color(0, 0, 255))
            # draw_arrow(self.screen, flip(e.position, height), flip(e.position + 100 * e.acceleration, height), Color(0, 0, 255))


        self.dt = self.clock.tick(self.fps) / 1000

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        for e in self.entities:
            e.update(self.dt)

    def close(self):
        pygame.quit()

    def add_entity(self, entity):
        self.entities.append(entity)

    def set_model(self, model=Kinematics(-9.8)):
        self.model = model

    def flip(self):
        pygame.display.flip()

    def render_effects(self, entities, effects):
        for effect in effects:
            for entity in entities:
                effect.render(entity)
