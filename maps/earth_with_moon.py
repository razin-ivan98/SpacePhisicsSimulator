from Object import Object
from Vector import Vector
from math import sqrt

objects: list[Object] = []

RED = (150, 50, 50)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
YELLOW = (255, 255, 0)

SUN_MASS = 100000

G: float = 6.67 * 10 ** (-2)# * 10 ** (-11)

# objects.append(Object(SUN_MASS / 2, Vector(0, 30), YELLOW, 20, Vector(-sqrt(G * SUN_MASS / 2 / 2.5 / 30)), fixed=False))
# objects.append(Object(SUN_MASS / 2, Vector(0, -30), YELLOW, 20, Vector(sqrt(G * SUN_MASS / 2 / 2.5 / 30)), fixed=False))


objects.append(Object(SUN_MASS, Vector(0, 0), YELLOW, 50, fixed=False))





objects.append(Object(10, Vector(0, 100), BLUE, 7, Vector(sqrt(G * SUN_MASS / 100))))
objects.append(Object(0.01, Vector(0, 80), BLUE, 3, Vector(sqrt(G * SUN_MASS / 80)) * 1.1))
objects.append(Object(1, Vector(0, 150), YELLOW, 5, Vector(sqrt(G * SUN_MASS / 150))))

objects.append(Object(1000, Vector(0, 200), GREEN, 6, Vector(sqrt(G * SUN_MASS / 200))))
objects.append(Object(0.0000000001, Vector(0, 210), RED, 2, Vector(sqrt(G * SUN_MASS / 210) * 1.35)))


# T = 0.1