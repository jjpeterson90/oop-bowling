from classes.frame import frame

class Game:
    
    def __init__(self):
        self.rolls = []
        
    def roll(self, pins_hit):
        self.rolls.append(pins_hit)
        
    def score(self):
        result = 0
        for i in range(20):
            result += self.rolls[i]
        return result