from math import sqrt
from typing import List
import pygame
from DrawEngine import DrawEngine

from Object import Object
from PhisicsEngine import PhisicEngine
from Vector import Vector

FPS = 60


pygame.init()
clock = pygame.time.Clock()

tracks: List[Object] = []

RED = (150, 50, 50)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
YELLOW = (255, 255, 0)

SUN_MASS = 100000

from maps.earth_with_moon import objects

phisics = PhisicEngine(objects, tracks, clock)
draw = DrawEngine(objects, tracks)

is_running: bool = True

is_paused: bool = False

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                draw.zoom_plus()
            if event.button == 5:
                draw.zoom_minus()
            if event.button == 1:
                draw.select(Vector(event.pos[0], event.pos[1]))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_paused = not is_paused


    mouse_motion = pygame.mouse.get_rel()
    pressed_buttons = pygame.mouse.get_pressed()

    if pressed_buttons[2]:
        draw.move_camera(Vector(mouse_motion[0], mouse_motion[1]))

    if not is_paused:
        phisics.update_universe()

    draw.render()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
