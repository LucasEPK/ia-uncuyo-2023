import matrices
from vectors import Vector2
import random

class Environment:
    space = None
    size = Vector2()
    CLEAN_SPACE = "X"
    DIRTY_SPACE = "a"
    

    def __init__(self, size, initialPos, dirtRate):
        self.set_size(size.x, size.y)
        self.space = matrices.create_matrix(size.x, size.y)
        matrices.fill_matrix(self.space, self.CLEAN_SPACE)
        self.fill_with_dirt(dirtRate)
        self.print_environment()

    def fill_with_dirt(self, dirtRate):
        dirtPercentage = dirtRate * 100

        numberOfTilesToFill = round(dirtPercentage * (self.size.x * self.size.y) / 100)

        while numberOfTilesToFill > 0:
            x = random.randint(0, self.size.x - 1)
            y = random.randint(0, self.size.y - 1)

            if self.space[x][y] == self.CLEAN_SPACE:
                self.space[x][y] = self.DIRTY_SPACE
                numberOfTilesToFill -= 1

    def set_size(self, x, y):
        self.size.x = x
        self.size.y = y

    def accept_action(self, action):
        pass

    def is_dirty(self):
        pass

    def get_performance(self):
        pass

    def print_environment(self):
        matrices.print_matrix(self.space)