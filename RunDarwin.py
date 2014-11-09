import random
import sys
from Darwin import *

# ----
# food
# ----

"""
 0: left
 1: go 0
"""
food = Species('f')
food.add_instruction("left")
food.add_instruction("go 0")

# ------
# hopper
# ------

"""
 0: hop
 1: go 0
"""
hopper = Species("h")
hopper.add_instruction("hop")
hopper.add_instruction("go 0")

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
rover = Species("r")
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
trap = Species("t")
trap.add_instruction("if_enemy 3")
trap.add_instruction("left")
trap.add_instruction("go 0")
trap.add_instruction("infect")
trap.add_instruction("go 0")

# ----
# best
# ----
"""
 0: if_enemy 10
 1: if_wall 6
 2: if_random 10
 3: hop
 4: go 0
 5: if_random 9
 6: left
 7: go 0
 8: right
 9: go 0
 10: infect
 11: go 0
 12: hop
 13: go 0
 14: if_enemy 12
 15: infect
 16: go 0
"""

best = Species("b")
best.add_instruction("if_enemy 10")
best.add_instruction("if_wall 6")
best.add_instruction("if_random 10")
best.add_instruction("hop")
best.add_instruction("go 0")
best.add_instruction("if_random 9")
best.add_instruction("left")
best.add_instruction("go 0")
best.add_instruction("right")
best.add_instruction("go 0")
best.add_instruction("infect")
best.add_instruction("go 0")
best.add_instruction("hop")
best.add_instruction("go 0")
best.add_instruction("if_enemy 12")
best.add_instruction("infect")
best.add_instruction("go 0")
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

"""
t1 = Creature(trap, "south", 0, 0)
h1 = Creature(hopper, "east", 3, 2)
r1 = Creature(rover, "east", 5, 4)
t2 = Creature(trap, "west", 6, 8)

turn = 6
y = Darwin(7, 9)

y.add_creature(t1)
y.add_creature(h1)
y.add_creature(r1)
y.add_creature(t2)

# ============ START GAME ================
y.master_turn(turn, [t1, h1, r1, t2])

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
direction = ['north','east', 'south', 'west']
f1 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f2 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f3 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f4 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f5 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f6 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f7 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f8 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f9 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f10 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))

h1 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h2 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h3 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h4 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h5 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h6 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h7 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h8 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h9 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h10 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))

r1 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r2 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r3 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r4 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r5 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r6 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r7 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r8 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r9 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r10 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))

t1 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t2 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t3 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t4 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t5 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t6 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t7 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t8 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t9 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t10 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))

y = Darwin(72, 72)
turn = 1001

y.add_creature(f1)
y.add_creature(f2)
y.add_creature(f3)
y.add_creature(f4)
y.add_creature(f5)
y.add_creature(f6)
y.add_creature(f7)
y.add_creature(f8)
y.add_creature(f9)
y.add_creature(f10)

y.add_creature(h1)
y.add_creature(h2)
y.add_creature(h3)
y.add_creature(h4)
y.add_creature(h5)
y.add_creature(h6)
y.add_creature(h7)
y.add_creature(h8)
y.add_creature(h9)
y.add_creature(h10)

y.add_creature(r1)
y.add_creature(r2)
y.add_creature(r3)
y.add_creature(r4)
y.add_creature(r5)
y.add_creature(r6)
y.add_creature(r7)
y.add_creature(r8)
y.add_creature(r9)
y.add_creature(r10)

y.add_creature(t1)
y.add_creature(t2)
y.add_creature(t3)
y.add_creature(t4)
y.add_creature(t5)
y.add_creature(t6)
y.add_creature(t7)
y.add_creature(t8)
y.add_creature(t9)
y.add_creature(t10)

# ============ START GAME ================
y.master_turn(turn, [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])

# ------------
# darwin 72x72
# with best
# ------------

"""
print("*** Darwin 72x72 with Best ***")
seed(0);

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
z = Darwin(72, 72)
turn = 1001

direction = ['north','east', 'south', 'west']
f1 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f2 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f3 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f4 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f5 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f6 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f7 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f8 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f9 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))
f10 = Creature(food, random.choice(direction), random.randint(0,71), random.randint(0,71))

h1 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h2 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h3 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h4 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h5 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h6 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h7 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h8 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h9 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))
h10 = Creature(hopper, random.choice(direction), random.randint(0,71), random.randint(0,71))

r1 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r2 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r3 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r4 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r5 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r6 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r7 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r8 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r9 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))
r10 = Creature(rover, random.choice(direction), random.randint(0,71), random.randint(0,71))

t1 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t2 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t3 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t4 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t5 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t6 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t7 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t8 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t9 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))
t10 = Creature(trap, random.choice(direction), random.randint(0,71), random.randint(0,71))

z.add_creature(f1)
z.add_creature(f2)
z.add_creature(f3)
z.add_creature(f4)
z.add_creature(f5)
z.add_creature(f6)
z.add_creature(f7)
z.add_creature(f8)
z.add_creature(f9)
z.add_creature(f10)

z.add_creature(h1)
z.add_creature(h2)
z.add_creature(h3)
z.add_creature(h4)
z.add_creature(h5)
z.add_creature(h6)
z.add_creature(h7)
z.add_creature(h8)
z.add_creature(h9)
z.add_creature(h10)

z.add_creature(r1)
z.add_creature(r2)
z.add_creature(r3)
z.add_creature(r4)
z.add_creature(r5)
z.add_creature(r6)
z.add_creature(r7)
z.add_creature(r8)
z.add_creature(r9)
z.add_creature(r10)

z.add_creature(t1)
z.add_creature(t2)
z.add_creature(t3)
z.add_creature(t4)
z.add_creature(t5)
z.add_creature(t6)
z.add_creature(t7)
z.add_creature(t8)
z.add_creature(t9)
z.add_creature(t10)

best_1 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_2 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_3 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_4 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_5 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_6 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_7 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_8 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_9 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))
best_10 = Creature(best, random.choice(direction), random.randint(0,71), random.randint(0,71))

z.add_creature(best_1)
z.add_creature(best_2)
z.add_creature(best_3)
z.add_creature(best_4)
z.add_creature(best_5)
z.add_creature(best_6)
z.add_creature(best_7)
z.add_creature(best_8)
z.add_creature(best_9)
z.add_creature(best_10)

# ============ START GAME ================
z.master_turn(turn, [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, best_1, best_2, best_3, best_4, best_5, best_6, best_7, best_8, best_9, best_10])
