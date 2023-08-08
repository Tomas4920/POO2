class vehiculo:
    def __init__(self, vel_max, km):
        self.vel_max = vel_max
        self.km = km

vel1 = vehiculo(200, 15000)
vel2 = vehiculo(180, 22000)

print("Vehículo 1 - Velocidad Máxima:", vel1.vel_max)
print("Vehículo 1 - Kilometraje:", vel1.km)

print("Vehículo 2 - Velocidad Máxima:", vel2.vel_max)
print("Vehículo 2 - Kilometraje:", vel2.km)
