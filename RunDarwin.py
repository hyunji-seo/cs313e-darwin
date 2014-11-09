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
"""
# create unique creatures of a species
f1 = Creature(food, "east", 0, 0)
h1 = Creature(hopper, "north", 3, 3)
h2 = Creature(hopper, "east", 3, 4)
h3 = Creature(hopper, "south", 4, 4)
h4 = Creature(hopper, "west", 4, 3)
f2 = Creature(food, "north", 7, 7)

# create the board
turn = 5
x = Darwin(8, 8)

x.add_creature(f1)
x.add_creature(h1)
x.add_creature(h2)
x.add_creature(h3)
x.add_creature(h4)
x.add_creature(f2)

# ============ START GAME ================

x.master_turn(turn, [f1, h1, h2, h3, h4, f2])
"""
# ----------
# darwin 7x9
# ----------
"""
print("*** Darwin 7x9 ***")

7x9 Darwin
Trap,   facing south, at (0, 0)
Hopper, facing east,  at (3, 2)
Rover,  facing north, at (5, 4)
Trap,   facing west,  at (6, 8)
Simulate 5 moves.
Print every grid.
"""

"""
# create unique creatures of a species
t1 = Creature(trap, "south", 0, 0)
h1 = Creature(hopper, "east", 3, 2)
r1 = Creature(rover, "north", 5, 4)
t2 = Creature(trap, "west", 6, 8)

# create the board
turn = 6
y = Darwin(7, 9)

# add creatures to the board
y.add_creature(t1)
y.add_creature(h1)
y.add_creature(r1)
y.add_creature(t2)

# ============ START GAME ================

y.master_turn(turn, [t1, h1, r1, t2])

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
# create unique creatures of a species
f1 = Creature(trap, "south", 0, 0)
f2 = Creature(trap, "south", 0, 0)
f3 = Creature(trap, "south", 0, 0)
f4 = Creature(trap, "south", 0, 0)
f5 = Creature(trap, "south", 0, 0)
f6 = Creature(trap, "south", 0, 0)
f7 = Creature(trap, "south", 0, 0)
f8 = Creature(trap, "south", 0, 0)
f9 = Creature(trap, "south", 0, 0)
f10 = Creature(trap, "south", 0, 0)

h1 = Creature(hopper, "east", 3, 2)
h2 = Creature(hopper, "east", 3, 2)
h3 = Creature(hopper, "east", 3, 2)
h4 = Creature(hopper, "east", 3, 2)
h5 = Creature(hopper, "east", 3, 2)
h6 = Creature(hopper, "east", 3, 2)
h7 = Creature(hopper, "east", 3, 2)
h8 = Creature(hopper, "east", 3, 2)
h9 = Creature(hopper, "east", 3, 2)
h10 = Creature(hopper, "east", 3, 2)

r1 = Creature(rover, "north", 5, 4)
r2 = Creature(rover, "north", 5, 4)
r3 = Creature(rover, "north", 5, 4)
r4 = Creature(rover, "north", 5, 4)
r5 = Creature(rover, "north", 5, 4)
r6 = Creature(rover, "north", 5, 4)
r7 = Creature(rover, "north", 5, 4)
r8 = Creature(rover, "north", 5, 4)
r9 = Creature(rover, "north", 5, 4)
r10 = Creature(rover, "north", 5, 4)

t1 = Creature(rover, "north", 5, 4)
t2 = Creature(trap, "west", 6, 8)
t3 = Creature(rover, "north", 5, 4)
t4 = Creature(rover, "north", 5, 4)
t5 = Creature(rover, "north", 5, 4)
t6 = Creature(rover, "north", 5, 4)
t7 = Creature(rover, "north", 5, 4)
t8 = Creature(rover, "north", 5, 4)
t9 = Creature(rover, "north", 5, 4)
t10 = Creature(rover, "north", 5, 4)

# create the board
turn = 11
y = Darwin(72, 72)

# add creatures to the board
y.add_creature(t1)
y.add_creature(h1)
y.add_creature(r1)
y.add_creature(t2)

# ============ START GAME ================

y.master_turn(turn, [t1, h1, r1, t2])
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
