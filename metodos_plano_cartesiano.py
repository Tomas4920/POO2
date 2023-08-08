class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def mostrar(self):
        print(f"Punto: x = {self.x}, y = {self.y}")
        
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        
    def calc_dis(self, p_dif):
        dx = self.x - p_dif.x
        dy = self.y - p_dif.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

p1 = punto(3, 4)
p2 = punto(0, 0)

p1.mostrar()
p1.mover(5, 7)
p1.mostrar()

dis_p = p1.calc_dis(p2)
print(f" Distancia entre los puntos : {dis_p}")
