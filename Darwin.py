#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

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
		print("   " + " ".join("{0:2d}".format(i) for i in range(len(grid[0]))))
		for i, row in enumerate(grid, 0):
			print("{0:2d}".format(i),end=" ")
			print("".join(" {0} ".format(col if col != None else ".") for col in row))
			
	#def place_creatures(self, creat):
	def random_row(self, grid):
		ship_row = self.grid	
		return (randint(0, len(grid) - 1))
		
			

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


class Creature:
	def __init__(self):
		pass

	def add_instruction(self):
		pass

	class Species:
		def __init__(self):
			pass

		def direction(self):
			pass

		def program_counter(self):
			pass

		def best(self):
			pass




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
