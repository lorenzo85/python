
# Boids try to fly towards the centre of mass of neighbouring boids.
# The center of mass is simply the average position of all the boids except the current one.
# To move it 1% of the way towards the centre we compute pcj - bj.position / 100
from vector import Vector

class BoidsRule1:
    @staticmethod
    def apply(boids, bj):
        pcj = Vector()
        for b in boids:
            if b != bj:
                pcj.sum(b.position)
        pcj = pcj.div(len(boids) - 1)
        return pcj.minus(bj.position).div(100)

class BoidsRule2:
    @staticmethod
    def apply(boids, bj):
        c = Vector()
        for b in boids:
            if b != bj:
                distance = Vector.distance(b.position, bj.position)
                if distance < 5:
                    delta = Vector.s_minus(b.position, bj.position)
                    c.minus(delta)
        return c

class BoidsRule3:
    @staticmethod
    def apply(boids, bj):
        pvj = Vector()
        for b in boids:
            if b != bj:
                pvj.sum(b.velocity)
        pvj.div(len(boids) - 1)
        return pvj.minus(bj.velocity).div(8)

class BoidsRule4:
    @staticmethod
    def apply(boid, xmin, xmax, ymin, ymax):
        v = Vector()
        position = boid.position
        if position.x < xmin:
            v.x = 10
        elif position.x > xmax:
            v.x = -10
        if position.y < ymin:
            v.y = 10
        elif position.y > ymax:
            v.y = -10
        return v

class BoidsRule5:
    @staticmethod
    def apply(boid):
        vlim = 10
        currx = boid.velocity.x
        curry = boid.velocity.y
        if abs(currx) > vlim or abs(curry) > vlim:
            newx = round(currx / abs(currx) * vlim) if currx != 0 else currx
            newy = round(curry / abs(curry) * vlim) if curry != 0 else curry
            boid.velocity = Vector(newx, newy)
