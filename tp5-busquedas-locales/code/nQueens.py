# This module implements an environment and an agent for the labyrinth environment
import matrices
from nodes import Node
from vectors import Vector2
from random import randint

class Environment:
    chessBoard = None
    size = 0
    
    def __init__(self, size: int, chessBoard= None):
        self.set_size(size)

        if chessBoard == None:
            self.set_random_chessBoard()
        else:
            self.set_chessboard(chessBoard)
    
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

    def make_node(self, environment : Environment):
        chessBoard = environment.get_chessBoard()

        node = Node()
        node.set_state(chessBoard)
        h = environment.h()
        node.set_value(h)

    def choose_best_neighbor(self, node : Node):
        chessBoard = node.get_state()
        chessBoardSize = len(chessBoard)
        bestNeighbor = None
        bestH = chessBoardSize*chessBoardSize # This is used to have a scalable bigger than the worst h possible

        for j in range(0, chessBoardSize):
            for i in range(0, chessBoardSize):
                if i != chessBoard[j]:
                    newChessBoard = chessBoard
                    newChessBoard[j] = i
                    newEnvironment = Environment(chessBoardSize, newChessBoard)
                    newEnvironmentH = newEnvironment.h()

                    if newEnvironmentH < bestH:
                        bestNeighbor = newEnvironment
                        bestH = newEnvironmentH
        
        neighborNode = Node(bestNeighbor.get_chessBoard(), bestH)
        return neighborNode



    # Setters
    def set_environment(self, initialEnvironment: Environment):
        self.initialEnvironment = initialEnvironment
            
    # Getters
    def get_environment(self) -> Environment:
        return self.initialEnvironment