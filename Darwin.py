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
		#for i in range(turn):
	#	print(("Turn = ", str(i) + ".") for i in range(turn))
		print("Turn = ", str(turn) + ".")
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end=" ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))
		print()



	def add_creature(self, creature):
		self.grid[creature.x_cor][creature.y_cor] = str(creature.c_id)
		return self.grid

	def move(self, species, creature, turn):
		for x in species.species:
			if x == 'hop':
				print("hop")
				self.grid[creature.x_cor][creature.y_cor] = "h"
				(creature.x_cor) += 1
				self.grid[creature.x_cor-2][creature.y_cor] = "."




#	def is_boundary(self):
#	def is_creature(self):
		# identify same or different species

#	def __repr__(self):
#		return "(%d, %d)" % (self.row, self.col)

	

class Species:
	species = []     # wouldn't work if not called 'species';gives list of instructions to 'move'
	def __init__(self):
		self.species = []

	def add_instruction(self, instruction):
		self.species.append(instruction)
		return self.species

	def hop(self):
		[species.x_cor][species.y_cor] = "."
		species.y_cor += 1
		[species.x_cor][species.y_cor] = str(creature.c_id)
#			Darwin.grid[creature.x_cor][creature.y_cor] = str(creature.c_id)

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
	def __init__(self, species, x_cor, y_cor, c_id):
		self.direction = ["north", "east", "south", "west"]
		self.program_counter = 0
		self.species = species
		self.x_cor = x_cor
		self.y_cor = y_cor
		self.c_id = c_id

	def __repr__(self):
		return "(%s, %s, %d, %d)" % (self.program_counter, self.species, self.x_cor, self.y_cor)



