from random import randint, sample, seed

## IT'S DARWIN
class Species:
	def __init__(self, name):
		self.instructions = []
		self.c_id = name

<<<<<<< HEAD
	def get_instruction(self, instructions, index):
		return instructions[index]

	def list_instructions(self):
		return self.instructions
=======
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
	
	def turn(self, creature_grid):
		c_species = self.species
	#	self.program_counter = 0 
		stop_turn = False
		while stop_turn == False:
			for inst in c_species.instructions:
				current = inst[0].split(' ')
				if len(current) > 1:
					if current[0] == "if_wall":
						if_wall(self, creature_grid)
					if current[0] == "if_empty":
						if_empty(self, creature_grid)
					if current[0] == "if_enemy":
						if_enemy(self, creature_grid)
					if current[0] == "if_random":
						if_random()
					if current[0] == "infect":
						infect(self, creature_grid)

				if len(current) == 1:
					if current[0] == "hop":
						hop(self, creature_grid)
					if current[0] == "left":
						left(self, creature_grid)
					if current[0] == "right":
						right(self, creature_grid)
					if current[0] == "go":
						Creature.program_counter = 0
					stop_turn = True
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

	#def display(self, display_grid, turn):
	def print_board(self, display_grid, creature_grid, turn):
		print("Turn =", str(turn) + ".")
		print("  " + "".join("{0:d}".format(i%10) for i in range(len(display_grid[0]))))
		for i, row in enumerate(display_grid, 0):
			print("{0:d}".format(i%10),end= " ")
			print("".join("{0}".format(col if col != '1' else ".") for col in row))
		print()
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd

	def add_instruction(self, instructions):
		[a] = [instructions]
		self.instructions.append(a)
		return self.instructions

	#	self.display_grid = Darwin.display(self, display_grid, turn)		
	
		for i in range(0, self.row):
			for j in range(0, self.col):
				#print("type", type(creature_grid[i][j]))
				if creature_grid[i][j].species == None:
					display_grid[i][j] = '.'
				else:
					#print("type", type(creature_grid[i][j]))
					display_grid[i][j] = creature_grid[i][j].species.c_id

		return self.display_grid

	def master_turn(self, turn, list_creat):
		#self.print_board(self.display_grid, self.creature_grid, 0)
		for x in range(0, turn):
			for creat in list_creat:
				if creat.turn(self.creature_grid) == True:
					self.creature_grid
			self.print_board(self.display_grid, self.creature_grid, x)


<<<<<<< HEAD
class Creature:
	def __init__(self, species, direction, x_cor, y_cor): 
		self.species = species
		self.direction = direction
		self.program_counter = 0		
		self.index = 0
		self.x_cor = x_cor
		self.y_cor = y_cor
	'''
	def get_move(self, species, instructions, direction, index):
		if index <= len(instructions):
			return species.get_instruction(instructions, index), direction, index
		else:
			print("get move error")
	'''
	def turn(self, creature_grid):
		c_species = self.species

		self.program_counter = 0 
		stop_turn = False
=======

	def add_creature(self, creature): 
		x_cor = creature.x_cor
		y_cor = creature.y_cor
		self.creature_grid[x_cor][y_cor] = creature
	#	print("type", type(creature.species))

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
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd

		while stop_turn == False:
			for item in c_species.instructions:

