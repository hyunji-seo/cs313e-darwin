#!/usr/bin/env python3

# -----------------------------
# projects/collatz/RunDarwin.py
# Copyright (C) 2014
# Glenn P. Downing
# -----------------------------

# -------
# imports
# -------

from random import seed
import sys

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
