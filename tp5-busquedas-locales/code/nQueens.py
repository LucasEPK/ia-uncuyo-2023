# This module implements an environment and an agent for the labyrinth environment
import matrices
from nodes import Node
from vectors import Vector2
from random import randint, random
import math

class Environment:
    chessBoard = None
    size = 0
    
    def __init__(self, size: int, chessBoard= None):
        self.set_size(size)

        if chessBoard == None:
            self.set_random_chessBoard()
        else:
            self.set_chessBoard(chessBoard)
    
    def h(self):
        # Heuristic function that counts the total number of pair of queens that are attacking eachother and returns it
        h=0
        board = self.get_chessBoard()
        l_board = len(board)

        for i in range(0, l_board):

            for j in range(i+1, l_board):
                #check horizontal
                if board[j] == board[i]: #if this happens then they are in the same row so they attack eachother
                    h += 1
                
                #check diagonals
                elif board[j] == board[i]+(j-i) or board[j] == board[i]-(j-i): #j-i represents the increment so j is diagonal to i
                    h += 1
            
        return h

    def print_environment(self):
        print(self.get_chessBoard()[:])

    # SETTERS
    def set_size(self, size : int):
        # Sets the size of the environment
        self.size = size

    def set_chessBoard(self, chessBoard):
        self.chessBoard = chessBoard
    
    def set_random_chessBoard(self):
        # Creates a chess board with N randomly placed queens represented by an array, the position represents the column while the numbers in the array represents the row in which the queen is placed
        size = self.get_size()
        chessBoard = []

        for i in range(0, size):
            queenPos = randint(0, size-1)
            chessBoard.insert(i, queenPos)
        
        self.chessBoard = chessBoard

    
    # GETTERS
    def get_size(self) -> int:
        return self.size

    def get_chessBoard(self):
        return self.chessBoard





class Agent:
    initialEnvironment: Environment = None

    def __init__(self, initialEnvironment: Environment):
        # Sets the initialEnvironment in which the agent will move in, chooses a random position to start the agent in, adds the agent to the initialEnvironment and sets the total lives of the agent
        self.set_environment(initialEnvironment)
    
    def solve_by_hillclimbing(self):
        current = self.make_node(self.get_environment())
        maxSteps = self.get_environment().get_size() # This is because on average classic hillclimbing on 8 queens problem takes 4 steps if succeded and 3 if not, so we round it up to 8, which is the problem size
        for i in range(0, maxSteps):
            neighbor = self.choose_best_neighbor(current)
            if neighbor.get_value() >= current.get_value():
                if current.get_value() == 0:
                    print("solution lol")
                else:
                    print("reached local minimum, h = ", current.get_value())
                return current.get_state(), i+1
            current = neighbor
        print("maxSteps reached")
        return current.get_state(), maxSteps
    
    def solve_by_simulated_annealing(self):
        current = self.make_node(self.get_environment())
        maxTime = self.get_environment().get_size()*13 # 2 times the maximum steps of hill climbing
        for time in range(0, maxTime):
            temperature = self.schedule(time, maxTime)

            if temperature == 0:
                if current.get_value() == 0:
                    print("solution")
                else:
                    print("best attempt:", current.get_value())
                return current.get_state(), time
            
            neighbor = self.choose_random_neighbor(current)

            evaluation = neighbor.get_value() - current.get_value()
            if evaluation < 0:
                current = neighbor
            else:
                probability = 1 / math.exp(-evaluation / temperature)
                random_number = random()

                if random_number < probability:
                    current = neighbor


    def make_node(self, environment : Environment) -> Node:
        chessBoard = environment.get_chessBoard()

        node = Node()
        node.set_state(chessBoard)
        h = environment.h()
        node.set_value(h)
        return node

    def choose_best_neighbor(self, node : Node):
        # Generates new chess boards moving only 1 queen in her column and calculates the heuristic for every possible movement, then chooses the movement with the lowest heuristic and returns it as a node
        chessBoard = self.copy_chessBoard(node.get_state())
        chessBoardSize = len(chessBoard)
        environment = Environment(chessBoardSize, chessBoard)
        environmentH = environment.h()
        bestNeighbor = environment

        bestH = environmentH

        for j in range(0, chessBoardSize):
            for i in range(0, chessBoardSize):
                if i != chessBoard[j]:
                    newChessBoard = self.copy_chessBoard(chessBoard)
                    newChessBoard[j] = i
                    newEnvironment = Environment(chessBoardSize, newChessBoard)
                    newEnvironmentH = newEnvironment.h()

                    if newEnvironmentH < bestH:
                        bestNeighbor = newEnvironment
                        bestH = newEnvironmentH
        
        neighborNode = Node(bestNeighbor.get_chessBoard(), bestH)
        return neighborNode
    
    def choose_random_neighbor(self, node : Node):

        chessBoard = self.copy_chessBoard(node.get_state())
        chessBoardSize = len(chessBoard)

        randomCol = randint(0, chessBoardSize-1)
        randomRow = randint(0, chessBoardSize-1)

        while chessBoard[randomCol] == randomRow:
            # Checks if the random position isn't the same as the one in the current board, if it is we roll again
            randomCol = randint(0, chessBoardSize-1)
            randomRow = randint(0, chessBoardSize-1)
        
        chessBoard[randomCol] = randomRow
        environment = Environment(chessBoardSize, chessBoard)
        environmentH = environment.h()
        neighbor = Node(environment.get_chessBoard(), environmentH)

        return neighbor

    def schedule(self, time, maxTime):
        return (maxTime - (time + 1)) * 0.3
    
    def copy_chessBoard(self, chessBoard):
        copy = []
        for i in range(0, len(chessBoard)):
            copy.insert(i, chessBoard[i])

        return copy

    # Setters
    def set_environment(self, initialEnvironment: Environment):
        self.initialEnvironment = initialEnvironment
            
    # Getters
    def get_environment(self) -> Environment:
        return self.initialEnvironment