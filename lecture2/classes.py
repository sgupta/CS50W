class Numops:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def multiply(self):
        return self.x*self.y
    
z = Numops(5,6)
print(z.multiply())

