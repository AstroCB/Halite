import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

class Game:
    def __init__(self, name):
        self.id, self.map = hlt.get_init()
        hlt.send_init(name)

    def start(self):
        while True:
            self.map.get_frame()
            moves = [self.move(square) for square in self.map if square.owner == self.id]
            hlt.send_frame(moves)

    def move(self, square):
        for direction, neighbor in enumerate(self.map.neighbors(square)):
            if neighbor.owner != self.id and neighbor.strength < square.strength:
                return Move(square, direction)
        if square.strength < 5 * square.production:
            return Move(square, STILL)
        else:
            return Move(square, random.choice((NORTH, WEST)))

g = Game("AstroCB")
g.start()
