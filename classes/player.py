class Player:
    
    def __init__(self, name):
        self.name = name
        self.frames = []
        
    def calc_score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            print(frame.balls, i)
            if i == 9:
                if frame.is_strike():
                    score+= 10 + frame.balls[1] + frame.balls[2]
                elif frame.is_spare():
                    score += 10 + frame.balls[2]
                else:
                    score += frame.balls[0] + frame.balls[1]
            
            elif frame.is_strike():
                score += 10 + self.frames[i+1].balls[0]
                if len(self.frames[i+1].balls) > 1:
                    score += self.frames[i+1].balls[1]
                else:
                    score+= self.frames[i+2].balls[0]
            
            elif frame.is_spare():
                score += 10 + self.frames[i+1].balls[0]
                
            else:
                score+= frame.balls[0] + frame.balls[1]
                      
        return score