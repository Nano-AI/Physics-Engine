import pygame.time

from window import Window

from entity.ball import Ball

from pygame import Color, Vector2

from models.gravitation import Gravitation

from effects.dots import Dots
from effects.freebodydiagram import FreeBodyDiagram


def gravitation_example():
    window = Window(1280, 720, 120)
    window.init()

    window.set_model(Gravitation(1000))

    b1 = Ball(1280 / 2, 720 / 2, 50, 10e5, Color(0, 0, 0))
    b2 = Ball(400, 400, 5, 10e2, Color(0, 0, 0))

    window.add_entity(b1)
    window.add_entity(b2)

    window.entities[1].velocity = Vector2(25, 50)
    # effect = Dots(window.screen)
    effect = FreeBodyDiagram(window.screen)

    while window.running:
        window.screen.fill((255, 255, 255))

        window.render_effects([window.entities[1]], [effect])

        window.render()

        window.flip()

        window.model.simulate(window.entities)

        window.update()

    window.close()


if __name__ == "__main__":
    gravitation_example()
