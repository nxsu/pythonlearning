class Point:

    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x + other
        y = self.y + other.y + other
        return Point(x, y)