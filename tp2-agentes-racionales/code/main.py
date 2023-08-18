# X es espacio limpio, O es la aspiradora, a es espacio sucio, @ es aspiradora en espacio sucio
from environment import Environment
from vectors import Vector2

size = Vector2()
size.x = 64
size.y = 64

env = Environment(size,0,0.5)