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
		for i in range(turn):
			print("Turn = ", str(i) + ".")
			print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
			for i, row in enumerate(grid, 0):
				print("{0:2d}".format(i),end=" ")
				print("".join(" {0} ".format(col if col != None else ".") for col in row))
			print()

	def add_creature(self, creature):
		self.grid[creature.x_cor][creature.y_cor] = str(creature.c_id)
		return self.grid


#	def is_boundary(self):
#	def is_creature(self):
		# same or different species


	def __repr__(self):
		return "(%d, %d)" % (self.row, self.col)

		
#class Instruction:
#	def __init__(self):

	# instruction
#	def code(self):
		# separate instruction and n

#	def program_counter(self):



class Species:
	def __init__(self):
		self.species = []

	def add_instruction(self, instruction):
		self.species.append(instruction)
		return self.species

	def hop(self):
#		if str(creature.c_id) == "h":
		[species.x_cor][species.y_cor] = "."
		species.y_cor += 1
		[species.x_cor][species.y_cor] = "h"
#			Darwin.grid[creature.x_cor][creature.y_cor] = str(creature.c_id)

#	def left(self):
#	def right(self):
#	def infect(self):

#	if_empty(self):
#	if_wall(self):
#	if_random(self):
#	if_enemy(self):
#	go(self):

	def move(self, species):
		for x in self.species:
			if x == 'hop':
				print("HOPPING")



	def __repr__(Darwin):
		return "(%s)" % (self.hopper)

   
class Creature:
	def __init__(self, species, x_cor, y_cor, c_id):
		self.direction = ["north", "east", "south", "west"]
		self.program_counter = 0
		self.species = species
		self.x_cor = x_cor
		self.y_cor = y_cor
		self.c_id = c_id


#	def food(self):
#	def hopper(self):
#	#	self.grid[x_cor][y_cor] = str(c_id)
#		for i in 
#		return 
	#	print(Darwin.print_board())

#	def rover(self):
#		row = 0
#		col = 0	
#		for i in range(9):
#			col += 1
#			s.grid[row][col] = "r"
#			s.print_board(s.grid)
#			s.grid[row][col] = "."
#		return s.grid

#	def best(self):

	def __repr__(self):
		return "(%s, %s, %d, %d)" % (self.program_counter, self.species, self.x_cor, self.y_cor)

#s.start_game()

'''
	def random_col(self, grid):
		ship_col = self.grid
		return (randint(0, len(grid[0]) - 1))

	def start_turn(self):
		pass

	def action_hop(self):
		pass

	def action_left(self):
		pass

	def action_infect(self):
		pass

	def control_if_empty(self):
		pass

	def control_if_wall(self):
		pass

	def cotrol_if_random(self):
		pass

	def if_enemy(self):
		pass

	def go(self):
		pass

class Species(self):
	def __init__(self):
		self.rover = rover
		self.food = food
		self.trap = trap
		self.best = best

	def add_instruction(self):
		pass

class Creature(self):
	def __init__(self):
	self.direction = direction
	self.program_counter = program_counter			
'''
