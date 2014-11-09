from random import randint, sample, seed

class Species:
	def __init__(self, name):
		self.instructions = []
		self.c_id = name
		assert self.instructions == []

	def get_instruction(self, instructions, index):
		return instructions[index]

	def add_instruction(self, instructions):
		[a] = [instructions]
		self.instructions.append(a)
		return self.instructions

class Creature:
	def __init__(self, species, direction, x_cor, y_cor): 
		self.species = species
		self.direction = direction
		self.program_counter = 0		
		self.index = 0
		self.x_cor = x_cor
		self.y_cor = y_cor

	def turn(self, creature_grid):
		c_species = self.species
		self.program_counter = 0 
		stop_turn = False
		while stop_turn == False:
			for item in c_species.instructions:
				self.program_counter += 1
				current = item.split(' ')
				# control instructions
				if len(current) > 1:
					if current[0] == "if_wall":
						self.program_counter = int(current[1])
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "if_empty":
						self.program_counter = int(current[1])
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "if_enemy":
						self.program_counter = int(current[1])
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "if_random":
						self.program_counter = int(current[1])
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "go":
						self.program_counter = int(current[1])
						c_species.get_instruction(c_species.instructions, self.program_counter)
				# action instructions
				if len(current) == 1:
					if current[0] == "hop":
						hop(self, creature_grid)
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "left":
						left(self, creature_grid)
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "right":
						right(self, creature_grid)
						c_species.get_instruction(c_species.instructions, self.program_counter)
					if current[0] == "infect":
						infect(self, creature_grid)
						c_species.get_instruction(c_species.instructions, self.program_counter)
					stop_turn = True
		assert stop_turn == True
		return stop_turn

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

	def print_board(self, display_grid, creature_grid, turn):
		for i in range(0, self.row):
			for j in range(0, self.col):
				if creature_grid[i][j].species == None:
					display_grid[i][j] = '.'
				else:
					display_grid[i][j] = creature_grid[i][j].species.c_id

		print("Turn =", str(turn) + ".")
		print("  " + "".join("{0:d}".format(i%10) for i in range(len(display_grid[0]))))
		for i, row in enumerate(display_grid, 0):
			print("{0:d}".format(i%10),end= " ")
			print("".join("{0}".format(col if col != '1' else ".") for col in row))
		print()
		
		for i in range(0, self.row):
			for j in range(0, self.col):
				if creature_grid[i][j].species == None:
					display_grid[i][j] = '.'
				else:
					display_grid[i][j] = creature_grid[i][j].species.c_id
		return self.display_grid

	def master_turn(self, turn, list_creat):
		for x in range(0, turn):
			self.print_board(self.display_grid, self.creature_grid, x)
			for creat in list_creat:
				if creat.turn(self.creature_grid) == True:
					self.creature_grid
					self.display_grid	

	def add_creature(self, creature): 
		x_cor = creature.x_cor
		y_cor = creature.y_cor
		self.creature_grid[x_cor][y_cor] = creature


# ======================== INSTRUCTIONS ============================
def hop(creature_object, creature_grid):
	if creature_object.direction == "north" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor-1][creature_object.y_cor] = creature_grid[creature_object.x_cor][creature_object.y_cor]
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.x_cor -= 1
	if creature_object.direction == "south" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor+1][creature_object.y_cor] = creature_grid[creature_object.x_cor][creature_object.y_cor]
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.x_cor+=1
	if creature_object.direction == "east" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor+1] = creature_grid[creature_object.x_cor][creature_object.y_cor]
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.y_cor+=1
	if creature_object.direction == "west" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor-1] = creature_grid[creature_object.x_cor][creature_object.y_cor]
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.y_cor-=1

def left(creature_object, creature_grid):
	if creature_object.direction == "north":
		creature_object.direction = "west"
	elif creature_object.direction == "west":
		creature_object.direction = "south"
	elif creature_object.direction == "south":
		creature_object.direction = "east"
	elif creature_object.direction == "east":
		creature_object.direction = "north"

def right(creature_object, creature_grid):
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
	#print(creature_object.direction, if_wall(creature_object))
	if creature_object.direction == "north" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species != creature_object.species and creature_grid[creature_object.x_cor-1][creature_object.y_cor].species != None:
		return True
	if creature_object.direction == "south" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species != creature_object.species and creature_grid[creature_object.x_cor+1][creature_object.y_cor].species != None:
		return True
	if creature_object.direction == "east" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species != creature_object.species and creature_grid[creature_object.x_cor][creature_object.y_cor+1].species != None:
		return True
	if creature_object.direction == "west" and if_wall(creature_object) == False and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species != creature_object.species and creature_grid[creature_object.x_cor][creature_object.y_cor-1].species != None:
		return True
	else:

		return False

def infect(creature_object, creature_grid):
	if creature_object.direction == "north" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor-1][creature_object.y_cor].direction
		creature_grid[creature_object.x_cor-1][creature_object.y_cor].species = creature_grid[creature_object.x_cor][creature_object.y_cor].species
	if creature_object.direction == "south" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor+1][creature_object.y_cor].direction
		creature_grid[creature_object.x_cor+1][creature_object.y_cor].species = creature_grid[creature_object.x_cor][creature_object.y_cor].species
	if creature_object.direction == "east" and if_enemy(creature_object, creature_grid):
		d = creature_grid[creature_object.x_cor][creature_object.y_cor+1].direction
		creature_grid[creature_object.x_cor][creature_object.y_cor+1].species = creature_grid[creature_object.x_cor][creature_object.y_cor].species
	if creature_object.direction == "west" and if_enemy(creature_object, creature_grid): 
		d = creature_grid[creature_object.x_cor][creature_object.y_cor-1].direction
		creature_grid[creature_object.x_cor][creature_object.y_cor-1].species = creature_grid[creature_object.x_cor][creature_object.y_cor].species

def if_random():
	seed(0) 
	if randint(0, 2)  % 2 != 0:
		return True
	else:
		return False

