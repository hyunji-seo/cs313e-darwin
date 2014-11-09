class Species:
	def __init__(self, name):
		self.instructions = []
		self.name = name

	def get_instruction(self, instructions, program_counter):
		return instructions[program_counter]

	def list_instructions(self):
		return self.instructions

	def add_instruction(self, instructions, program_counter = None):
		# each instruction is a function
		if program_counter != None:
			a = [instructions, program_counter]
		else:
			a = [instructions]
		self.instructions.append(a)
		return self.instructions


class Creature:
	def __init__(self, species, direction, x_cor, y_cor): 

		self.species = species
		self.direction = direction
		self.program_counter = 0
		self.x_cor = x_cor
		self.y_cor = y_cor

	def get_move(self, species, instructions, direction, program_counter):
		count = 0
		if count == 0:
			program_counter = 0
			count += 1
		else:
			program_counter += 1
		return species.get_instruction(instructions, program_counter), direction
	
	def turn(self):
		m = Species.get_instruction()
		Creature.program_counter = 0 
		stop_turn = False
		while stop_turn == False:
			current = m[self.program_counter].split(' ')
			if len(current) > 1:
				if current[0] == "if_wall":
					if_wall(creature_object, creature_grid)
				if current[0] == "if_empty":
					if_empty(creature_object, creature_grid)
				if current[0] == "if_enemy":
					if_enemy(creature_object, creature_grid)
				if current[0] == "if_random":
					if_random()
				if current[0] == "infect":
					infect(creature_object, creature_grid)
			if len(current) < 1:
				if current[0] == "hop":
					hop(creature_object, creature_grid)
				if current[0] == "left":
					left(creature_object, creature_grid)
				if current[0] == "right":
					right(creature_object, creature_grid)
				if current[0] == "go":
					Creature.program_counter += 0 
class Darwin:

	def __init__(self, x, y):
		assert x != 0
		assert y != 0
		self.row = x
		self.col = y
		self.creature_grid = []
		self.display_grid = []
		global r
		r = x
		global c
		c = y
		#self.grid = [["."] * self.col for x in range(self.row)]
		for row in range(0, self.row):
			temp = []	
			for col in range(0, self.col):
				temp.append(Creature(None, None, None, None))
			self.creature_grid.append(temp)

	def print_board(self, display_grid, turn):
		print("Turn = ", str(turn) + ".")
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(display_grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end= " ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))
		print()

	def add_creature(self, species, direction, x_cor, y_cor):
		self.creature_grid[x_cor][y_cor] = Creature(species, direction, x_cor, y_cor)


def hop(creature_object, creature_grid):
	if creature_object.direction == "north":
		if not if_wall(creature_object) and if_empty(creature_object, creature_grid):
			creature_grid[creature_object.x_cor-1][creature_object.y_cor] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor-1, creature_object.y_cor)
			creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)


	if creature_object.direction == "south":
		if not if_wall(creature_object) and if_empty(creature_object, creature_grid):
			creature_grid[creature_object.x_cor+1][creature_object.y_cor] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor+1, creature_object.y_cor)
			creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)

			
	if creature_object.direction == "east":
		if not if_wall(creature_object) and if_empty(creature_object, creature_grid):
			creature_grid[creature_object.x_cor][creature_object.y_cor+1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor+1)
			creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
			

	if creature_object.direction == "west":
		if not if_wall(creature_object) and if_empty(creature_object, creature_grid):
			creature_grid[creature_object.x_cor][creature_object.y_cor-1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor-1)
			creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
					
def left(creature_object, creature_grid):
	if creature_object.direction == "north":
		creature_object.direction == "west"
	if creature_object.direction == "west":
		creature_object.direction == "south"
	if creature_object.direction == "south":
		creature_object.direction == "east"
	if creature_object.direction == "east":
		creature_object.direction == "north"

def right(creature_object, creature_grid):
	if creature_object.direction == "north":
		creature_object.direction == "east"
	if creature_object.direction == "west":
		creature_object.direction == "north"
	if creature_object.direction == "south":
		creature_object.direction == "west"
	if creature_object.direction == "east":
		creature_object.direction == "south"

def infect(creature_object, creature_grid):
	if creature_object.direction == "north":
		if if_enemy(creature_object):
			d = creature_grid[creature_object.x_cor-1][creature_object.y_cor].direction
			creature_grid[creature_object.x_cor-1][creature_object.y_cor] = Creature(creature_object.species, d, creature_object.x_cor-1, creature_object.y_cor)
	if creature_object.direction == "south":
		if if_enemy(creature_object):
			d = creature_grid[creature_object.x_cor+1][creature_object.y_cor].direction
			creature_grid[creature_object.x_cor+1][creature_object.y_cor] = Creature(creature_object.species, d, creature_object.x_cor+1, creature_object.y_cor)
	if creature_object.direction == "east":
		if if_enemy(creature_object):
			d = creature_grid[creature_object.x_cor][creature_object.y_cor+1].direction
			creature_grid[creature_object.x_cor][creature_object.y_cor+1] = Creature(creature_object.species, d, creature_object.x_cor, creature_object.y_cor+1)
	if creature_object.direction == "west":
		if if_enemy(creature_object): 
			d = creature_grid[creature_object.x_cor][creature_object.y_cor-1].direction
			creature_grid[creature_object.x_cor][creature_object.y_cor-1] = Creature(creature_object.species, d, creature_object.x_cor, creature_object.y_cor-1)

def if_wall(creature_object):
	r
	c
	if creature_object.direction == "south" and creature_object.x_cor ==  r:
		return True
	if creature_object.direction == "north" and creature_object.x_cor ==  0:
		return True
	if creature_object.direction == "east" and creature_object.y_cor ==  c:
		return True
	if creature_object.direction == "west" and creature_object.y_cor ==  0:
		return True
	else:
		return False

def if_empty(creature_object, creature_grid):
	if creature_object.direction == "north":
		if not if_wall(creature_object) and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species == None:
			return True
	if creature_object.direction == "south":
		if not if_wall(creature_object) and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species == None:
			return True
	if creature_object.direction == "east":
		if not if_wall(creature_object) and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species == None:
			return True
	if creature_object.direction == "west":
		if not if_wall(creature_object) and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species == None:
			return True
	else:
		return False

def if_random():
	random.seed(0) 
	if random.randrange(0, 2)  % 2 != 0:
		return True
	else:
		return False

def if_enemy(creature_object, creature_grid):
	if creature_object.direction == "north":
		if not if_wall(creature_object) and not if_empty(creature_object, creature_grid) and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species != creature_oject.species:
			return True
	if creature_object.direction == "south":
		if not if_wall(creature_object) and not if_empty(creature_object, creature_grid) and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species != creature_object.species:
			return True
	if creature_object.direction == "east":
		if not if_wall(creature_object) and not if_empty(creature_object, creature_grid) and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species != creature_object.species:
			return True
	if creature_object.direction == "west":
		if not if_wall(creature_object) and not if_empty(creature_object, creature_grid) and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species != creature_object.species:
			return True
	else:
		return False

if __name__ == "__main__":
	turn = 5
	s = Darwin(8,8)
	s.add_creature(Species('hopper'), 'south', 0, 0 )
	#hop(creature_object, creature_grid)
	

	print(if_wall(s.creature_grid[0][0]))
	#for i in s.creature_grid:
	 #	for j in i:
	 #		print (j.species)
	print(s.creature_grid)
