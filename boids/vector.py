import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def sum(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def div(self, scalar):
        self.x = round(self.x / scalar)
        self.y = round(self.y / scalar)
        return self

    def minus(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    @staticmethod
    def s_minus(v1, v2):
        vector = Vector()
        vector.x = v1.x - v2.x
        vector.y = v1.y - v2.y
        return vector

    @staticmethod
    def distance(v1, v2):
        delta_x = v2.x - v1.x
        delta_y = v2.y - v1.y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y,2))

    def __repr__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y)