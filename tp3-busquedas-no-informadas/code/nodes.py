# Node class to act as a graph
class Node:
    state = None
    parent = None
    action = ""
    pathCost = 0

    def __init__(self, initialState=None, pathCost=None) -> None:
        if initialState != None:
            self.set_state(initialState)
        if pathCost != None:
            self.set_pathCost(pathCost)

    # SETTERS
    def set_state(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def set_pathCost(self, pathCost):
        self.pathCost = pathCost

    # GETTERS

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_pathCost(self):
        return self.pathCost