#copia do video rede de um neuronio
import math

#entrada
input = 1

#saida desejada
output_desire = 0

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

    #erro = saidadesejada - saida
    error = output_desire - output

    print("erro:", error, " peso:", input_weight, " iteracoes:", iteration)

    #ajuste relativo ao erro
    if error != 0:
        input_weight = input_weight + (learning_rate * input * error)

print("aprendeu!")



