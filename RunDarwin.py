## IT'S RUNDARWIN

from random import randint, sample, seed
import sys
from Darwin import *

# ----
# food
# ----

"""
 0: left
 1: go 0
"""

# ------
# hopper
# ------

"""
 0: hop
 1: go 0
"""

# -----
# rover
# -----

"""
 0: if_enemy 9
 1: if_empty 7
 2: if_random 5
 3: left
 4: go 0
 5: right
 6: go 0
 7: hop
 8: go 0
 9: infect
10: go 0
"""

# ----
# trap
# ----

"""
 0: if_enemy 3
 1: left
 2: go 0
 3: infect
 4: go 0
"""

# ----------
# darwin 8x8
# ----------

print("*** Darwin 8x8 ***")
"""
8x8 Darwin
Food,   facing east,  at (0, 0)
Hopper, facing north, at (3, 3)
Hopper, facing east,  at (3, 4)
Hopper, facing south, at (4, 4)
Hopper, facing west,  at (4, 3)
Food,   facing north, at (7, 7)
Simulate 5 moves.
Print every grid.
"""
# create all species
food = Species('f')
hopper = Species("h")
rover = Species("r")
trap = Species("t")
best = Species("b")

# add instructions for each species
food.add_instruction("left")
food.add_instruction("go 0")

hopper.add_instruction("hop")
hopper.add_instruction("go 0")

rover.add_instruction("if_enemy 9")
rover.add_instruction("if_empty 7")
rover.add_instruction("if_random 5")
rover.add_instruction("left")
rover.add_instruction("go 0")
rover.add_instruction("right")
rover.add_instruction("go 0")
rover.add_instruction("hop")
rover.add_instruction("go 0")
rover.add_instruction("infect")
rover.add_instruction("go 0")

trap.add_instruction("if_enemy 3")
trap.add_instruction("left")
trap.add_instruction("go 0")
trap.add_instruction("infect")
trap.add_instruction("go 0")

# create unique creatures of a species
f1 = Creature(food, "east", 0, 0)
h1 = Creature(hopper, "north", 3, 3)
h2 = Creature(hopper, "east", 3, 4)
h3 = Creature(hopper, "south", 4, 4)
h4 = Creature(hopper, "west", 4, 3)
f2 = Creature(food, "north", 7, 7)

# create the board
<<<<<<< HEAD
turn = 4
s = Darwin(10, 10)

=======
turn = 5
s = Darwin(8, 8)

s.add_creature(f1)
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd
s.add_creature(h1)
s.add_creature(h2)
s.add_creature(h3)
s.add_creature(h4)

<<<<<<< HEAD
s.master_turn(turn, [h1, h2, h3, h4])
#left(creature_object, s.creature_grid)
=======
s.master_turn(turn, [f1, h1, h2, h3, h4, f2])
#left(creature_object, s.creature_grid)

# ============ START GAME ================
>>>>>>> 7a2350517adbd65715a715f03233e99b7f6140dd
#s.turn(turn, [[hopper, h1]])

# ----------
# darwin 7x9
# ----------

print("*** Darwin 7x9 ***")
"""
7x9 Darwin
Trap,   facing south, at (0, 0)
Hopper, facing east,  at (3, 2)
Rover,  facing north, at (5, 4)
Trap,   facing west,  at (6, 8)
Simulate 5 moves.
Print every grid.


# create unique creatures of a species
t1 = Creature(trap, "south", 0, 0)
h1 = Creature(hopper, "east", 3, 2)
r1 = Creature(rover, "north", 5, 4)
t2 = Creature(trap, "west", 6, 8)

# create the board
turn = 5
s = Darwin(7, 9)

# add creatures to the board
s.add_creature(t1, trap)
s.add_creature(h1, hopper)
s.add_creature(r1, rover)
s.add_creature(t2, trap)

# ============ START GAME ================
s.turn(turn, [[trap, t1], [hopper, h1], [rover, r1], [trap, t2]])
"""

# ------------
# darwin 72x72
# without best
# ------------

print("*** Darwin 72x72 without Best ***")
seed(0);
"""
Randomly place the following creatures facing randomly.
Call rand(), mod it with 5184 (72x72), and use that for the position
in a row-major order grid.
Call rand() again, mod it with 4 and use that for it's direction with
the ordering: west, north, east, south.
Do that for each kind of creature.
10 Food
10 Hopper
10 Rover
10 Trap
Simulate 1000 moves.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""

# ------------
# darwin 72x72
# with best
# ------------

print("*** Darwin 72x72 with Best ***")
seed(0);
"""
Randomly place the following creatures facing randomly.
Call rand(), mod it with 5184 (72x72), and use that for the position
in a row-major order grid.
Call rand() again, mod it with 4 and use that for it's direction with
the ordering: 0:west, 1:north, 2:east, 3:south.
Do that for each kind of creature.
10 Food
10 Hopper
10 Rover
10 Trap
10 Best
Simulate 1000 moves.
Best MUST outnumber ALL other species for the bonus pts.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""
