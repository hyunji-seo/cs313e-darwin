
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

	def add_creature(self, creature, species):
	#	c_list = []
		self.grid[creature.x_cor][creature.y_cor] = str(species.c_id)
#		c_list.append(creature)
		self.grid

	def move(self, species, creature, turn):
		#for n in range(turn):
		if self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "south":
			creature.x_cor += 1
			self.grid[creature.x_cor][creature.y_cor] = str(species.c_id)
			self.grid[creature.x_cor-1][creature.y_cor] = "."
		elif self.grid[creature.x_cor][creature.y_cor] != "." and creature.direction == "east":
			creature.y_cor += 1
			self.grid[creature.x_cor][creature.y_cor] = str(species.c_id)
			self.grid[creature.x_cor][creature.y_cor-1] = "."
		#self.grid
		#if ('hop' in species.species):
		#	print("hop")
	#		return species.hop(species, creature, self.grid)
		#	self.grid[creature.x_cor][creature.y_cor] = "h"
			
	# intakes grid and moves each creature accordingly, then prints the board
	def turn(self, turn, list_spec_creat):
		self.print_board(self.grid, 0)
		for x in range(1, turn):
			for one in list_spec_creat:
				species = one[0]
				creature = one[1]
				for i in self.grid[creature.x_cor][creature.y_cor]:
					for j in i:
						self.move(species, creature, turn)
			#		self.grid[row][col] != "."
			#self.move(species, creature, turn)				
			self.print_board(self.grid, x)
#for i in self.grid[creature.x_cor][creature.y_cor]


#	def is_boundary(self):

#	def is_creature(self):
		# identify same or different species

	def __repr__(self):
		return "(%d, %d)" % (self.row, self.col)




class Species:
	species = []
	def __init__(self, c_id):
		self.species = []
		self.c_id = c_id

	def add_instruction(self, instruction):
		self.species.append(instruction)
		return self.species

#	def hop(self, species, creature, grid):
#		grid[creature.x_cor][creature.y_cor] = str(creature.c_id)
#		creature.y_cor += 1
#		grid[creature.x_cor][creature.y_cor-2] = "."
#		Darwin.grid[creature.x_cor][creature.y_cor] = str(creature.c_id)

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
		self.direction = direction
		self.program_counter = 0
		self.species = species
		self.x_cor = x_cor
		self.y_cor = y_cor

	def __repr__(self):
		return "(%s, %s, %d, %d)" % (self.program_counter, self.species, self.x_cor, self.y_cor)



# THINGS TO DO
# add_instruction
# instruction
# is_boundary
# direction
# is_creature