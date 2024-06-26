import utils
from effects.effect import Effect
from pygame import Color


class FreeBodyDiagram(Effect):
    def __init__(self, screen, unit_vector=True, scale=100):
        super().__init__(screen)
        self.scale = scale

    def render(self, entity):
        utils.draw_arrow(self.screen,
                         utils.flip(entity.position, self.screen.get_size()[1]),
                         utils.flip(entity.position + utils.unit_vector(entity.velocity) * self.scale, self.screen.get_size()[1]),
                         Color(0, 255, 0),
                         head_width = 6
        )


        utils.draw_arrow(self.screen,
                 utils.flip(entity.position, self.screen.get_size()[1]),
                 utils.flip(entity.position + utils.unit_vector(entity.acceleration) * self.scale,
                self.screen.get_size()[1]),
                 Color(255, 0, 0),
                head_width=6
             )
