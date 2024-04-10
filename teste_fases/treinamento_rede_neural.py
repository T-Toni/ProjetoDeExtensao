'''#copia do video rede de um neuronio
import math

#entrada
input = 0

#saida desejada
output_desire = 1

#peso da entrada
input_weight = 0.5

#taxa de aprendizado
learning_rate = 0.1

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

#erro. Inicialmente recebe infinito, pois qualquer outro erro vai ser menor que infinito
error = math.inf

#iterações
iteration = 0
#"soma" -- deve somar essa multipicação para todas as entradas
while error != 0:
    iteration += 1
    sum = input * input_weight


    #saida
    output = activation(sum)

    print("entrada:", input, " saida:", output, " saida desejada:", output_desire)

    #erro = saida_desejada - saida
    error = output_desire - output

    print("erro:", error, " peso:", input_weight, " iteracoes:", iteration)

    #ajuste relativo ao erro
    if error != 0:
        input_weight = input_weight + (learning_rate * input * error)

print("aprendeu!")'''

""""""

#copia do video rede de um neuronio
import math

#entrada
input_cloro = (12, -1)

input_sujeira = (10, 8)

#saida desejada
output_desire = (0, -1)

#peso da entrada
cloro_weight = 0.5
sujeira_weight = 0.5

#taxa de aprendizado
learning_rate = 0.1

def activation(sum_cloro, sum_sujeira):
    movX = sum_sujeira[0] * sujeira_weight - sum_cloro[0] * cloro_weight
    movY = sum_sujeira[1] * sujeira_weight - sum_cloro[1] * cloro_weight

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

#erro. Inicialmente recebe infinito, pois qualquer outro erro vai ser menor que infinito
error_cloro = math.inf
error_sujeira = math.inf

#iterações
iteration = 0

while error_cloro != 0 or error_sujeira != 0:
    iteration += 1
    #"soma" -- deve somar essa multipicação para todas as entradas
    sum_cloro = ((input_cloro[0] * cloro_weight), (input_cloro[1] * cloro_weight))
    sum_sujeira = ((input_sujeira[0] * sujeira_weight), (input_sujeira[1] * sujeira_weight))


    #saida
    output = activation(sum_cloro, sum_sujeira)


    #erro = saidade_sejada - saida
    error_cloro = output_desire[0] - output[0]
    error_sujeira = output_desire[1] - output[1]


    #ajuste relativo ao erro
    if error_cloro != 0:
        cloro_weight += learning_rate * error_cloro
    if error_sujeira != 0:
        sujeira_weight += learning_rate * error_sujeira

    print("iteração: ", iteration)
    print("output: ", output)

print("aprendeu!")


