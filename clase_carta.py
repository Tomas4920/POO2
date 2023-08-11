class carta:

    CORAZON = " Corazón "
    DIAMANTE = " Diamante "
    TREBOL = " Trébol "
    ESPADA = " Espada "

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = carta("8", carta.DIAMANTE)
carta2 = carta("Q", carta.ESPADA)
 
print(" Carta 1: Valor = ", carta1.valor, ", Pinta = ", carta1.pinta)
print(" Carta 2: Valor = ", carta2.valor, ", Pinta = ", carta2.pinta)
