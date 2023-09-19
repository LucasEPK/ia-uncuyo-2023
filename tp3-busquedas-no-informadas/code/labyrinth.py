# This module implements an environment and an agent for the labyrinth environment
import matrices
from vectors import Vector2
from random import randint
from os import system

system('color') # This enables color in the cmd on windows

class Environment:
    space = None
    size = Vector2()
    total_obstacle: int = None
    EMPTY_TILE = "0"
    OBSTACLE_TILE = "1"
    AGENT_TILE = "2"
    GOAL_TILE = "3"
    

    def __init__(self, size: Vector2, obstacleRate: float):
        # Sets the size of the space matrix, creates the matrix, fills it with empty tiles, then adds obstacles according to the given obstacle rate
        self.set_size(size.y, size.x)
        self.space = matrices.create_matrix(size.y, size.x)
        matrices.fill_matrix(self.get_space(), self.EMPTY_TILE)
        self.add_obstacles(obstacleRate)
        self.add_goal()

    def add_obstacles(self, obstacleRate: float):
        # Adds obstacles to the space matrix randomly, the quantity depends on the obstacle rate given
        obstaclePercentage = obstacleRate * 100
        space = self.get_space()

        numberOfTilesToFill = round(obstaclePercentage * (self.size.x * self.size.y) / 100)
        self.set_total_obstacle(numberOfTilesToFill)
        while numberOfTilesToFill > 0:
            x = randint(0, self.size.x - 1)
            y = randint(0, self.size.y - 1)

            if space[y][x] == self.EMPTY_TILE:
                space[y][x] = self.OBSTACLE_TILE
                numberOfTilesToFill -= 1

    def add_goal(self):
        # Adds a goal tile in a random position in the space matrix
        space = self.get_space()
        spaceSize = self.get_size()
        repeat = True
        while repeat:
            x = randint(0, spaceSize.x-1)
            y = randint(0, spaceSize.y-1)

            if space[y][x] == self.EMPTY_TILE:
                repeat = False
                space[y][x] = self.GOAL_TILE
        
    
    def move_agent(self, agent, movement: str):
        # Moves the specified agent according to the movement given
        # All of the ifs are to make sure the correct tile is visualized, for example if the agent moves right and the tile it left was dirty, it should stay dirty, and the next tile be the agent or the agent with dirt depending on what it was before
        space = self.get_space()

        if space[agent.get_position().y][agent.get_position().x] == self.AGENT_TILE:
            space[agent.get_position().y][agent.get_position().x] = self.EMPTY_TILE
        else:
            space[agent.get_position().y][agent.get_position().x] = self.OBSTACLE_TILE

        match movement:
            case "up":

                if space[agent.get_position().y - 1][agent.get_position().x] == self.EMPTY_TILE:
                    space[agent.get_position().y - 1][agent.get_position().x] = self.AGENT_TILE
                else:
                    space[agent.get_position().y - 1][agent.get_position().x] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y - 1
                agent.update_position(newPosition)

            case "down":

                if space[agent.get_position().y + 1][agent.get_position().x] == self.EMPTY_TILE:
                    space[agent.get_position().y + 1][agent.get_position().x] = self.AGENT_TILE
                else:
                    space[agent.get_position().y + 1][agent.get_position().x] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x
                newPosition.y = agent.get_position().y + 1
                agent.update_position(newPosition)

            case "left":

                if space[agent.get_position().y][agent.get_position().x - 1] == self.EMPTY_TILE:
                    space[agent.get_position().y][agent.get_position().x - 1] = self.AGENT_TILE
                else:
                    space[agent.get_position().y][agent.get_position().x - 1] = self.AGENT_WITH_DIRT_SPACE

                newPosition = Vector2()
                newPosition.x = agent.get_position().x - 1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)

            case "right":

                if space[agent.get_position().y][agent.get_position().x + 1] == self.EMPTY_TILE:
                    space[agent.get_position().y][agent.get_position().x + 1] = self.AGENT_TILE
                else:
                    space[agent.get_position().y][agent.get_position().x + 1] = self.AGENT_WITH_DIRT_SPACE
                
                newPosition = Vector2()
                newPosition.x = agent.get_position().x + 1
                newPosition.y = agent.get_position().y
                agent.update_position(newPosition)

    def accept_agent_pos(self, y, x):
        # Checks if the position given isn't already occopied
        space = self.space

        if space[y][x] == self.EMPTY_TILE:
            return True
        else:
            return False

    def add_agent(self, agent):
        # Adds the given agent to the space matrix
        x = agent.get_position().x
        y = agent.get_position().y
        space = self.get_space()

        space[y][x] = self.AGENT_TILE

    def accept_action(self, agent, action: str):
        # Checks if the action given is valid to take with the agent given
        agentPos = agent.get_position()
        spaceSize = self.size()
        match action:
            case "up":
                if agentPos.y == 0:
                    return False
                else:
                    return True
            case "down":
                if agentPos.y == spaceSize.y - 1:
                    return False
                else:
                    return True
            case "left":
                if agentPos.x == 0:
                    return False
                else:
                    return True
            case "right":
                if agentPos.x == spaceSize.x - 1:
                    return False
                else:
                    return True

    def print_environment(self):
        # Prints the space matrix with colors
        GREEN = "\u001b[42m"
        YELLOW = "\u001b[43m"
        ENDC = "\u001b[0m"

        space = self.get_space()

        rows = len(space)
        for i in range(rows):
            columns = len(space[i])
            for j in range(columns):
                if j == 0:
                    print(i, ":  ", end='')
                
                if space[i][j] == self.AGENT_TILE:
                    print(GREEN + str(space[i][j]) + ENDC, end='')
                elif space[i][j] == self.GOAL_TILE:
                    print(YELLOW + str(space[i][j]) + ENDC, end='')
                else:
                    print(space[i][j], end='')
                
            print()

    # Setters
    def set_size(self, x: int, y: int):
        # Sets the size of the environment
        self.size.x = x
        self.size.y = y

    def set_total_obstacle(self, total_obstacle: int):
        self.total_obstacle = total_obstacle
    
    # Getters
    def get_size(self) -> Vector2:
        return self.size
    
    def get_space(self):
        return self.space
    
    def get_total_obstacle(self) -> int:
        return self.total_obstacle





