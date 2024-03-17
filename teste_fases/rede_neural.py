
import math


class RedeNeural:

    """def __init__(self):

        #entradas
        self.input_cloro = (clorox, cloroy)

        self.input_sujeira = (sujeirax, sujeiray)"""

    def encontra_direcao(self, clorox, cloroy, sujeirax, sujeiray):

        #entradas
        self.input_cloro = (clorox, cloroy)

        self.input_sujeira = (sujeirax, sujeiray)

        #peso da entrada
        cloro_weight = 0.5
        sujeira_weight = 0.5

        def activation(sum_cloro, sum_sujeira):
            movX = sum_sujeira[0] - sum_cloro[0]
            movY = sum_sujeira[1] - sum_cloro[1]

            if movX > 0:
                movX = 1
            elif movX == 0:
                movX = 0
            else:
                movX = -1

            if movY > 0:
                movY = 1
            elif movY == 0:
                movY = 0
            else:
                movY = -1

            return (movX, movY)

        #"soma" -- deve somar essa multipicação para todas as entradas
        sum_cloro = ((self.input_cloro[0] * cloro_weight), (self.input_cloro[1] * cloro_weight))
        sum_sujeira = ((self.input_sujeira[0] * sujeira_weight), (self.input_sujeira[1] * sujeira_weight))


        #saida
        output = activation(sum_cloro, sum_sujeira)

        print("output: ", output)
        return output
