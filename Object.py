from Vector import Vector

class Object:
    def __init__(
        self,
        m: float,
        pos: Vector,
        color: tuple[int, int, int],
        r: float = 3,
        v: Vector = Vector(0, 0),
        a: Vector = Vector(0, 0),
        fixed: bool = False,
        ttl: int = None
    ):
        self.pos = pos
        self.v = v
        self.a = a
        self.m = m
        self.r = r
        self.color = color
        self.fixed = fixed
        self.ttl = ttl