class Agent:
    position = Vector2()
    environment: Environment = None

    def __init__(self, environment: Environment):
        # Sets the environment in which the agent will move in, chooses a random position to start the agent in, adds the agent to the environment and sets the total lives of the agent
        self.set_environment(environment)
        self.set_random_position(environment.size)
        environment.add_agent(self)
    
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
        
    def think(self):
        # Thinks of what the next move is gonna be, if the current position is dirty, it sucks if not it moves in a random direction
        self.subtract_life()

        if self.perspective():
            self.suck()
        else:
            self.move_randomly()
    
    def dont_think(self):
        # Substracts a life and does a random action
        self.subtract_life()
        self.do_randomly()

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
    
    def do_randomly(self):
        # Does a random action, choosing between going up, down, left or right but also sucking, and idling
        do = randint(1, 6)

        match do:
            case 1:
                self.up()
            case 2:
                self.down()
            case 3:
                self.left()
            case 4:
                self.right()
            case 5:
                self.suck()
            case 6:
                self.idle() 
    
    def update_position(self, position : Vector2):
        # Updates the agent position with the position given
        self.position = position

    # Setters
    def set_environment(self, environment: Environment):
        self.environment = environment

    def set_position(self, y, x):
        self.position.y = y
        self.position.x = x

    def set_random_position(self, environmentSize: Vector2):
        # Sets a random position for the agent
        repeat = True
        environment = self.get_environment()
        while repeat:
            x = randint(0, environmentSize.x-1)
            y = randint(0, environmentSize.y-1)

            if environment.accept_agent_pos(y, x):
                repeat = False
                self.set_position(y, x)
            

    # Getters
    def get_environment(self) -> Environment:
        return self.environment

    def get_position(self):
        return self.position