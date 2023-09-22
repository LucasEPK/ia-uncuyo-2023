class Vector2:
    x = None
    y = None

    def __init__(self, y=None, x=None) -> None:
        
        if y != None:
            self.set_y(y)
        if x != None:
            self.set_x(x)

    # SETTERS
    def set_y(self, y):
        self.y = y
    
    def set_x(self, x):
        self.x = x
