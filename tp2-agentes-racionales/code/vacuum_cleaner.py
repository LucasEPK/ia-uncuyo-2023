# This module implements an environment and an agent for the vacuum cleaner environment
import matrices
from vectors import Vector2
from random import randint

class Environment:
    space = None
    size = Vector2()
    total_dirt: int = None
    CLEAN_SPACE = "X"
    DIRTY_SPACE = "a"
    AGENT_SPACE = "O"
    AGENT_WITH_DIRT_SPACE = "@"
    

    def __init__(self, size: Vector2, dirtRate: float):
        # Sets the size of the space matrix, creates the matrix, fills it with clean tiles, then adds dirt according to the given dirt rate
        self.set_size(size.y, size.x)
        self.space = matrices.create_matrix(size.y, size.x)
        matrices.fill_matrix(self.space, self.CLEAN_SPACE)
        self.add_dirt(dirtRate)

    def add_dirt(self, dirtRate: float):
        # Adds dirt to the space matrix randomly, the quantity depends on the dirt rate given
        dirtPercentage = dirtRate * 100

        numberOfTilesToFill = round(dirtPercentage * (self.size.x * self.size.y) / 100)
        self.set_total_dirt(numberOfTilesToFill)
        #print("total dirty tiles:", numberOfTilesToFill)
        while numberOfTilesToFill > 0:
            x = randint(0, self.size.x - 1)
            y = randint(0, self.size.y - 1)

            if self.space[y][x] == self.CLEAN_SPACE:
                self.space[y][x] = self.DIRTY_SPACE
                numberOfTilesToFill -= 1

    
    def add_agent(self, agent):
        # Adds the given agent to the space matrix
        x = agent.position.x
        y = agent.position.y

        if self.space[y][x] == self.CLEAN_SPACE:
            self.space[y][x] = self.AGENT_SPACE
        else:
            self.space[y][x] = self.AGENT_WITH_DIRT_SPACE
    
    def move_agent(self, agent, movement: str):
        # Moves the specified agent according to the movement given
        # All of the ifs are to make sure the correct tile is visualized, for example if the agent moves right and the tile it left was dirty, it should stay dirty, and the next tile be the agent or the agent with dirt depending on what it was before

        if self.get_space()[agent.get_position().y][agent.get_position().x] == self.AGENT_SPACE:
            self.get_space()[agent.get_position().y][agent.get_position().x] = self.CLEAN_SPACE
        else:
            self.get_space()[agent.get_position().y][agent.get_position().x] = self.DIRTY_SPACE

        match movement:
            case "up":

                if self.get_space()[agent.get_position().y - 1][agent.get_position().x] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().y - 1][agent.get_position().x] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().y - 1][agent.get_position().x] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y - 1
                agent.update_position(newPosition)

            case "down":

                if self.get_space()[agent.get_position().y + 1][agent.get_position().x] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().y + 1][agent.get_position().x] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().y + 1][agent.get_position().x] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y + 1
                agent.update_position(newPosition)

            case "left":

                if self.get_space()[agent.get_position().y][agent.get_position().x - 1] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().y][agent.get_position().x - 1] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().y][agent.get_position().x - 1] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x - 1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)

            case "right":

                if self.get_space()[agent.get_position().y][agent.get_position().x + 1] == self.CLEAN_SPACE:
                    self.get_space()[agent.get_position().y][agent.get_position().x + 1] = self.AGENT_SPACE
                else:
                    self.get_space()[agent.get_position().y][agent.get_position().x + 1] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x + 1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)
    
    def clean_dirt(self, agentPosition: Vector2):
        # Removes the dirt in the position given and updates the total dirt remaining
        self.space[agentPosition.y][agentPosition.x] = self.AGENT_SPACE

        self.set_total_dirt(self.total_dirt-1)


    def accept_action(self, agent, action: str):
        # Checks if the action given is valid to take with the agent given
        match action:
            case "suck":
                if self.get_space()[agent.get_position().y][agent.get_position().x] == self.AGENT_WITH_DIRT_SPACE:
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


    def is_dirty(self) -> bool:
        # Returns true if the total dirt in the environment is more than 0, if not it returns false
        if self.get_total_dirt() != 0:
            return True
        else:
            return False

    def print_environment(self):
        # Prints the space matrix
        matrices.print_matrix(self.space)

    # Setters
    def set_size(self, x: int, y: int):
        # Sets the size of the environment
        self.size.x = x
        self.size.y = y

    def set_total_dirt(self, total_dirt: int):
        self.total_dirt = total_dirt
    
    # Getters
    def get_space(self):
        return self.space

    def get_performance(self):
        pass
    
    def get_total_dirt(self) -> int:
        return self.total_dirt








class Agent:
    position = Vector2()
    lives: int = None # Lives are taken every time the agent thinks
    points: int = 0
    environment: Environment = None

    def __init__(self, environment: Environment):
        # Sets the environment in which the agent will move in, chooses a random position to start the agent in, adds the agent to the environment and sets the total lives of the agent
        self.set_environment(environment)
        self.set_random_position(environment.size)
        environment.add_agent(self)
        self.set_lives(1000)
    
    def up(self):
        # Goes up in the environment
        if self.get_environment().accept_action(self, "up"):
            self.get_environment().move_agent(self, "up")
            

    def down(self):
        # Goes down in the environment
        if self.get_environment().accept_action(self, "down"):
            self.get_environment().move_agent(self, "down")

    def left(self):
        # Goes left in the environment
        if self.get_environment().accept_action(self, "left"):
            self.get_environment().move_agent(self, "left")

    def right(self):
        # Goes right in the environment
        if self.get_environment().accept_action(self, "right"):
            self.get_environment().move_agent(self, "right")

    def suck(self):
        # Sucks the dirt in the current position if it is dirty
        if self.get_environment().accept_action(self, "suck"):
            self.get_environment().clean_dirt(self.position)
            self.add_point()
        

    def idle(self):
        # Doesn't move
        pass

    def perspective(self) -> bool: # Returns true if the current position of the agent is dirty, if not it returns false

        space = self.get_environment().get_space()
        if space[self.position.y][self.position.x] == self.get_environment().AGENT_WITH_DIRT_SPACE:
            return True
        else:
            return False

    def think(self):
        # Thinks of what the next move is gonna be, if the current position is dirty, it sucks if not it moves in a random direction
        self.subtract_life()

        if self.perspective():
            self.suck()
        else:
            self.move_randomly()
    
    def move_randomly(self):
        # Makes the player move in a random direction
        move = randint(1, 4)

        match move:
            case 1:
                self.up()
            case 2:
                self.down()
            case 3:
                self.left()
            case 4:
                self.right()
    
    def is_alive(self) -> bool:
        # Returns true if the agent lives are more than 0 if not it returns false
        if self.get_lives() <= 0:
            return False
        else:
            return True    

    def add_point(self):
        self.points += 1

    def subtract_life(self):
        self.lives -= 1
    
    def update_position(self, position : Vector2):
        # Updates the agent position with the position given
        self.position = position

    # Setters
    def set_environment(self, environment: Environment):
        self.environment = environment

    def set_random_position(self, environment_size: Vector2):
        # Sets a random position for the agent
        self.position.x = randint(0, environment_size.x - 1)
        self.position.y = randint(0, environment_size.y - 1)

    def set_lives(self, lives: int):
        self.lives = lives
    
    def set_points(self, points: int):
        self.points = points

    # Getters
    def get_environment(self) -> Environment:
        return self.environment

    def get_position(self):
        return self.position
    
    def get_lives(self):
        return self.lives
    
    def get_points(self) -> int:
        return self.points