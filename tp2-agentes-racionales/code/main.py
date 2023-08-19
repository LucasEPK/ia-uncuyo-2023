# X es espacio limpio, O es la aspiradora, a es espacio sucio, @ es aspiradora en espacio sucio
from vacuum_cleaner import Environment, Agent
from vectors import Vector2

size = Vector2()
size.x = 4
size.y = 4

env = Environment(size, 0.2)
agent = Agent(env)

print("agent lives: ", agent.get_lives())
env.print_environment()

agent.think()
print("agent lives: ", agent.get_lives())
env.print_environment()