
# -------
# imports
# -------

import random 
from io       import StringIO
from unittest import main, TestCase

from Darwin import *

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


    # ============= add_instruction ==============
 
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

# ============== CREATURE =========================
# ============== turn ================
    def test_turn_1(self):
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
        self.assertEqual(True, Creature.turn(r, s.creature_grid))

    def test_turn_2 (self):
        s = Darwin(6, 6)
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

# -------------
# class Darwin
# -------------

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
    
# =============== INSTRUCTIONS ==================
    
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
        left(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'west')

    def test_left_2 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "west", 5, 5) 
        s.add_creature(creature)
        left(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'south')

    def test_left_3 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "south", 5, 5) 
        s.add_creature(creature)
        left(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'east')

    def test_left_4 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("left")
        creature = Creature(species, "east", 5, 5) 
        s.add_creature(creature)
        left(creature, s.creature_grid)
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
        right(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'east')

    def test_right_2 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "west", 5, 5) 
        s.add_creature(creature)
        right(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'north')

    def test_right_3 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "south", 5, 5) 
        s.add_creature(creature)
        right(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'west')

    def test_right_4 (self) :
        s = Darwin(8, 8)
        species = Species('rover')
        species.add_instruction("right")
        creature = Creature(species, "east", 5, 5) 
        s.add_creature(creature)
        right(creature, s.creature_grid)
        self.assertEqual(creature.direction, 'south')
    
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
        r = Creature(rover, "south", 4, 4)
        f = Creature(food, "south", 5, 4) 
        s.add_creature(f)
        s.add_creature(r)
        infect(r, s.creature_grid)
        self.assertTrue(s.creature_grid[r.x_cor+1][r.y_cor].species, s.creature_grid[r.x_cor][r.y_cor].species)


# ----
# main
# ----

main()
