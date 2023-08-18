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
    
    def move_agent(self, agent, movement):

        if self.get_space()[agent.get_position().x][agent.get_position().y] == self.AGENT_SPACE:
            self.get_space()[agent.get_position().x][agent.get_position().y] = self.CLEAN_SPACE
        else:
            self.get_space()[agent.get_position().x][agent.get_position().y] = self.DIRTY_SPACE

        match movement:
            case "up":

                if self.get_space()[agent.get_position().x][agent.get_position().y-1] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().x][agent.get_position().y-1] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().x][agent.get_position().y-1] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y-1
                agent.update_position(newPosition)

            case "down":

                if self.get_space()[agent.get_position().x][agent.get_position().y+1] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().x][agent.get_position().y+1] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().x][agent.get_position().y+1] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y+1
                agent.update_position(newPosition)

            case "left":

                if self.get_space()[agent.get_position().x-1][agent.get_position().y] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().x-1][agent.get_position().y] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().x-1][agent.get_position().y] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x-1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)

            case "right":

                if self.get_space()[agent.get_position().x+1][agent.get_position().y] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().x+1][agent.get_position().y] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().x+1][agent.get_position().y] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x+1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)
    
    def clean_dirt(self, agentPosition):
        self.space[agentPosition.x][agentPosition.y] = self.AGENT_SPACE


    def accept_action(self, agent, action):

        match action:
            case "suck":
                if self.get_space()[agent.get_position().x][agent.get_position().y] == self.AGENT_WITH_DIRT_SPACE:
                    return True
                else:
                    return False
            case "up":
                if agent.get_position().y == 0:
                    return False
                else:
                    return True
            case "down":
                if agent.get_position().y == self.size.y - 1:
                    return False
                else:
                    return True
            case "left":
                if agent.get_position().x == 0:
                    return False
                else:
                    return True
            case "right":
                if agent.get_position().x == self.size.x - 1:
                    return False
                else:
                    return True

    def is_dirty(self):
        pass

    def get_performance(self):
        pass

    def print_environment(self):
        matrices.print_matrix(self.space)

    def get_space(self):
        return self.space


class Agent:
    position = Vector2()
    lives = None
    points = 0

    def __init__(self, environment):
        self.set_random_position(environment.size)
        environment.add_agent(self)
        self.set_lives(1000)
    
    def set_random_position(self, environment_size):
        self.position.x = random.randint(0, environment_size.x - 1)
        self.position.y = random.randint(0, environment_size.y - 1)
        print("x:", self.position.x+1, "y:", self.position.y+1)

    def set_lives(self, lives):
        self.lives = lives
    
    def set_points(self, points):
        self.points = points

    def subtract_life(self):
        self.lives -= 1
    
    def up(self, environment):
        if environment.accept_action(self, "up"):
            print("going up")
            environment.move_agent(self, "up")
            

    def down(self, environment):
        if environment.accept_action(self, "down"):
            print("going down")
            environment.move_agent(self, "down")

    def left(self, environment):
        if environment.accept_action(self, "left"):
            print("going left")
            environment.move_agent(self, "left")

    def right(self, environment):
        if environment.accept_action(self, "right"):
            print("going right")
            environment.move_agent(self, "right")

    def suck(self, environment):

        if environment.accept_action(self, "suck"):
            print("sucked")
            environment.clean_dirt(self.position)
        
        pass

    def idle(self):
        pass

    def perspective(self, environment): # Returns true if the current position of the agent is dirty, if not it returns false

        space = environment.get_space()
        if space[self.position.x][self.position.y] == environment.AGENT_WITH_DIRT_SPACE:
            return True
        else:
            return False

    def think(self, environment):
        print("thought")
        self.subtract_life()

        if self.perspective(environment):
            self.suck(environment)
        else:
            self.move_randomly(environment)
    
    def move_randomly(self, environment):
        move = random.randint(1, 4)

        match move:
            case 1:
                self.up(environment)
            case 2:
                self.down(environment)
            case 3:
                self.left(environment)
            case 4:
                self.right(environment)

    def update_position(self, position):
        self.position = position

    def get_position(self):
        return self.position
    
    def get_lives(self):
        return self.lives