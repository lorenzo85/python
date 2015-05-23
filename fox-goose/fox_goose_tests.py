import unittest
from fox_goose import *

class TestState(unittest.TestCase):

	def test_fox_not_allowed_with_goose(self):
		# Given
		fox = Fox()
		R1 = [Goose()]

		# When
		result = fox.is_allowed(R1)
		
		# Then
		self.assertFalse(result)

	def test_fox_allowed_with_empty_set(self):
		# Given
		fox = Fox()
		R1 = []

		# When
		result = fox.is_allowed(R1)

		# Then
		self.assertTrue(result)

	def test_fox_allowed_with_beans(self):
		# Given
		fox = Fox()
		R1 = [Beans()]

		# When
		result = fox.is_allowed(R1)

		# Then
		self.assertTrue(result)

	def test_fox_allowed_with_boat(self):
		# Given
		fox = Fox()
		R1 = [Boat()]

		# When
		result = fox.is_allowed(R1)

		# Then
		self.assertTrue(result)

	def test_goose_allowed_with_fox(self):
		# Given
		goose = Goose()
		R1 = [Fox()]

		# When
		result = goose.is_allowed(R1)

		# Then
		self.assertTrue(result)

	def test_goose_not_allowed_with_beans(self):
		# Given
		goose = Goose()
		R1 = [Beans()]

		# When
		result = goose.is_allowed(R1)

		# Then
		self.assertFalse(result)

	def test_goose_allowed_with_boat(self):
		# Given
		goose = Goose()
		R1 = [Boat()]

		# When
		result = goose.is_allowed(R1)

		# Then
		self.assertTrue(result)

	def test_allowed_states(self):
		# Given
		states = []
		states.append(State([Fox(), Goose(), Beans(), Boat()], []))
		states.append(State([Goose(), Boat()], [Fox(), Beans()]))

		for state in states:
			# When
			result = state.is_valid()
			# Then
			self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()