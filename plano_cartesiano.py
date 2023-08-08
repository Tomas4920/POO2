class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def dis(self, punto_dif):
        dx = self.x - punto_dif.x
        dy = self.y - punto_dif.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

p1 = punto(2, 3)
p2 = punto(-1, 4)

print(" Punto 1: ", p1)
print(" Punto 2: ", p2)

dis_p = p1.dis(p2)
print(" Distancia entre los puntos: ", dis_p)
