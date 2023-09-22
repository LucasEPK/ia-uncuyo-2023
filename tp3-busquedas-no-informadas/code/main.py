from labyrinth import Environment, Agent
from vectors import Vector2
from random import randint
from os import system

class Interface:

    agentPos = Vector2()
    size = Vector2() # Size of the environment we want

    obstacleRate = 0
    showType: bool = None # If true then the agent and environment is shown graphically, if false it repeats the environment with the same size and obstacle rate 10 times and shows the stats
    wantsToExit = False
    environment: Environment = None
    agent: Agent = None


    def __init__(self):
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
            else: # This means the user wants to repeat the algorithms 30 times and see the stats

                for i in range(30):
                    print("--SIMULATION ", i+1)
                    self.create_new_environment_and_agent()

    def menu(self):
        print("==================== LABYRINTH LOCAL SEARCH =====================")
        print("===============MENU================")
        print("What do you want to see the AI do?")
        print("1. Show environment and agent graphically")
        print("2. Repeat 30 times and show stats")
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