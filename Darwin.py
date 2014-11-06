from random import randint, sample, seed

class Species:
	def __init__(self, c_id):
		self.instructions = []
		self.c_id = c_id

	def get_instruction(self, instructions, program_counter):
		return instructions[program_counter]

	def add_instruction(self, instructions, program_counter = None):
		# each instruction is a function
		if program_counter != None:
			a = [instructions, program_counter]
		else:
			a = [instructions]
		self.instructions.append(a)
		return self.instructions


class Creature:
	def __init__(self, species, direction, program_counter, x_cor, y_cor): 
		self.species = species
		self.direction = direction
		self.program_counter = program_counter
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


class Darwin:
	def __init__(self, x, y):
		self.row = x
		self.col = y
		self.grid = [["."] * self.col for x in range(self.row)]

	def turn(self, turn, list_turn):
		s.print_board(s.grid, 0)
		for x in range(1, turn):
			for one in list_turn:
				species = one[0]
				creature = one[1]
				instructions = one[2]
				direction = one[3]
				program_counter = one[4]
				for row in self.grid[0][0]:
					for c in row:
						try:
							m = creature.get_move(species, instructions, direction, program_counter)
							print(m[0])
							if m[0] == ["hop"]:
								assert creature.x_cor >= 0 and creature.y_cor >= 0
								if self.grid[creature.x_cor+1][creature.y_cor] != species.c_id and creature.direction == "south":
									creature.x_cor += 1
									self.grid[creature.x_cor][creature.y_cor] = species.c_id
									self.grid[creature.x_cor-1][creature.y_cor] = '.'
								if self.grid[creature.x_cor][creature.y_cor+1] != species.c_id and creature.direction == "east":
									creature.y_cor += 1
									self.grid[creature.x_cor][creature.y_cor] = species.c_id
									self.grid[creature.x_cor][creature.y_cor-1] = '.'
								if self.grid[creature.x_cor-1][creature.y_cor] != species.c_id and creature.direction == "north":
									creature.x_cor -= 1
									self.grid[creature.x_cor][creature.y_cor] = species.c_id
									self.grid[creature.x_cor+1][creature.y_cor] = '.'
								if self.grid[creature.x_cor][creature.y_cor-1] != species.c_id and creature.direction == "west":
									creature.y_cor -= 1
									self.grid[creature.x_cor][creature.y_cor] = species.c_id
									self.grid[creature.x_cor][creature.y_cor+1] = '.'

							if m[0] == ["left"]  :
								if creature.direction == "north":
									creature.direction = "west"
								if creature.direction == "west":
									creature.direction = "south"
								if creature.direction == "south":
									creature.direction = "east"
								if creature.direction == "east":
									creature.direction = "north" 
							#	print(creature.direction)
							
							if m[0] == ["right"]:
								if creature.direction == "north":
									creature.direction = "east"
								if creature.direction == "west":
									creature.direction = "north"
								if creature.direction == "south":
									creature.direction = "west"
								if creature.direction == "east":
									creature.direction = "south" 

							if m[0][0] == "infect":
								if creature.direction == "north" and self.grid[creature.x_cor-1][creature.y_cor] != '.' and self.grid[creature.x_cor-1][creature.y_cor] != creature.species.c_id :
							   		print(self.grid[creature.x_cor-1][creature.y_cor])
							   		self.grid[creature.x_cor-1][creature.y_cor] = creature.species
							
							if m[0][0] == "if_empty":
								index = m[0][1]								
								if self.grid[creature.x_cor+1][creature.y_cor] == '.' and creature.direction == "south":
									print(creature.species.get_instruction(species.instructions, index))
								if self.grid[creature.x_cor][creature.y_cor+1] == '.' and creature.direction == "east":
									print(creature.species.get_instruction(species.instructions, index))
								if self.grid[creature.x_cor-1][creature.y_cor] == '.' and creature.direction == "north":
									print(creature.species.get_instruction(species.instructions, index))
								if self.grid[creature.x_cor][creature.y_cor-1] == '.' and creature.direction == "west":
									print(creature.species.get_instruction(species.instructions, index))

							if m[0][0] == "if_wall":
								index = m[0][1]
								if self.grid[creature.x_cor+1][creature.y_cor] != '.' and creature.direction == "south":		## what's a wall?
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor][creature.y_cor+1] != '.' and creature.direction == "east":
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor-1][creature.y_cor] != '.' and creature.direction == "north":
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor][creature.y_cor-1] != '.' and creature.direction == "west":
									species.get_instruction(species.instructions, index)
							
						#	if m[0][0] == "if_random":
						#		index = m[0][1]
						#		random.seed(0) 
						#		if random.randrange(0, 2) != %2:
									# not sure here
							
							if m[0][0] == "if_enemy":
								index = m[0][1]
								if self.grid[creature.x_cor+1][creature.y_cor] != species.c_id and creature.direction == "south":
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor][creature.y_cor+1] != species.c_id and creature.direction == "east":
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor-1][creature.y_cor] != species.c_id and creature.direction == "north":
									species.get_instruction(species.instructions, index)
								if self.grid[creature.x_cor][creature.y_cor-1] != species.c_id and creature.direction == "west":
									species.get_instruction(species.instructions, index)
								creature.program_counter += 1
								print(creature.program_counter)
								#print(creature.species.instructions)
								print(creature.species.instructions[creature.program_counter])
								creature.species.get_instruction(creature.species.instructions, creature.program_counter)
							

							if m[0][0] == "go":
								counter = m[0][1]
								return (species.get_instruction(species.instructions, counter))

						#assert creature.x_cor >= 0 and creature.y_cor >= 0
	
						except AssertionError:
							m = creature.get_move(species, instructions, direction, program_counter)
							print("assertion")
						except IndexError:
							print("index")
					
			s.print_board(s.grid, x)


	def print_board(self, grid, turn):
		print("Turn = ", str(turn) + ".")
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end= " ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))
		print()

	def add_creature(self, creature, species):
		self.grid[creature.x_cor][creature.y_cor] = species.c_id
		self.grid



