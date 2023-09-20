# This module implements an environment and an agent for the labyrinth environment
import matrices
from nodes import Node
from vectors import Vector2
from random import randint
from os import system

system('color') # This enables color in the cmd on windows

class Environment:
    space = None
    size = Vector2()
    total_obstacle: int = None
    goalPos = Vector2()
    agentPos = Vector2() 
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
                self.set_goalPos(y, x)
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

        self.set_agentPos(y, x)
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

    def goal_test(self, pos : Vector2):
        # Checks if the given position is the same as the goal position
        goalPos = self.get_goalPos

        if pos.x == goalPos.x and pos.y == goalPos.y:
            return True
        else:
            return False

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

    # SETTERS
    def set_size(self, y: int, x: int):
        # Sets the size of the environment
        self.size.x = x
        self.size.y = y

    def set_goalPos(self, y: int, x: int):
        # Sets the goalPos of the environment
        self.goalPos.x = x
        self.goalPos.y = y

    def set_agentPos(self, y: int, x: int):
        # Sets the agentPos of the environment
        self.agentPos.x = x
        self.agentPos.y = y

    def set_total_obstacle(self, total_obstacle: int):
        self.total_obstacle = total_obstacle
    
    # GETTERS
    def get_size(self) -> Vector2:
        return self.size
    
    def get_goalPos(self):
        return self.goalPos
    
    def get_agentPos(self):
        return self.agentPos

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

    def solve_by_bfs(self):
        environment = self.get_environment()
        node = Node(self.position, 0)
        if environment.goal_test(node.get_state()):
            pass

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