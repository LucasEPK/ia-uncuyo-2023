# This module connects all the other modules to execute in conjunction, it creates an environment and an agent to solve a maze with different search algorithms
from nQueens import Environment, Agent
from vectors import Vector2
from os import system
from time import time
import csv

class Interface:
    size = 0 # Size of the environment we want

    showType: bool = None # If true then the agent and environment is shown graphically, if false it repeats the environment with the same size and obstacle rate 10 times and shows the stats
    wantsToExit = False
    environment: Environment = None
    agent: Agent = None


    def __init__(self):
        # Initilialize the program
        self.set_size(8)
        self.menu()
        path = 'C:/Users/Lucas Estudio/Documents/Universidad/2023 2ndo semestre/Inteligencia_Artificial_1/ia-uncuyo-2023/tp5-busquedas-locales/locales-results.csv'
        if not self.wantsToExit:
        

            if self.showType: # This means the user wants to see the agent and environment graphically
                print("===== LEGEND: the columns of the array represents the columns of the chessboard while the numbers inside the positions represents the row in which the queen si placed, the numbers start from 0\n")

                self.create_new_environment_and_agent()
                self.environment.print_environment()
                agent = self.get_agent()
                print("=========== SOLVED WITH HILL CLIMBING ===================")
                chessBoard, steps, solution = agent.solve_by_hillclimbing()
                print(chessBoard[:])
                print(steps)
                print("is it a solution?: ", solution)
                print("=========== SOLVED WITH SIMULATED ANNEALING ===================")
                chessBoardS, stepsS, solutionS = agent.solve_by_simulated_annealing()
                print(chessBoardS[:])
                print(stepsS)
                print("is it a solution?: ", solutionS)
                print("=========== SOLVED WITH GENETIC ALGORITHM ===================")
                chessBoardGA, stepsGA, solutionGA = agent.solve_by_genetic_algorithm()
                print(chessBoardGA[:])
                print(stepsGA)
                print("is it a solution?: ", solutionGA)

            else: # This means the user wants to repeat the algorithms 30 times and see the stats
                csvHeader = ['algorithm_name', 'n_queens', 'run_n', 'explored_states', 'time_taken', 'solution_found']
                csvDataList = []
                for j in range(3):

                    match j:
                        case 0:
                            n_queens = 4
                        case 1:
                            n_queens = 8
                        case 2:
                            n_queens = 10
                    
                    self.set_size(n_queens)

                    print("=============== N_QUEENS ", n_queens)
                    print("")


                    for i in range(30):
                        print("=============== EXECUTION ", i+1)

                        self.create_new_environment_and_agent()
                        agent = self.get_agent()

                        print("=========== SOLVED WITH HILL CLIMBING ===================")
                        startingTime = time()
                        chessBoard, steps, solution = agent.solve_by_hillclimbing()
                        stoppingTime = time()
                        timeTaken = stoppingTime - startingTime
                        print(chessBoard[:])
                        print(steps)
                        print("is it a solution?: ", solution)
                        print("time taken: ", timeTaken)
                        csvData = ['hillClimbing', n_queens, (i+1), steps, timeTaken, solution]
                        csvDataList.append(csvData)

                        print("=========== SOLVED WITH SIMULATED ANNEALING ===================")
                        startingTime = time()
                        chessBoardS, stepsS, solutionS = agent.solve_by_simulated_annealing()
                        stoppingTime = time()
                        timeTaken = stoppingTime - startingTime
                        print(chessBoardS[:])
                        print(stepsS)
                        print("is it a solution?: ", solutionS)
                        print("time taken: ", timeTaken)
                        csvData = ['simulatedAnnealing', n_queens, (i+1), stepsS, timeTaken, solutionS]
                        csvDataList.append(csvData)

                        print("=========== SOLVED WITH GENETIC ALGORITHM ===================")
                        startingTime = time()
                        chessBoardGA, stepsGA, solutionGA = agent.solve_by_genetic_algorithm()
                        stoppingTime = time()
                        timeTaken = stoppingTime - startingTime
                        print(chessBoardGA[:])
                        print(stepsGA)
                        print("is it a solution?: ", solutionGA)
                        print("time taken: ", timeTaken)
                        csvData = ['genetic', n_queens, (i+1), stepsGA, timeTaken, solutionGA]
                        csvDataList.append(csvData)

                        print("")
                
                self.write_csv(csvHeader, csvDataList, path)

    def menu(self):
        print("==================== N-QUEENS LOCAL SEARCH =====================")
        print("===============MENU================")
        print("What do you want to see the AI do?")
        print("1. Show environment and agent graphically")
        print("2. Repeat 30 times, show stats and write csv")
        print("3. Exit")
        option = int(input())

        match option:
            case 1:
                self.showType = True
            case 2:
                self.showType = False
            case 3:
                self.wantsToExit = True
                return

        system("cls")
    
    def create_new_environment_and_agent(self):
        self.set_environment(Environment(self.get_size()))
        self.set_agent(Agent(self.get_environment()))

    def write_csv(self, header, data, path : str):
        # Writes a csv in the path given with the header and data specified (they are lists)
        
        with open(path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)

            writer.writerow(header)

            writer.writerows(data)
    
    # GETTERS
    def get_size(self) -> int:
        return self.size
    
    def get_environment(self):
        return self.environment
    
    def get_agent(self):
        return self.agent
    
    # SETTERS
    def set_environment(self, environment):
        self.environment = environment
    
    def set_agent(self, agent):
        self.agent = agent
    
    def set_size(self, size):
        self.size = size

main = Interface()