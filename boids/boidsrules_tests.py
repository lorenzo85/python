import unittest

from vector import Vector
from boids import Boid
from boidsrules import BoidsRule1


class TestState(unittest.TestCase):
    def test_rule_1(self):
        # Given
        pos_bj = Vector(2, 3)
        pos_b1 = Vector(5, 6)
        pos_b2 = Vector(12, 4)

        boidj = Boid(pos_bj, Vector(4, 5), "Boid 1")
        boid1 = Boid(pos_b1, Vector(1, 2), "Boid 2")
        boid2 = Boid(pos_b2, Vector(5, 6), "Boid 3")
        boids = [boid1, boid2, boidj]

        pcjv1 = (pos_b1.x + pos_b2.x) / (len(boids) - 1)
        pcjv2 = (pos_b1.y + pos_b2.y) / (len(boids) - 1)
        expected_vector = Vector(pcjv1, pcjv2).minus(pos_bj).div(100)

        # When
        result = BoidsRule1.apply(boids, boidj)

        # Then
        self.assertEquals(expected_vector.x, result.x)
        self.assertEquals(expected_vector.y, result.y)

if __name__ == '__main__':
    unittest.main()