turn = 5
s = Darwin(8,8)


hopper = Species("h")
hopper.add_instruction("hop")
hopper.add_instruction("go", 0)

food = Species('f')
food.add_instruction("left")
food.add_instruction("go", 0)

rover = Species("r")
rover.add_instruction("hop")
rover.add_instruction("if_enemy")
#rover.add_instruction("if_empty", 7)
#rover.add_instruction("if_random", 5)
#rover.add_instruction("left")
#rover.add_instruction("go", 0)
#rover.add_instruction("right")
#rover.add_instruction("go", 0)
#rover.add_instruction("hop")
#rover.add_instruction("go", 0)
rover.add_instruction("infect")
#rover.add_instruction("go", 0)

f1 = Creature(food, "east", 0, 0, 0)
h1 = Creature(hopper, "north", 0, 3, 3)
h2 = Creature(hopper, "east", 0, 3, 4)
h3 = Creature(hopper, "south", 0, 4, 4)
h4 = Creature(hopper, "west", 0, 4, 3)
f2 = Creature(food, "north", 0, 7, 7)

r1 = Creature(rover, "north", 0, 4, 5)

#s.add_creature(f1, food)
#s.add_creature(h1, hopper)
s.add_creature(h2, hopper)
#s.add_creature(h3, hopper)
#s.add_creature(h4, hopper)
#s.add_creature(f2, food)

s.add_creature(r1, rover)
#print(h1.get_move(hopper, hopper.instructions, h1.direction, h1.program_counter))
#print(hopper.get_instruction(hopper.instructions, h1.program_counter))

#hopper.get_instruction()
#print(hopper.instructions)

#print(hopper.get_instruction(hopper.instructions, h2.program_counter))


#s.print_board(s.grid,turn)

s.turn(turn, [[rover, r1, rover.instructions, r1.direction, r1.program_counter], [hopper, h2, hopper.instructions, h2.direction, h2.program_counter]])

#s.print_board(s.grid,turn)

#[food, f1, food.instructions, f1.direction, f1.program_counter], 
#	[hopper, h1, hopper.instructions, h1.direction, h1.program_counter],
#	[hopper, h2, hopper.instructions, h2.direction, h2.program_counter],
#	[hopper, h3, hopper.instructions, h3.direction, h3.program_counter],
#	[hopper, h4, hopper.instructions, h4.direction, h4.program_counter], 
#	[food, f2, food.instructions, f2.direction, f2.program_counter],