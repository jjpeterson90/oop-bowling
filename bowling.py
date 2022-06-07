from classes.frame import Frame
from classes.player import Player
import random


def lucky_rand(n):
    return max(random.randint(0, n), random.randint(0, n))


class Game:

    def __init__(self, players):
        self.players = players
        self.current_frame = 0

    def play_a_game(self):
        for i in range(10):
            self.bowl_frame()
        for player in self.players:
            print(
                f"The final score for {player.name} is {player.calc_score()}")

    def bowl_frame(self):
        self.current_frame += 1
        for player in self.players:
            balls = []

            # first throw
            balls.append(lucky_rand(10))
            if balls[0] < 10:
                
                # if they didn't knock down all the pins, they get a second chance
                balls.append(lucky_rand(10-balls[0]))

                # on the final frame fo the game, you get a third ball if you throw a spare
                if balls[0] + balls[1] == 10 and self.current_frame == 10:
                    balls.append(lucky_rand(10))

            # if they get a strike on the last frame, they get 2 extra balls
            if balls[0] == 10 and self.current_frame == 10:
                balls.append(lucky_rand(10))
                if balls[1] == 10:
                    balls.append(lucky_rand(10))
                else:
                    balls.append(lucky_rand(10 - balls[1]))

            player.frames.append(Frame(balls))