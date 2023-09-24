# This module connects all the other modules to execute in conjunction, it creates an environment and an agent to solve a maze with different search algorithms
from labyrinth import Environment, Agent
from vectors import Vector2
from random import randint
from os import system
import csv

class Interface:

    agentPos = Vector2()
    size = Vector2() # Size of the environment we want

    obstacleRate = 0
    showType: bool = None # If true then the agent and environment is shown graphically, if false it repeats the environment with the same size and obstacle rate 10 times and shows the stats
    wantsToExit = False
    environment: Environment = None
    agent: Agent = None


    def __init__(self):
        # Initilialize the program
        self.set_obstacleRate(0.08)
        self.set_size(100, 100)
        self.set_agentPos(randint(0, 99), randint(0, 99))
        self.menu()
        if not self.wantsToExit:
        

            if self.showType: # This means the user wants to see the agent and environment graphically
                print("===== LEGEND: 0 = empty tile, 1 = obstacle tile, 2 = agent tile, 3 = goal tile =======\n")

                self.create_new_environment_and_agent()
                self.environment.print_environment()
                agent = self.get_agent()
                size = self.get_size()

                print("============================ Solved with BFS ===============================")
                solutionBFS, nodesExploredBFS = agent.solve_by_bfs()
                print("Steps:")
                print(solutionBFS[:])
                print("Nodes explored:")
                print(nodesExploredBFS)

                print("============================ Solved with DFS ===============================")
                solutionDFS, nodesExploredDFS = agent.solve_by_dfs()
                print("Steps:")
                print(solutionDFS[:])
                print("Nodes explored:")
                print(nodesExploredDFS)

                print("============================ Solved with DLS ===============================")
                solutionDLS, nodesExploredDLS = agent.solve_by_dls(round((size.x*size.y)/2)) # I chose the limit to be half of the matrix
                print("Steps:")
                if solutionDLS != None:
                    print(solutionDLS[:])
                else:
                    print("Solution not found before limit")
                print("Nodes explored:")
                print(nodesExploredDLS)

                print("============================ Solved with UCS ===============================")
                solutionUCS, nodesExploredUCS = agent.solve_by_ucs()
                print("Steps:")
                print(solutionUCS[:])
                print("Nodes explored:")
                print(nodesExploredUCS)

                print("============================ Solved with A* ===============================")
                solutionAstar, nodesExploredAstar = agent.solve_by_Astar()
                print("Steps:")
                print(solutionAstar[:])
                print("Nodes explored:")
                print(nodesExploredAstar)
            else: # This means the user wants to repeat the algorithms 30 times and see the stats
                csvHeader = ['algorithm_name', 'run_n', 'explored_states', 'solution_found']
                csvDataList = []
                for i in range(30):
                    print("=============== EXECUTION ", i+1)

                    self.create_new_environment_and_agent()
                    agent = self.get_agent()
                    size = self.get_size()

                    print("============================ Solved with BFS ===============================")
                    solutionBFS, nodesExploredBFS = agent.solve_by_bfs()
                    print("Nodes explored:")
                    print(nodesExploredBFS)
                    solutionFound = len(solutionBFS) != 0
                    csvData = ['BFS', (i+1), nodesExploredBFS, solutionFound]
                    csvDataList.append(csvData)

                    print("============================ Solved with DFS ===============================")
                    solutionDFS, nodesExploredDFS = agent.solve_by_dfs()
                    print("Nodes explored:")
                    print(nodesExploredDFS)
                    solutionFound = len(solutionDFS) != 0
                    csvData = ['DFS', (i+1), nodesExploredDFS, solutionFound]
                    csvDataList.append(csvData)

                    print("============================ Solved with DLS ===============================")
                    solutionDLS, nodesExploredDLS = agent.solve_by_dls(round((size.x*size.y)/2)) # I chose the limit to be half of the matrix
                    solutionFound = True
                    if solutionDLS == None:
                        print("Solution not found before limit")
                        solutionFound = False
                    print("Nodes explored:")
                    print(nodesExploredDLS)
                    csvData = ['DLS', (i+1), nodesExploredDLS, solutionFound]
                    csvDataList.append(csvData)

                    print("============================ Solved with UCS ===============================")
                    solutionUCS, nodesExploredUCS = agent.solve_by_ucs()
                    print("Nodes explored:")
                    print(nodesExploredUCS)
                    solutionFound = len(solutionUCS) != 0
                    csvData = ['UCS', (i+1), nodesExploredUCS, solutionFound]
                    csvDataList.append(csvData)

                    print("============================ Solved with A* ===============================")
                    solutionAstar, nodesExploredAstar = agent.solve_by_Astar()
                    print("Nodes explored:")
                    print(nodesExploredAstar)
                    solutionFound = len(solutionAstar) != 0
                    csvData = ['A*', (i+1), nodesExploredAstar, solutionFound]
                    csvDataList.append(csvData)
                
                self.write_csv(csvHeader, csvDataList)

    def menu(self):
        print("==================== LABYRINTH LOCAL SEARCH =====================")
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
        self.set_environment(Environment(self.get_size(), self.get_obstacleRate()))
        self.set_agent(Agent(self.get_environment()))

    def write_csv(self, header, data):
        # Writes a csv in the path below with the header and data specified (they are lists)
        path = 'C:/Users/Lucas Estudio/Documents/Universidad/2023 2ndo semestre/Inteligencia_Artificial_1/ia-uncuyo-2023/tp4-busquedas-informadas/informada-results.csv'
        
        with open(path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)

            writer.writerow(header)

            writer.writerows(data)
    
    # GETTERS
    def get_size(self) -> Vector2:
        return self.size
    
    def get_obstacleRate(self) -> float:
        return self.obstacleRate
    
    def get_environment(self):
        return self.environment
    
    def get_agent(self):
        return self.agent
    
    # SETTERS
    def set_environment(self, environment):
        self.environment = environment
    
    def set_agent(self, agent):
        self.agent = agent
    
    def set_obstacleRate(self, obstacleRate):
        self.obstacleRate = obstacleRate
    
    def set_size(self, y, x):
        self.size.x = x
        self.size.y = y

    def set_agentPos(self, y, x):
        self.agentPos.x = x
        self.agentPos.y = y

main = Interface()