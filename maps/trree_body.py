from Object import Object
from Vector import Vector
from math import sqrt

objects: list[Object] = []

RED = (150, 50, 50)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
YELLOW = (255, 255, 0)



G: float = 6.67 * 10 ** (-2)# * 10 ** (-11)

objects.append(Object(1000, Vector(0, 30), YELLOW, 20))
objects.append(Object(1000, Vector(-30, -30), YELLOW, 20))
objects.append(Object(1000, Vector(30, 30), YELLOW, 20))


