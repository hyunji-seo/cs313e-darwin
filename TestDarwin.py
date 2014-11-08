
# -------
# imports
# -------

from random import *
from io       import StringIO
from unittest import main, TestCase

from New import *

# -----------
# TestDarwin
# -----------

class TestDarwin (TestCase) :
    

    # -------------
    # class Species
    # -------------

    # ============= Species ======================


    # =============== get_instruction ====================   
    def test_get_instruction_1 (self) :
        s = Species('food')
        instructions = [['left'], ['go']]
        program_counter = 1
        get_i = s.get_instruction(instructions, program_counter)
        self.assertEqual(get_i, ['go'])

    def test_get_instruction_2 (self) :
        s = Species('hopper')
        instructions = [['hop'], ['go']]
        program_counter = 0
        get_i = s.get_instruction(instructions, program_counter)
        self.assertEqual(get_i, ['hop'])

    def test_get_instruction_3 (self) :
        s = Species('trap')
        instructions = [['if_enemy'],['left'],['go'],['infect'],['go']]
        program_counter = 3
        get_i = s.get_instruction(instructions, program_counter)
        self.assertEqual(get_i, ['infect'])

    def test_list_instruction_1 (self) :
        s = Species('food')
        list_i = s.list_instructions()
        self.assertEqual(list_i, [])

    def test_list_instruction_2 (self) :
        s = Species('trap')
        list_i = s.list_instructions()
        self.assertEqual(list_i, [])

    def test_list_instruction_3 (self) :
        s = Species('hopper')
        list_i = s.list_instructions()
        self.assertEqual(list_i, [])

    # ============= add_instruction ==============
