import math

class circulo:
    def __init__(self, c, r):
        self.c = c
        self.r = r
    
    def area(self):
        return math.pi * self.r**2
    
    def perimetro(self):
        return 2 * math.pi * self.r
    
    def p_pertenece(self, punto):
        
        dis_c = math.sqrt((punto[0] - self.c[0])**2 + (punto[1] - self.c[1])**2)
        return dis_c <= self.r

c = (0, 0)
r = 9
circ = circulo (c, r)

print(" Área: ", circ.area())
print(" Perímetro: ", circ.perimetro())

p1 = (1, 2)
p2 = (8, 5)

print(" Punto (1, 2) pertenece al círculo: ", circ.p_pertenece(p1))
print(" Punto (8, 5) pertenece al círculo: ", circ.p_pertenece(p2))
