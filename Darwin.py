
from random import randint, sample, seed

# code for building a grid

class Darwin:

	def __init__(self, x, y):
		assert y != 0
		assert x != 0
		self.row = x
		self.col = y	
		self.grid  = [["."] * self.col for x in range(self.row)]

	def print_board(self, grid, turn):
		print("Turn = ", str(turn) + ".")
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end=" ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))
		print()

	# adds a creature to the grid
	def add_creature(self, creature, species):
		self.grid[creature.x_cor][creature.y_cor] = str(species.c_id)
		self.grid

	# moves a creature
	def move(self, species, creature, turn):
		if species.c_id == 'h':
			# hop instruction below
			if self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "south":
				creature.x_cor += 1
				self.grid[creature.x_cor][creature.y_cor] = species.c_id
				self.grid[creature.x_cor-1][creature.y_cor] = "."
			elif self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "east":
				creature.y_cor += 1
				self.grid[creature.x_cor][creature.y_cor] = species.c_id
				self.grid[creature.x_cor][creature.y_cor-1] = "."
			elif self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "north":
				creature.x_cor -= 1
				self.grid[creature.x_cor][creature.y_cor] = species.c_id
				self.grid[creature.x_cor+1][creature.y_cor] = "."
			elif self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "west":
				creature.y_cor -= 1
				self.grid[creature.x_cor][creature.y_cor] = species.c_id
				self.grid[creature.x_cor][creature.y_cor+1] = "."
		elif species.c_id == 'f':
			# returns present location
			self.grid[creature.x_cor][creature.y_cor] = str(species.c_id)      ### not sure if this is exactly what we want
		elif species.c_id == 'r':
			if creature.direction == 'north' and self.grid[creature.x_cor-1][creature.y_cor] != '.':	
				# if different species, infect
				if self.grid[creature.x_cor-1][creature.y_cor] != species.c_id :
					creature.x_cor -= 1
					self.grid[creature.x_cor][creature.y_cor] = species.c_id
					infected = self.grid[creature.x_cor+1][creature.y_cor]
					infected = species.c_id								### need to continue working on infect, currently not changing the actual species
		#	elif creature.direction == 'east' and self.grid[creature.x_cor-1][creature.y_cor] != '.':
		#	elif creature.direction == 'south' and self.grid[creature.x_cor-1][creature.y_cor] != '.':
		#	elif creature.direction == 'west' and self.grid[creature.x_cor-1][creature.y_cor] != '.':

	# intakes grid, left/right then up/down
	# moves each creature, then prints the board
	def turn(self, turn, list_spec_creat):
		self.print_board(self.grid, 0)
		for x in range(1, turn):
			for one in list_spec_creat:
				species = one[0]
				creature = one[1]
				for i in self.grid[creature.x_cor][creature.y_cor]:
					for j in i:
						self.move(species, creature, turn)				
			self.print_board(self.grid, x)


#	def is_boundary(self):

#	def is_creature(self, species, creature):
		# identify same or different species

	def __repr__(self):
		return "(%d, %d)" % (self.row, self.col)




class Species:

	species = []
	def __init__(self, c_id):
		self.species = []
		self.c_id = c_id
		self.direction = ["north", "east", "south", "west"]

	def add_instruction(self, instruction):
		self.species.append(instruction)
		return self.species

#	def hop(self, species, creature, grid):
#	def left(self):
#	def right(self):
#	def infect(self):

#	if_empty(self):
#	if_wall(self):
#	if_random(self):
#	if_enemy(self):
#	go(self):

	def __repr__(self):
		return "(%s)" % (self.species)



class Creature:
	def __init__(self, species, direction, x_cor, y_cor):
		self.species = species
		self.direction = direction
		self.program_counter = 0
		self.x_cor = x_cor
		self.y_cor = y_cor

	def __repr__(self):
		return "(%s, %s, %d, %d)" % (self.program_counter, self.species, self.x_cor, self.y_cor)



# THINGS TO DO
# add_instruction
# instruction
# is_boundary
# is_creature