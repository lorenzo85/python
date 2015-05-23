import copy

class Item():
	def is_allowed(self, set):
		exclusion = self.exclusion()
		if exclusion:
			for item in set:
				if type(item) == exclusion and not self.is_boat_present(set):
					return False
		return True

	def exclusion(self):
		return None

	def is_boat_present(self, set):
		return list(filter(lambda item: type(item) is Boat, set))

class Fox(Item):
	def exclusion(self):
		return Goose

	def __repr__(self):
		return "Fox"

class Goose(Item):
	def exclusion(self):
		return Beans

	def __repr__(self):
		return "Goose"

class Beans(Item):
	def __repr__(self):
		return "Beans"

class Boat(Item):
	def __repr__(self):
		return "Boat"

class State:
	def __init__(self, R1, R2):
		self.R1 = R1
		self.R2 = R2

	def __str__(self):
		return "R1: {}, R2: {}".format(str(self.R1), str(self.R2))

	def __eq__(self, other):
		r1 = filter(lambda el: not self.is_el_in_set(el, other.R1), self.R1)
		r2 = filter(lambda el: not self.is_el_in_set(el, other.R2), self.R2)
		return not list(r1) and not list(r2)

	def is_valid(self):
		r1 = filter(lambda item: not item.is_allowed(self.R1), self.R1)
		r2 = filter(lambda item: not item.is_allowed(self.R2), self.R2)
		return not list(r1) and not list(r2)

	def is_el_in_set(self, el, set):
		return list(filter(lambda item: type(item) == type(el), set))

	def get_boat(self, set):
		boat = list(filter(lambda el: type(el) is Boat, set))
		return boat.pop() if boat else None

	# Move the Item, if it is not a Boat than move the Boat as well.
	def move(self, to_move, src, dst):
		for el in src:
			if type(el) == type(to_move):
				src.remove(el)
				dst.append(el)
				if type(el) is not Boat:
					the_boat = self.get_boat(src)
					src.remove(the_boat)
					dst.append(the_boat)

	# Generates next valid states combinations starting from the current state
	def generate_next_states(self):
		generated = []
		if self.get_boat(self.R1):
			for item in self.R1:
				new_state = copy.deepcopy(self)
				new_state.move(item, new_state.R1, new_state.R2)
				generated.append(new_state)
		else:
			for item in self.R2:
				new_state = copy.deepcopy(self)
				new_state.move(item, new_state.R2, new_state.R1)
				generated.append(new_state)
		return filter(lambda x: x.is_valid(), generated)

def pretty_print(path):
	for state in path:
		print(state)

def not_already_visited(path, state):
	return not list(filter(lambda s: s.__eq__(state), path))

def find_next_paths_solutions(valid_paths):
	new_valid_paths = []
	for path in valid_paths:
		last_state = path[-1]
		generated_states = last_state.generate_next_states()
		generated_states = filter(lambda x: not_already_visited(path, x), generated_states)
		for state in generated_states:
			new_valid_paths.append(path + [state])
	return new_valid_paths

def is_solution(path):
	return not path[-1].R1

if __name__ == "__main__":
	valid_paths = [[State([Boat(), Fox(), Goose(), Beans()], [])]]
	solutions = []

	while not solutions:
		next_paths = find_next_paths_solutions(valid_paths)
		valid_paths = []
		for path in next_paths:
			if is_solution(path):
				solutions.append(path)
			else:
				valid_paths.append(path)
	
	for solution in solutions:
		print("---- Solution ----")
		pretty_print(solution)