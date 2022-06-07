class Frame:
    
    def __init__(self, balls):
        self.balls = balls
        
    def is_strike(self):
        return self.balls[0] == 10

    def is_spare(self):
        return len(self.balls) > 1 and self.balls[0] + self.balls[1] == 10