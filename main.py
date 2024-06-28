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

    # window.set_model(Gravitation(6.67430e-11, r_power=2))
    window.set_model(Gravitation(6.67430e-11, r_power=2))

    b1 = Ball(1280 / 2, 720 / 2, 50, 10e15, Color(0, 0, 0), freeze=True)
    b2 = Ball(400, 400, 5, 1, Color(0, 0, 0))
    b3 = Ball(420, 420, 5, 1, Color(0, 0, 0))

    window.add_entity(b1)
    window.add_entity(b2)
    window.add_entity(b3)

    window.entities[1].velocity = Vector2(25, 50)
    window.entities[2].velocity = Vector2(25, 50)
    # effect = Dots(window.screen)
    effect = FreeBodyDiagram(window.screen)

    window.screen.fill((255, 255, 255))

    while window.running:
        window.screen.fill((255, 255, 255))

        window.render_effects([window.entities[1]], [effect])

        window.render()

        window.flip()

        window.model.simulate(window.entities)

        v = Vector2(0, 0)
        for f in b2.forces:
            v += f

        # print(v.magnitude(), b2.acceleration.magnitude() * b2.mass, 1000 * b1.mass * b2.mass / b2.position.distance_squared_to(b1.position))
        window.update()

    window.close()


if __name__ == "__main__":
    gravitation_example()

