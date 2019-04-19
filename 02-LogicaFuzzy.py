from random import randint

# Valores de entrada
# - pressão no pedal; varia no intervalo [0,100]
# - velocidade da roda; varia no intervalo [0,100]
# - velocidade do carro; varia no intervalo [0,100]

# randint: Return a random integer N such that a <= N <= b.

# Variáveis de entrada
pressao_pedal = randint(0,100)
velocidade_roda = randint(0,100)
velocidade_carro = randint(0,100)

# Variável de saída
pressao_freio = 0

# Funções de pertinência dos conjuntos nebulosos

# PRESSÃO NO FREIO
# Função que retorna três valores de pertinência
# para os conjuntos 'alta', 'média' e 'baixa'//
def pressaoFreio(pres_pedal):

    pert_alta = 0
    pert_media = 0
    pert_baixa = 0

    # alta
    if pres_pedal < 50:
        pert_alta = 0
        print('Alta: {%d, 0}' % (pres_pedal))
    elif pres_pedal == 50 or pres_pedal > 50:
        pert_alta =  (pres_pedal / 50) - 1
        print('Alta: {%d, %f}' % (pres_pedal, pert_alta))

    # baixa
    if pres_pedal < 30:
        pert_media = 0
        print('Média: {%d, 0}' % (pres_pedal))
    elif




def  inf_de_Mamdani(pedal, roda, carro):

    return pressao_freio
