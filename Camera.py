from Vector import Vector

class Camera:
    def __init__(self, pos: Vector = Vector(0, 0), scale: float = 1):
        self.pos = pos
        self.scale = scale
