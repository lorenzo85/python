import unittest

from vector import Vector


class TestState(unittest.TestCase):

    def test_sum(self):
        # Given
        vector = Vector()
        vector_to_sum = Vector(2, 3)

        expected_x = vector.x + vector_to_sum.x
        expected_y = vector.y + vector_to_sum.y

        # When
        vector.sum(vector_to_sum)

        # Then
        self.assertEquals(vector.x, expected_x)
        self.assertEquals(vector.y, expected_y)

    def test_minus(self):
        # Given
        vector = Vector(5, 10)
        vector_to_subtract = Vector(1, 2)

        expected_x = vector.x - vector_to_subtract.x
        expected_y = vector.y - vector_to_subtract.y

        # When
        vector.minus(vector_to_subtract)

        # Then
        self.assertEquals(vector.x, expected_x)
        self.assertEquals(vector.y, expected_y)

    def test_div(self):
        # Given
        vector = Vector(15, 20)
        scalar = 5

        expected_x = vector.x / scalar
        expected_y = vector.y / scalar

        # When
        vector.div(scalar)

        # Then
        self.assertEqual(vector.x, expected_x)
        self.assertEqual(vector.y, expected_y)

if __name__ == '__main__':
    unittest.main()