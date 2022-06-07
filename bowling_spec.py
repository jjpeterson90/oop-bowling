import unittest
from bowling import Game

class TestGame(unittest.TestCase):
    
    def __init__(self):
        self.setUp()
    
    def setUp(self):
        self.game = Game()
        
    def roll_game(self, pins_hit, rolls):
        for i in range(rolls):
            self.game.roll(pins_hit)
  
    def test_all_gutter_balls(self):
        self.roll_game(0, 20)
        print(f"Test all gutter balls: {self.game.score() == 0}")
        # return f"Test all gutter balls: {self.game.score() == 0}"
        
    def test_all_ones(self):
        self.roll_game(1, 20)
        print(f"Test all ones: {self.game.score() == 20}")
        # return f"Test all ones: {self.game.score() == 20}"
    

TestGame().test_all_gutter_balls()
TestGame().test_all_ones()

