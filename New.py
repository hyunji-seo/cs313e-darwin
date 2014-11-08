from random import randint, sample, seed

class Species:
	def __init__(self, name):
		self.instructions = []
		self.c_id = name

	def get_instruction(self, instructions, program_counter):
		return instructions[program_counter]

	def list_instructions(self):
		return self.instructions

	def add_instruction(self, instructions):
		# each instruction is a function
		[a] = [instructions]
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
		return species.get_instruction(species, instructions, program_counter), direction

class Darwin:
	def __init__(self, x, y):
		assert x != 0
		assert y != 0
		self.row = x
		self.col = y
		global r
		r = x
		global c
		c = y
		self.display_grid = [["."] * self.col for x in range(self.row)]
		self.creature_grid = []
		for row in range(0, self.row):
			temp = []	
			for col in range(0, self.col):
				temp.append(Creature(None, None, None, None))
			self.creature_grid.append(temp)

	def display(self, display_grid, turn):
		print("Turn =", str(turn) + ".")
		print("  " + "".join("{0:d}".format(i) for i in range(len(display_grid[0]))))
		for i, row in enumerate(display_grid, 0):
			print("{0:d}".format(i%10),end= " ")
			print("".join("{0}".format(col if col != None else ".") for col in row))
		print()


	def add_creature(self, creature): # may delete direction and x_cor, y_cor
	#	self.creature_grid[x_cor][y_cor] = Creature(species, direction, creature.x_cor, creature.y_cor)
		x_cor = creature.x_cor
		y_cor = creature.y_cor
		self.creature_grid[x_cor][y_cor]
	#	self.creature_grid



	"""
	def turn(self, creature_grid):
		c_species = self.species
		self.program_counter = 0 
		stop_turn = False
		count = 0
		while stop_turn == False:
			for inst in c_species.instructions:
				current = inst[self.program_counter].split(' ')
				if len(current) > 1:
					if current[0] == "if_wall":
						if_wall(self, creature_grid)
						count += 1
					elif current[0] == "if_empty":
						if_empty(self, creature_grid)
					if count > 0:
						program_counter += 1
						get_instruction
					return species.get_instruction(species, instructions, program_counter), direction
					stop_turn = True
		return stop_turn
	"""

def hop(creature_object, creature_grid):
	
	if creature_object.direction == "north" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor-1][creature_object.y_cor] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor-1, creature_object.y_cor)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
	
	if creature_object.direction == "south" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor+1][creature_object.y_cor] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor+1, creature_object.y_cor)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)

	if creature_object.direction == "east" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor+1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor+1)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
	
	if creature_object.direction == "west" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor-1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor-1)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)


def left(creature_object):
	if creature_object.direction == "north":
		creature_object.direction = "west"
	elif creature_object.direction == "west":
		creature_object.direction = "south"
	elif creature_object.direction == "south":
		creature_object.direction = "east"
	elif creature_object.direction == "east":
		creature_object.direction = "north"

def right(creature_object):
	if creature_object.direction == "north":
		creature_object.direction = "east"
	elif creature_object.direction == "west":
		creature_object.direction = "north"
	elif creature_object.direction == "south":
		creature_object.direction = "west"
	elif creature_object.direction == "east":
		creature_object.direction = "south"
	
def if_wall(creature_object):
	r
	c
	# True = there's a wall ahead
	if creature_object.direction == "south" and creature_object.x_cor+1 ==  r:
		return True
	if creature_object.direction == "north" and creature_object.x_cor-1 < 0:
		return True
	if creature_object.direction == "east" and creature_object.y_cor+1 ==  c:
		return True
	if creature_object.direction == "west" and creature_object.y_cor-1 <  0:
		return True
	else:
		return False

def if_empty(creature_object, creature_grid):
	if creature_object.direction == "north" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species == None:
		return True
	if creature_object.direction == "south" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species == None:
		return True

	if creature_object.direction == "east" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species == None:
		return True

	if creature_object.direction == "west" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species == None:
		return True
	else:
		return False


def if_enemy(creature_object, creature_grid):
	if creature_object.direction == "north" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species != creature_object.species:
		return True
	
	if creature_object.direction == "south" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species != creature_object.species:
		return True
	
	if creature_object.direction == "east" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species != creature_object.species:
		return True
	
	if creature_object.direction == "west" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species != creature_object.species:
		return True

	else:
		return False


def infect(creature_object, creature_grid):
	
	if creature_object.direction == "north" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor-1][creature_object.y_cor].direction
		creature_grid[creature_object.x_cor-1][creature_object.y_cor] = Creature(creature_object.species, d, creature_object.x_cor-1, creature_object.y_cor)
	
	if creature_object.direction == "south" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor+1][creature_object.y_cor].direction
		creature_grid[creature_object.x_cor+1][creature_object.y_cor] = Creature(creature_object.species, d, creature_object.x_cor+1, creature_object.y_cor)
	
	if creature_object.direction == "east" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor][creature_object.y_cor+1].direction
		creature_grid[creature_object.x_cor][creature_object.y_cor+1] = Creature(creature_object.species, d, creature_object.x_cor, creature_object.y_cor+1)
	
	if creature_object.direction == "west" and if_enemy(creature_object, creature_grid): 
		d = creature_grid[creature_object.x_cor][creature_object.y_cor-1].direction
		creature_grid[creature_object.x_cor][creature_object.y_cor-1] = Creature(creature_object.species, d, creature_object.x_cor, creature_object.y_cor-1)

def if_random():
	seed(0) 
	if randint(0, 2)  % 2 != 0:
		return True
	else:
		return False


