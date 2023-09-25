# Node class to act as a graph
class Node:
    state = None
    value = None

    def __init__(self, initialState=None, value=None) -> None:
        if initialState != None:
            self.set_state(initialState)
        if value != None:
            self.set_value(value)

    # SETTERS
    def set_state(self, state):
        self.state = state

    def set_value(self, value):
        self.value = value

    # GETTERS
    def get_state(self):
        return self.state
    
    def get_value(self):
        return self.value