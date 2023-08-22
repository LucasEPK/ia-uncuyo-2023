from vacuum_cleaner import Environment, Agent
from vectors import Vector2
from os import system

class Interface:
    size = Vector2()

    dirtRate = 0
    showType: bool = None # If true then the agent and environment is shown graphically, if false it repeats the environment with the same size and dirt rate 10 times and shows the stats
    wantsToExit = False
    environment: Environment = None
    agent: Agent = None


    def __init__(self):
        self.menu()
        if not self.wantsToExit:
        

            if self.showType:
                print("X = empty tile, O = empty tile with agent, a = dirty tile, @ = dirty tile with agent\n")

                self.create_new_environment_and_agent()
                print("agent lives: ", self.agent.get_lives())
                self.environment.print_environment()
                while self.agent.is_alive() and self.environment.is_dirty():
                    self.agent.think()
                    print("points:", self.agent.get_points())
                    print("agent used lives: ", 1000 - self.agent.get_lives())
                    #print("environment total dirt: ", self.environment.get_total_dirt())
                    self.environment.print_environment()

            else:

                for i in range(10):
                    print("--SIMULATION ", i+1)
                    self.create_new_environment_and_agent()
                    #print("agent lives: ", self.agent.get_lives())
                    while self.agent.is_alive() and self.environment.is_dirty():
                        self.agent.think()
                    #print("----------------simulation ended----------------")
                    print("points:", self.agent.get_points())
                    print("agent used lives: ", 1000 - self.agent.get_lives())
                    #print("environment total dirt: ", self.environment.get_total_dirt())

                


    def menu(self):

        print("===============MENU================")
        print("Select environment size")
        print("1. 2x2")
        print("2. 4x4")
        print("3. 8x8")
        print("4. 16x16")
        print("5. 32x32")
        print("6. 64x64")
        print("7. 128x128")
        print("8. Exit")
        option = int(input())

        match option:
            case 1:
                self.size.x = 2
                self.size.y = 2
            case 2:
                self.size.x = 4
                self.size.y = 4
            case 3:
                self.size.x = 8
                self.size.y = 8
            case 4:
                self.size.x = 16
                self.size.y = 16
            case 5:
                self.size.x = 32
                self.size.y = 32
            case 6:
                self.size.x = 64
                self.size.y = 64
            case 7:
                self.size.x = 128
                self.size.y = 128
            case 8:
                self.wantsToExit = True
                return
        system("cls")

        print("===============MENU================")
        print("Select dirt rate")
        print("1. 0.1")
        print("2. 0.2")
        print("3. 0.4")
        print("4. 0.8")
        print("5. Exit")
        option = int(input())

        match option:
            case 1:
                self.dirtRate = 0.1
            case 2:
                self.dirtRate = 0.2
            case 3:
                self.dirtRate = 0.4
            case 4:
                self.dirtRate = 0.8
            case 5:
                self.wantsToExit = True
                return
        system("cls")

        print("===============MENU================")
        print("Select show type")
        print("1. Show environment and agent graphically")
        print("2. Repeat 10 times and show stats")
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
        self.set_environment(Environment(self.get_size(), self.get_dirt_rate()))
        self.set_agent(Agent(self.get_environment()))

    def get_size(self) -> Vector2:
        return self.size
    
    def get_dirt_rate(self) -> float:
        return self.dirtRate
    
    def get_environment(self):
        return self.environment
    
    def get_agent(self):
        return self.agent
    
    def set_environment(self, environment):
        self.environment = environment
    
    def set_agent(self, agent):
        self.agent = agent

main = Interface()
print("")
print("Size:", main.get_size().x, "x", main.get_size().y)
print("Dirt rate:", main.get_dirt_rate())