# This module implements an environment and an agent for the n_queens problem
import matrices
from nodes import Node
from vectors import Vector2
from random import randint, random, choices
import math

class Environment:
    chessBoard = None
    population = None
    size = 0
    
    def __init__(self, size: int, chessBoard= None):
        self.set_size(size)

        if chessBoard == None:
            self.set_random_chessBoard()
        else:
            self.set_chessBoard(chessBoard)
        
        k = size*2

        self.set_population(self.generate_k_random_chessBoards(k))

    
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

    def generate_k_random_chessBoards(self, k):
        size = self.get_size()
        population = []
        for j in range(0, k):
            chessBoard = []

            for i in range(0, size):
                queenPos = randint(0, size-1)
                chessBoard.insert(i, queenPos)
            
            population.append(chessBoard)
        
        return population
            

    def print_environment(self):
        print(self.get_chessBoard()[:])

    # SETTERS
    def set_size(self, size : int):
        # Sets the size of the environment
        self.size = size

    def set_population(self, population):
        self.population = population

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
    
    def get_population(self):
        return self.population





class Agent:
    initialEnvironment: Environment = None

    def __init__(self, initialEnvironment: Environment):
        # Sets the initialEnvironment in which the agent will move in, chooses a random position to start the agent in, adds the agent to the initialEnvironment and sets the total lives of the agent
        self.set_environment(initialEnvironment)
    
    # =================================== MAIN ALGORITHMS ==============================================
    def solve_by_hillclimbing(self):
        # Solves the current environment using a basic hill climbing algorithm, returns the solution's chessboard, number of nodes explored and if the solution is complete
        solutionFound = False
        current = self.make_node(self.get_environment())
        maxSteps = self.get_environment().get_size() # This is because on average classic hillclimbing on 8 queens problem takes 4 steps if succeded and 3 if not, so we round it up to 8, which is the problem size
        for i in range(0, maxSteps):
            neighbor = self.choose_best_neighbor(current)
            if neighbor.get_value() >= current.get_value():
                if current.get_value() == 0:
                    solutionFound = True
                #print("best h reached:", current.get_value())
                return current.get_state(), i+1, solutionFound
            current = neighbor
        
        return current.get_state(), maxSteps, solutionFound
    
    def solve_by_simulated_annealing(self):
        # Solves the current environment using a simulated annealing algorithm returns the solution's chessboard, number of nodes explored and if the solution is complete
        solutionFound = False
        current = self.make_node(self.get_environment())
        maxTime = self.get_environment().get_size()*100 # 2 times the maximum steps of hill climbing
        for time in range(0, maxTime):
            temperature = self.schedule(time, maxTime)

            if temperature == 0:
                if current.get_value() == 0:
                    solutionFound = True
                #print("best h reached:", current.get_value())
                return current.get_state(), time, solutionFound
            
            neighbor = self.choose_random_neighbor(current)

            deltaE = neighbor.get_value() - current.get_value()
            if deltaE < 0:
                current = neighbor
            else:
                probability = math.exp(-deltaE / temperature)
                random_number = random()

                if random_number < probability:
                    current = neighbor

    def solve_by_genetic_algorithm(self):
        # Solves the 8 queens problem using the population in the environment and a genetic algorithm, returns the solution's chessboard, number of nodes explored and if the solution is complete
        solutionFound = False
        population = self.get_environment().get_population()
        time = 0
        maxTime = 200 * self.get_environment().get_size()
        bestIndividual = population[0]
        maxFitness = self.max_fitness(len(population[0]))

        while not solutionFound and time < maxTime:
            newPopulation = []
            for i in range(0, len(population)):
                selection = self.random_selection(population)
                x = selection[0]
                y = selection[1]
                child = self.reproduce(x, y)
                smallProbability = 0.10
                randomNumber = random()
                if randomNumber < smallProbability:
                    child = self.mutate(child)
                newPopulation.append(child)
            population = newPopulation
            bestIndividual = self.best_individual(population)

            if self.fitness(bestIndividual) == maxFitness:
                solutionFound = True
            time += 1
        
        #print("best fitness reached: ", self.fitness(bestIndividual))
        return bestIndividual, time, solutionFound
    
    # ======================================== AUXILIARY FUNCTIONS =====================================
    
    # == FOR HILLCLIMBING ==
    def make_node(self, environment : Environment) -> Node:
        # Makes a node for an environment given and returns it
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
    
    def copy_chessBoard(self, chessBoard):
        # Copies a chessboard list and returns it
        copy = []
        for i in range(0, len(chessBoard)):
            copy.insert(i, chessBoard[i])

        return copy
    
    # == FOR SIMULATED ANNEALING ==
    def schedule(self, time, maxTime):
        # Function to calculate the temperature
        return (maxTime - (time + 1)) * 0.02
    
    def choose_random_neighbor(self, node : Node):
        # Moves a queen randomly in a column to make a new chessboard and returns the node that forms
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
    

    # == FOR GENETIC ALGORITHM ==    
    def max_fitness(self, size):
        # Calculates the max fitness for a chessboard size (calculation based on the fitness function)
        sum1 = 0
        for i in range(1, size):
            sum1 +=i
        
        return sum1
    
    def best_individual(self, population):
        # Calculates the fitness of every chessboard and returns the one with the most fitness
        populationSize = len(population)
        bestIndividual = None
        bestIndividualFitness = 0
        for i in range(0, populationSize):
            currentFitness = self.fitness(population[i])
            if currentFitness > bestIndividualFitness:
                bestIndividualFitness = currentFitness
                bestIndividual = population[i]
        
        return bestIndividual

    def reproduce(self, x, y):
        # Concatenates 2 list from a random crossover point
        chessBoardSize = len(x)
        crossoverPoint = randint(1, chessBoardSize-1)
        return x[:crossoverPoint] + y[crossoverPoint:]

    def mutate(self, child):
        # Changes a random queen to a random row in a child
        chessboardSize = len(child)

        col = randint(0, chessboardSize-1)
        row = randint(0, chessboardSize-1)
        child[col] = row
        return child
    
    def random_selection(self, population):
        # Selects 2 chessboards from the population biased towards better fitnesses

        # Calculates the fitness of every chessboard
        fitnessList = []
        for i in range(0, len(population)):
            fitnessList.insert(i, self.fitness(population[i]))
        
        selected = []
        selected.insert(0, choices(population, fitnessList, k=1)[0])
        selected.insert(1, choices(population, fitnessList, k=1)[0])

        # This is added to not let one node reproduce by itself generating less variety early
        maxRepetition = 1000 # This is because some times the population is the same
        i = 0
        while selected[1] == selected[0] and i < maxRepetition:
            selected[1] = choices(population, fitnessList, k=1)[0]
            i +=1
        return selected
    
    def fitness(self, chessBoard):
        # Calculates the number of non attacking pairs of queens
        size = len(chessBoard)
        fitness = 0

        for i in range(0, size):
            attacking=0

            for j in range(i+1, size):
                #check horizontal
                if chessBoard[j] == chessBoard[i]: #if this happens then they are in the same row so they attack eachother
                    attacking += 1
                
                #check diagonals
                elif chessBoard[j] == chessBoard[i]+(j-i) or chessBoard[j] == chessBoard[i]-(j-i): #j-i represents the increment so j is diagonal to i
                    attacking += 1
            
            # We calculate fitness subtracting the attacking queens to the max number of possible attacking queens in the column i
            fitness += (size-(i+1))-attacking
            
        return fitness

    # SETTERS
    def set_environment(self, initialEnvironment: Environment):
        self.initialEnvironment = initialEnvironment
            
    # GETTERS
    def get_environment(self) -> Environment:
        return self.initialEnvironment