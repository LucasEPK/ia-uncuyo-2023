import matrices
from vectors import Vector2
import random

class Environment:
    space = None
    size = Vector2()
    CLEAN_SPACE = "X"
    DIRTY_SPACE = "a"
    AGENT_SPACE = "O"
    AGENT_WITH_DIRT_SPACE = "@"
    

    def __init__(self, size, dirtRate):
        # Sets the size of the space matrix, creates the matrix, fills it with clean tiles, then adds dirt according to the given dirt rate
        self.set_size(size.x, size.y)
        self.space = matrices.create_matrix(size.x, size.y)
        matrices.fill_matrix(self.space, self.CLEAN_SPACE)
        self.add_dirt(dirtRate)

    def add_dirt(self, dirtRate):
        # Adds dirt to the space matrix randomly, the quantity depends on the dirt rate given
        dirtPercentage = dirtRate * 100

        numberOfTilesToFill = round(dirtPercentage * (self.size.x * self.size.y) / 100)
        print("total dirty tiles:", numberOfTilesToFill)
        while numberOfTilesToFill > 0:
            x = random.randint(0, self.size.x - 1)
            y = random.randint(0, self.size.y - 1)

            if self.space[x][y] == self.CLEAN_SPACE:
                self.space[x][y] = self.DIRTY_SPACE
                numberOfTilesToFill -= 1

    def set_size(self, x, y):
        # Sets the size of the environment
        self.size.x = x
        self.size.y = y
    
    def add_agent(self, agent):
        x = agent.position.x
        y = agent.position.y

        if self.space[x][y] == self.CLEAN_SPACE:
            self.space[x][y] = self.AGENT_SPACE
        else:
            self.space[x][y] = self.AGENT_WITH_DIRT_SPACE

    def accept_action(self, action):
        pass

    def is_dirty(self):
        pass

    def get_performance(self):
        pass

    def print_environment(self):
        matrices.print_matrix(self.space)


class Agent:
    position = Vector2()

    def __init__(self, environment):
        self.set_random_position(environment.size)
    
    def set_random_position(self, environment_size):
        self.position.x = random.randint(0, environment_size.x - 1)
        self.position.y = random.randint(0, environment_size.y - 1)
        print("x:", self.position.x+1, "y:", self.position.y+1)