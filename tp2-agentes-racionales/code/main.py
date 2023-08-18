# X es espacio limpio, O es la aspiradora, a es espacio sucio, @ es aspiradora en espacio sucio
from vacuum_cleaner import Environment, Agent
from vectors import Vector2

size = Vector2()
size.x = 2
size.y = 2

env = Environment(size, 0.5)
agent = Agent(env)

print("agent lives: ", agent.get_lives())
env.print_environment()

agent.think(env)
print("agent lives: ", agent.get_lives())
env.print_environment()