from threading import Thread
import random
from boidsrules import *
from vector import Vector

BOIDS_NUMBER = 10
MAX_SPEED = 10

class Boid:
    def __init__(self, position, velocity, name):
        self.position = position
        self.velocity = velocity
        self._name = name

    def __repr__(self):
        return "Boid #" + self._name + "[Pos: " + str(self.position) + "], [Vel: " + str(self.velocity) + "]"

class BoidsModel(Thread):
    boids = []

    def __init__(self, thread_events, data_transfer, width, height):
        super().__init__()
        self._thread_events = thread_events
        self._data_transfer = data_transfer
        self._width = width
        self._height = height
        self._scatter = False
        self.init_boids()

    def init_boids(self):
        for x in range(BOIDS_NUMBER):
            boid = self.random_boid()
            self.boids.append(boid)

    def random_boid(self):
        pos_v1 = random.randint(0, self._width)
        pos_v2 = random.randint(0, self._height)
        vel_v1 = random.randint(1, MAX_SPEED)
        vel_v2 = random.randint(1, MAX_SPEED)
        return Boid(Vector(pos_v1, pos_v2), Vector(vel_v1, vel_v2), str(random.randint(0, 2000)))

    def move_boids_to_new_positions(self):
        for boid in self.boids:
            v1 = BoidsRule1.apply(self.boids, boid)
            v2 = BoidsRule2.apply(self.boids, boid)
            v3 = BoidsRule3.apply(self.boids, boid)
            v4 = BoidsRule4.apply(boid, 0, self._width, 0, self._height)

            if self._scatter:
                boid.velocity.minus(v1)
            else:
                boid.velocity.sum(v1)

            boid.velocity.sum(v2).sum(v3).sum(v4)
            BoidsRule5.apply(boid)
            boid.position = boid.position.sum(boid.velocity)

    def on_scatter(self):
        print("On scatter")
        self._scatter = not self._scatter

    def map_data_structure(self):
        config = []
        for boid in self.boids:
            position = boid.position
            config.append((position.x, position.y))
        return config

    def run(self):
        while not self._thread_events.is_set():
            # Update boids state
            self.move_boids_to_new_positions()

            # Publish boids state after converting to suitable structure
            self._data_transfer.publish(self.map_data_structure())

            # Wait according to FPS
            self._thread_events.wait(0.06)