<<<<<<< HEAD
				self.program_counter += 1
				#print(self.program_counter)
				#print (current)

				current = item.split(' ')
			#	print(current)
				if len(current) > 1:
					if current[0] == "if_wall":
						self.program_counter = int(current[1])
						if if_wall(self) == True:
							current = get_instruction(c_species.instructions, int(current[1]))
						index += 1
						current = get_instruction(c_species.instructions, index)
					if current[0] == "if_empty":
						if if_empty(self, creature_grid) == True:
							current = get_instruction(c_species.instructions, int(current[1]))
						index += 1
						current = get_instruction(c_species.instructions, index)
					if current[0] == "if_enemy":
						if if_enemy(self, creature_grid) == True:
							current = get_instruction(c_species.instructions, int(current[1]))
						index += 1
						current = get_instruction(c_species.instructions, index)
					if current[0] == "if_random":
						if_random()
					if current[0] == "go":
						self.program_counter = int(current[1])
						current = c_species.get_instruction(c_species.instructions, self.program_counter)
						#return(self.get_move(c_species, c_species.instructions, self.direction, int(current[1])))
				if len(current) == 1:
					if current[0] == "hop":
						#print(self.x_cor, self.y_cor)
						hop(self, creature_grid)
						#print(self.x_cor, self.y_cor)
						current = c_species.get_instruction(c_species.instructions, self.program_counter)
					#	print (self.get_move(c_species, c_species.instructions, self.direction, index))
					if current[0] == "left":
						left(self)
					if current[0] == "right":
						right(self)
					if current[0] == "infect":
						infect(self, creature_grid)
					stop_turn = True
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

	#def display(self, display_grid, turn):
	def print_board(self, display_grid, creature_grid, turn):
		
		for i in range(0, self.row):
			for j in range(0, self.col):
				#print("type", type(creature_grid[i][j]))
				if creature_grid[i][j].species == None:
					display_grid[i][j] = '.'
				else:
					#print("type", type(creature_grid[i][j]))
					display_grid[i][j] = creature_grid[i][j].species.c_id
	#	return self.display_grid

		print("Turn =", str(turn) + ".")
		print("  " + "".join("{0:d}".format(i%10) for i in range(len(display_grid[0]))))
		for i, row in enumerate(display_grid, 0):
			print("{0:d}".format(i%10),end= " ")
			print("".join("{0}".format(col if col != '1' else ".") for col in row))
		print()
		#	self.display_grid = Darwin.display(self, display_grid, turn)		
		


	def master_turn(self, turn, list_creat):
	#	self.print_board(self.display_grid, self.creature_grid, 0)
	#	self.creature_grid
	#	self.display_grid
		for x in range(0, turn):
			self.print_board(self.display_grid, self.creature_grid, x)
			for creat in list_creat:
				if creat.turn(self.creature_grid) == True:
					creat.turn(self.creature_grid)
					self.creature_grid


		#	self.print_board(self.display_grid, self.creature_grid, x)

	def add_creature(self, creature): 
		x_cor = creature.x_cor
		y_cor = creature.y_cor
		self.creature_grid[x_cor][y_cor] = creature

# ======================== INSTRUCTIONS ============================
def hop(creature_object, creature_grid):
	#print(if_empty(creature_object, creature_grid))
#	print(creature_object.x_cor)
#	print(creature_object.y_cor)
	if creature_object.direction == "north" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor-1][creature_object.y_cor] = creature_grid[creature_object.x_cor][creature_object.y_cor]
		#Creature(creature_object.species, creature_object.direction, creature_object.x_cor-1, creature_object.y_cor)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.x_cor -= 1
	#	print(creature_grid[2][3].species)
	if creature_object.direction == "south" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor+1][creature_object.y_cor] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor+1, creature_object.y_cor)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.x_cor +=1
	if creature_object.direction == "east" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor+1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor+1)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.y_cor+=1
	if creature_object.direction == "west" and if_wall(creature_object) == False and if_empty(creature_object, creature_grid):
		creature_grid[creature_object.x_cor][creature_object.y_cor-1] = Creature(creature_object.species, creature_object.direction, creature_object.x_cor, creature_object.y_cor-1)
		creature_grid[creature_object.x_cor][creature_object.y_cor] = Creature(None, None, None, None)
		creature_object.y_cor-=1
=======
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

'''	

	#print(if_wall(s.creature_grid[0][0]))
	#for i in s.creature_grid:
	 #	for j in i:
	 #		print (j.species)
	print(s.display(s.display_grid, s.creature_grid, turn))
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd

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
#	print("m", creature_object.x_cor)
	if creature_object.direction == "south" and creature_object.x_cor+1 ==  r:
		return True
	if creature_object.direction == "north" and creature_object.x_cor-1 < 0:

<<<<<<< HEAD
		return True
	if creature_object.direction == "east" and creature_object.y_cor+1 ==  c:
		return True
	if creature_object.direction == "west" and creature_object.y_cor-1 <  0:
		return True
	else:
		#print("m", creature_object.x_cor)
		return False

def if_empty(creature_object, creature_grid):
	#print(creature_object.x_cor, creature_object.y_cor)
	#print("o", creature_object.x_cor-1)
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
=======
	def print_board(self, display_grid, turn):
		print("Turn =", str(turn) + ".")
		print("  " + "".join("{0:d}".format(i) for i in range(len(display_grid[0]))))
		for i, row in enumerate(display_grid, 0):
			print("{0:d}".format(i),end= " ")
			print("".join("{0}".format(col if col != None else ".") for col in row))
		print()


		for i in range(0, self.row):
			for j in range(0, self.col):
				if self.creature_grid[i][j].species == None:
					self.display_grid[i][j] = '.'
				else:
					self.display_grid[i][j] = self.creature_grid[i][j].species.c_id
		print(self.display_grid)
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd

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

<<<<<<< HEAD
def if_random():
	seed(0) 
	if randint(0, 2)  % 2 != 0:
		return True
	else:
		return False
=======
		top_line = "  "
		for c in range(self.col):
			top_line += str(c%10)
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd

		print (top_line) # change display grid name
		for x in self.display_grid:
 			line = ''
 			col_line = 0
 			for y in x:
 				line += y
 				col_line += 1
 			print(col_line)
 
'''
