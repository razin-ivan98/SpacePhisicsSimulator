from typing import List
from pygame.time import Clock

from Object import Object
from Vector import Vector

G: float = 6.67 * 10 ** (-2)# * 10 ** (-11)

TRACK_TTL = 7000

T = 0.3

class PhisicEngine:
    def __init__(self, objects: List[Object], tracks: List[Object], clock: Clock):
        self.__objects = objects
        self.__tracks = tracks
        self.clock = clock
        self.dt = 0

    def __update_dt(self):
        self.dt = self.clock.get_time()

    # сперва вычисляем ускорение (из гравитационных взаимодействий всех объектов сос всеми)
    def __compute_acceleration(self, obj_to_compute: Object):
        acceleration = Vector(0, 0)
        for obj in self.__objects:
            if obj == obj_to_compute:
                continue
            sub = obj.pos - obj_to_compute.pos
            ort = sub.normalize()
            r = sub.length
            # в формуле отсутствует масса вычисляемого объекта, т к она сокращается
            a = ort * (G * obj.m / r ** 2)
            acceleration += a
        obj_to_compute.a = acceleration

    # позицию вычисляем до скорости, потому что используется начальная скорость
    def __compute_position(self, obj: Object):
        # newPosition = obj.pos + obj.v * 0.01 + (obj.a * 0.01 ** 2) / 2
        # obj.pos = newPosition
        obj.pos += obj.v * T

    def __compute_velocity(self, obj: Object):
        newVelocity = obj.v + obj.a * T# * 0.01
        obj.v = newVelocity

    def __update_object(self, obj: Object):
        if (obj.fixed):
            return
        self.__tracks.append(Object(0, obj.pos, obj.color, ttl=TRACK_TTL))
        self.__compute_acceleration(obj)
        self.__compute_velocity(obj)
        self.__compute_position(obj)
        

    def update_universe(self):
        self.__update_dt()
        for track in self.__tracks:
            track.ttl -= self.dt
        for obj in self.__objects:
            self.__update_object(obj)