##########################################################
######## need to clarify what we wanna do on Darwin ######
##########################################################
    
    def test_add_instruction_1 (self) :
        s = Species('food')
        instructions = 'left'
        add_i = s.add_instruction(instructions)
        self.assertEqual(add_i, ["left"])  
        
    def test_add_instruction_2 (self) :
        s = Species('hopper')
        instructions = 'hop'
        add_i = s.add_instruction(instructions)
        self.assertEqual(add_i, ["hop"])   

    def test_add_instruction_3 (self) :
        s = Species('trap')
        instructions = 'if_enemy 3'
        add_i = s.add_instruction(instructions)
        self.assertEqual(add_i, ["if_enemy 3"])
    """
    # ============== get_move ==================
    def test_get_move_1 (self) :
        creature = Creature(food, "east", 0, 0)
        species = food
        instructions = [['left'],['go 0']]
        direction = "east"
        program_counter = 0
        m = creature.get_move(species, instructions, direction, program_counter)
        self.assertEqual(m[0], ['left'])

    def test_get_move_2 (self) :
        creature = Creature(hopper, "north", 3, 3)
        species = hopper
        instructions = [['hop'],['go 0']]
        direction = "north"
        program_counter = 0
        m = creature.get_move(species, instructions, direction, program_counter)
        self.assertEqual(m[0], ['hop'])

    def test_get_move_3 (self) :
        creature = Creature(trap, "north", 4, 5)
        species = trap
        instructions = [['if_enemy'],['left'],['go'],['infect'],['go']]
        direction = "north"
        program_counter = 0
        m = creature.get_move(species, instructions, direction, program_counter)
        self.assertEqual(m[0], ['if_enemy'])

    """

    # ============== turn ==================

    #def test_turn_1 (self):
    #    current - inst[self.program_counter].split('')

    #def test_turn_2 (self):

    #def test_turn_3 (self):

    # -------------
    # class Darwin
    # -------------

    def test_display_1 (self):
        turn = 5
        row = 10
        col = 10
        self.display_grid = [["."] * col for x in range(row)]
        self.display_grid[3][3] = 'h'
        self.assertEqual(self.display_grid[3][3], 'h')

    def test_display_2 (self):
        turn = 5
        row = 10
        col = 10
        self.display_grid = [["."] * col for x in range(row)]
        self.display_grid[0][0] = 'f'
        self.assertEqual(self.display_grid[0][0], 'f')

    def test_display_3 (self):
        turn = 5
        row = 10
        col = 10
        self.display_grid = [["."] * col for x in range(row)]
        self.display_grid[9][9] = 'r'
        self.assertNotEqual(self.display_grid[9][9], '.')


    #def test_display_1 (self):

    #def test_display_1 (self):

    # =========== add_creature ===============

    def test_add_creature_1 (self) :
        s = Darwin(8, 8)
        species = Species('trap')
        creature = Creature(species, "north", 4, 5)
        s.add_creature(creature)
        self.assertEqual(s.creature_grid[4][5], s.creature_grid[creature.x_cor][creature.y_cor])
    
    def test_add_creature_2 (self) :
        s = Darwin(8, 8)
        species = Species('hopper')
        creature = Creature(species, "west",4, 3)
        s.add_creature(creature)
        self.assertEqual(s.creature_grid[4][3], s.creature_grid[creature.x_cor][creature.y_cor])

    def test_add_creature_3 (self) :
        s = Darwin(8, 8)
        species = Species('food')
        creature = Creature(species, "east", 0, 0)
        s.add_creature(creature)
        self.assertNotEqual(s.creature_grid[0][1], s.creature_grid[creature.x_cor][creature.y_cor])
    


    
    # ---
    # hop
    # ---

    def test_hop_1 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
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
        r = Creature(rover, "south", 3, 3)
        s.add_creature(r)
        hop(r, s.creature_grid)
        self.assertEqual(s.creature_grid[r.x_cor-1][r.y_cor].species, None)
    
    def test_hop_2 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
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
        r = Creature(rover, "north", 3, 3)
        s.add_creature(r)
        hop(r, s.creature_grid)
        self.assertEqual(s.creature_grid[r.x_cor+1][r.y_cor].species, None)

    def test_hop_3 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
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
        r = Creature(rover, "east", 3, 3)
        s.add_creature(r)
        hop(r, s.creature_grid)
        self.assertEqual(s.creature_grid[r.x_cor][r.y_cor-1].species, None)

    def test_hop_3 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
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
        r = Creature(rover, "west", 3, 3)
        s.add_creature(r)
        hop(r, s.creature_grid)
        self.assertEqual(s.creature_grid[r.x_cor][r.y_cor+1].species, None)

    

    # ----
    # left
    # ----
    
    def test_left_1 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "north", 5, 5) 
        s.add_creature(creature)
        left(creature)
        self.assertEqual(creature.direction, 'west')

    def test_left_2 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "west", 5, 5) 
        s.add_creature(creature)
        left(creature)
        self.assertEqual(creature.direction, 'south')

    def test_left_3 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "south", 5, 5) 
        s.add_creature(creature)
        left(creature)
        self.assertEqual(creature.direction, 'east')

    def test_left_4 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "east", 5, 5) 
        s.add_creature(creature)
        left(creature)
        self.assertEqual(creature.direction, 'north')

    #------
    # right
    # -----
    
    def test_right_1 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "north", 5, 5) 
        s.add_creature(creature)
        right(creature)
        self.assertEqual(creature.direction, 'east')

    def test_right_2 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "west", 5, 5) 
        s.add_creature(creature)
        right(creature)
        self.assertEqual(creature.direction, 'north')

    def test_right_3 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "south", 5, 5) 
        s.add_creature(creature)
        right(creature)
        self.assertEqual(creature.direction, 'west')

    def test_right_4 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "east", 5, 5) 
        s.add_creature(creature)
        right(creature)
        self.assertEqual(creature.direction, 'south')
    
    # ------
    # infect
    # ------
    def test_infect_1 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "east", 4, 4)
        f = Creature(food, "south", 4, 5) 
        s.add_creature(f)
        s.add_creature(r)
        infect(r, s.creature_grid)
        self.assertTrue(s.creature_grid[r.x_cor][r.y_cor+1].species, s.creature_grid[r.x_cor][r.y_cor].species)
    
    def test_infect_2 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "west", 4, 4)
        f = Creature(food, "south", 4, 3) 
        s.add_creature(f)
        s.add_creature(r)
        infect(r, s.creature_grid)
        self.assertTrue(s.creature_grid[r.x_cor][r.y_cor-1].species, s.creature_grid[r.x_cor][r.y_cor].species)

    def test_infect_3 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "north", 4, 4)
        f = Creature(food, "south", 3, 4) 
        s.add_creature(f)
        s.add_creature(r)
        infect(r, s.creature_grid)
        self.assertTrue(s.creature_grid[r.x_cor-1][r.y_cor].species, s.creature_grid[r.x_cor][r.y_cor].species)

    def test_infect_3 (self) :
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "south", 4, 4)
        f = Creature(food, "south", 5, 4) 
        s.add_creature(f)
        s.add_creature(r)
        infect(r, s.creature_grid)
        self.assertTrue(s.creature_grid[r.x_cor+1][r.y_cor].species, s.creature_grid[r.x_cor][r.y_cor].species)

  
    # -------
    # if_wall
    # -------
    
    def test_if_wall_1 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        creature = Creature(species, "south", 7, 5) 
        s.add_creature(creature)
        self.assertTrue(if_wall(creature))

    def test_if_wall_2 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        creature = Creature(species, "east", 5, 7) 
        s.add_creature(creature)
        self.assertTrue(if_wall(creature))

    def test_if_wall_3 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        creature = Creature(species, "north", 0, 5) 
        s.add_creature(creature)
        self.assertTrue(if_wall(creature))

    def test_if_wall_4 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        creature = Creature(species, "west", 5, 0) 
        s.add_creature(creature)
        self.assertTrue(if_wall(creature))

    def test_if_wall_5 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        creature = Creature(species, "south", 0, 0) 
        s.add_creature(creature)
        self.assertFalse(if_wall(creature))

    # --------
    # if_empty
    # --------
    
    def test_if_empty_1 (self) :
        s = Darwin(2, 2)
        rover = Species('rover')
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
        creat = Creature(rover, "south", 0, 0) 
        s.add_creature(creat)
        self.assertTrue(if_empty(creat, s.creature_grid))

    def test_if_empty_2 (self) :
        s = Darwin(2, 2)
        rover = Species('rover')
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
        c_ture = Creature(rover, "north", 1, 1) 
        s.add_creature(c_ture)
        self.assertTrue(if_empty(c_ture, s.creature_grid))

    def test_if_empty_3 (self) :
        s = Darwin(2, 2)
        rover = Species('rover')
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
        creature = Creature(rover, "east", 0, 0) 
        s.add_creature(creature)
        self.assertTrue(if_empty(creature, s.creature_grid))

    def test_if_empty_4 (self) :
        s = Darwin(2, 2)
        rover = Species('rover')
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
        creature = Creature(rover, "north", 1, 1) 
        s.add_creature(creature)
        self.assertTrue(if_empty(creature, s.creature_grid))

    def test_if_empty_5 (self) :
        s = Darwin(2, 2)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
        rover.add_instruction("go 0")
        rover.add_instruction("hop")
        rover.add_instruction("go 0")
        rover.add_instruction("infect")
        rover.add_instruction("go 0")
        r = Creature(rover, "east", 0, 1)
        f = Creature(food, "south", 1, 1) 
        s.add_creature(f)
        s.add_creature(r)
        self.assertFalse(if_empty(r, s.creature_grid))


    # --------
    # if_enemy
    # --------
    
    
    def test_if_enemy_1 (self):
        s = Darwin(2, 2)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "south", 0, 1)
        f = Creature(food, "south", 1, 1) 
        s.add_creature(f)
        s.add_creature(r)
        self.assertTrue(if_enemy(r, s.creature_grid))

    def test_if_enemy_2 (self):
        s = Darwin(4, 4)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "west", 2, 2)
        f = Creature(food, "south", 2, 1)
        s.add_creature(f)
        s.add_creature(r)
        self.assertTrue(if_enemy(r, s.creature_grid))

    def test_if_enemy_3 (self):
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "east", 4, 4)
        f = Creature(food, "south", 4, 5) 
        s.add_creature(f)
        s.add_creature(r)
        self.assertTrue(if_enemy(r, s.creature_grid))

        
    def test_if_enemy_4 (self):
        s = Darwin(6, 6)
        rover = Species('rover')
        food = Species('food')
        food.add_instruction("left")
        food.add_instruction("go 0")
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
        r = Creature(rover, "north", 2, 2)
        f = Creature(food, "south", 1, 2) 
        s.add_creature(f)
        s.add_creature(r)
        self.assertTrue(if_enemy(r, s.creature_grid))




# ----
# main
# ----

main()


"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
