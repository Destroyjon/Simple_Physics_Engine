import pygame
import random
import time
from mover import mover
from jsLib import Vector, mean


WIDTH, HEIGHT = 700, 700
midX, midY = WIDTH / 2, HEIGHT / 2
WHITE = (255, 255, 255)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


def population(count: int):
    mover_pop = []
    for i in range(count):
        i = mover(random.randint(0, WIDTH), 250, 0, random.uniform(5, 10))
        i.setColor((random.randint(50, 150), random.randint(50, 150), random.randint(50, 150)))
        mover_pop.append(i)
    return mover_pop


gravity = Vector(0, 0)
wind = Vector()

movers = population(10)


def draw_window():
    start_time = time.time()

    DISPLAY.fill(WHITE, None, 5)
    global wind
    global gravity

    if pygame.mouse.get_pressed(3) == (1, 0, 0):
        # wind = Vector(0.01, -0.1)
        gravity = Vector(0, -1)
    else:
        wind = Vector()
        gravity = Vector(0, 0)

    for i in range(len(movers)):
        weight = gravity * movers[i].mass
        # movers[i].collision(movers)
        movers[i].applyforce(weight)
        movers[i].applyforce(wind)
        movers[i].friction(HEIGHT)
        movers[i].edges()
        movers[i].show(DISPLAY)
        movers[i].update()

    pygame.display.update()


def main_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


main_loop()
