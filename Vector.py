class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.__length: float = None
    
    def __str__(self):
        return "Vector: x = " + str(self.x) + ", y = " + str(self.y)

    def __mul__(self, other):
        if (type(other) == float or type(other) == int):
            return Vector(self.x * other, self.y * other)
        raise Exception("Вы можете умножить вектор лишь на число")
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if (type(other) == float or type(other) == int):
            return Vector(self.x / other, self.y / other)
        raise Exception("Вы можете разделить вектор лишь на число")

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise Exception("Вы не можете сложить вектор и не вектор")

    def __iadd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise Exception("Вы не можете вычесть не вектор из вектора")

    @property
    def length(self):
        if  self.__length != None:
            return self.__length
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        self.__length = length
        return length

    def normalize(self):
        return Vector(self.x / self.length, self.y / self.length)
