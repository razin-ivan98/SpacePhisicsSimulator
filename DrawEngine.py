from typing import List

import pygame
from Camera import Camera
from Object import Object
from Vector import Vector

W = 1000
H = 500

W_2 = W / 2
H_2 = H / 2

DARKBLUE = (0, 2, 25)

class DrawEngine:
    def __init__(self, objects: List[Object], tracks: List[Object]):
        self.__camera = Camera()
        self.__objects = objects
        self.__tracks = tracks
        self.__sc = pygame.display.set_mode((W, H))
        self.__selected: Object = None

    def __screen_coords_to_pixel_pos(self, coords: Vector):
        return Vector(round(W_2 + coords.x), round(H_2 + coords.y))

    def __pixel_pos_to_screen_coords(self, pos: Vector):
        return Vector(round(-W_2 + pos.x), round(-H_2 + pos.y))

    def __point_to_pixel_pos(self, point: Vector):
        translated = point - Vector(self.__camera.pos.x, self.__camera.pos.y)
        scaled = translated * self.__camera.scale
        pixel_pos = self.__screen_coords_to_pixel_pos(scaled)
        return pixel_pos

    def __pixel_pos_to_point(self, pixel_pos: Vector):
        screen_coords = self.__pixel_pos_to_screen_coords(pixel_pos)
        descaled = screen_coords / self.__camera.scale
        pos = descaled + Vector(self.__camera.pos.x, self.__camera.pos.y)
        
        return pos

    def __project_and_render_object(self, obj: Object):
        screen_pos = self.__point_to_pixel_pos(obj.pos)
        newR = obj.r * self.__camera.scale

        pygame.draw.circle(self.__sc, obj.color, (screen_pos.x, screen_pos.y), newR, 0)

    def __project_and_render_track(self, track: Object):
        screen_pos = self.__point_to_pixel_pos(track.pos)

        # self.__sc.fill(track.color, (screen_pos.x, screen_pos.y, 1, 1))
        pygame.draw.circle(self.__sc, track.color, (screen_pos.x, screen_pos.y), 1, 0)

    def __get_object_by_pos(self, pos: Vector):
        for obj in  self.__objects:
            if (obj.pos - pos).length < obj.r:
                return obj
        return None

    def render(self):
        self.__sc.fill(DARKBLUE)

        # camera update

        if self.__selected:
            self.__camera.pos = self.__selected.pos

        for track in self.__tracks:
            if track.ttl != None and track.ttl < 0:
                self.__tracks.remove(track)
            self.__project_and_render_track(track)
        for obj in self.__objects:
            self.__project_and_render_object(obj)

    def move_camera(self, d: Vector):
        self.__selected = None
        self.__camera.pos -= d / self.__camera.scale

    def zoom_plus(self):
        self.__camera.scale *= 1.1
        mouse_pos = Vector()
        mouse_pos.x, mouse_pos.y = pygame.mouse.get_pos()
        mouse_screen_coords = self.__pixel_pos_to_screen_coords(mouse_pos)
        self.__camera.pos += Vector(mouse_screen_coords.x, mouse_screen_coords.y) / self.__camera.scale * 0.1

    def zoom_minus(self):
        mouse_pos = Vector()
        mouse_pos.x, mouse_pos.y = pygame.mouse.get_pos()
        mouse_screen_coords = self.__pixel_pos_to_screen_coords(mouse_pos)
        self.__camera.pos -= Vector(mouse_screen_coords.x, mouse_screen_coords.y) / self.__camera.scale * 0.1
        self.__camera.scale /= 1.1

    def select(self, mouse_pos: Vector):
        pos = self.__pixel_pos_to_point(mouse_pos)
        print(pos)
        self.__selected = self.__get_object_by_pos(pos)
        print(self.__selected)
