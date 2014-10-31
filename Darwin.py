#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

from random import randint, sample, seed

# code for building a grid

class Darwin:
	def __init__(self, x, y):
		assert y != 0
		assert x != 0
		self.row = x
		self.col = y	
		self.grid  = [["."] * self.col for x in range(self.row)]
		#print (self.grid)
	
	def print_board(self, grid):
		print ("Turn = ")
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end=" ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))

	def add_creature(self, creature):
		self.grid[3][3] = "r"
		return self.grid

	def __repr__(self):
        	return "(%d, %d)" % (self.row, self.column)
		

class Species:
	def __init__(self):
		self.rover = []
		self.food = []
		self.hooper = []
		self.trap = []
		self.best = []

	def add_instruction(self):
		self.rover = ["if_enemy", "if_empty", "if_random", "left", "go", "right", "go", "hop", "go", "infect", "go"]
		return self.rover		

	def __repr__(self):
        	return "(%s)" % (self.rover)

class Creature:
	def __init__(self, species, x_cor, y_cor):
		self.direction = ["north", "east", "south", "west"]
		self.program_counter = 0
		self.species = species
		self.x_cor = x_cor
		self.y_cor = y_cor

	
	

	def __repr__(self):
        	return "(%s, %s, %s, %d, %d)" % (self.direction, self.program_counter, self.species, self.x_cor, self.y_cor)



s = Darwin(8, 8)
s.print_board(s.grid)
rover = Species()
r1 = Creature(rover, 3, 3)
s.add_creature(r1)
s.print_board(s.grid)
#s.start_game()



row = 0
col = 0	
for i in range(9):
	col += 1
	s.grid[row][col] = "r"
	s.print_board(s.grid)
	s.grid[row][col] = "."
			

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


s = Darwin(12, 12)

s.print_board(s.grid)
#s.place_creatures()


ship_row = s.random_row(s.grid)
ship_col = s.random_col(s.grid)

print (ship_row)
print (ship_col)

s.grid[ship_row][ship_col] = "r"
s.print_board(s.grid)
s.grid[ship_row][ship_col] = "t"

#s.print_board(s.grid[ship_row][ship_col])
s.print_board(s.grid)

			

# ------------
# collatz_read
# ------------



def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------



def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    cycle_length = {1:1} 
    assert i > 0  
    assert j > 0    
    if i > j:  # To ensure i is the start and j is the end of the range
        i, j = j, i
    if i < (j//2) + 1: 
        m = (j//2) + 1
    else:
        m = i
    for c in range(m,j+1):
      temp = c
      counter = 1      
      while c > 1:
        if c % 2 == 1:
            counter += 2
            c = c + (c//2) + 1 
        else:
            counter += 1
            c = (c // 2)
      cycle_length[temp] = counter
      v = max(cycle_length.values())
    assert v > 0
    return max(cycle_length.values())

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
