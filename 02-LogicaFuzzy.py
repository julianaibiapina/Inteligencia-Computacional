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

# Funções de pertinência dos conjuntos nebulosos

# PRESSÃO NO FREIO
# Função que retorna três valores de pertinência
# para os conjuntos 'alta', 'média' e 'baixa'
def pressaoFreio(pres_pedal):

    pert_alta = 0
    pert_media = 0
    pert_baixa = 0

    # alta
    if pres_pedal < 50:
        pert_alta = 0
    elif pres_pedal == 50 or pres_pedal > 50:
        pert_alta =  (pres_pedal / 50) - 1


    # média
    if pres_pedal < 30:
        pert_media = 0
    elif pres_pedal == 30 or pres_pedal > 30 and pres_pedal < 50:
        pert_media =  (pres_pedal / 20) - 1.5
    elif pres_pedal == 50 or pres_pedal > 50 and pres_pedal < 70:
        pert_media =  (70 - pres_pedal) / 20
    elif pres_pedal == 70 or pres_pedal > 70:
        pert_media = 0

    # baixa
    if pres_pedal < 50:
        pert_baixa = (50 - pres_pedal) / 50
    elif pres_pedal == 50 or pres_pedal > 50:
        pert_baixa = 0

    return pert_alta, pert_media, pert_baixa

# VELOCIDADE DA RODA E DO CARRO
# Função que retorna três valores de pertinência
# para os conjuntos 'devagar', 'médio' e 'rápido'

def velocidade(velo):

    pert_devagar = 0
    pert_medio = 0
    pert_rapido = 0

    # devagar
    if velo < 60:
        pert_devagar = (60 - velo) / 60
    elif velo == 60 or velo > 60:
        pert_devagar = 0

    # médio
    if velo < 20:
        pert_medio = 0
    elif velo == 20 or velo > 20 and velo < 50:
        pert_medio = (velo - 20) / 30
    elif velo == 50 or velo > 50 and velo < 80:
        pert_medio = (80 - velo) / 30
    elif velo == 80 or velo > 80:
        pert_medio = 0

    # rápido
    if velo == 40 or velo < 40:
        pert_rapido = 0
    elif velo > 40:
        pert_rapido = (velo - 40) / 60

    return pert_devagar, pert_medio, pert_rapido



# Recebe os valores de pressão no pedal de freio, a velociade do carro
# e a velociade da roda. Retorna o valor que deve ser aplicado no freio
def  inf_de_Mamdani(pedal, roda, carro):

    pedal_alta, pedal_media, pedal_baixa = pressaoFreio(pedal)
    roda_devagar, roda_medio, roda_rapido = velocidade(roda)
    carro_devagar, carro_medio, carro_rapido = velocidade(carro)

    # Regra 1: aperte o freio
    regra_1 = pedal_media

    # Regra 2: aperte o freio
    regra_2 = min(pedal_alta, carro_rapido, roda_rapido)

    # Regra 3: libera o freio
    regra_3 = min(pedal_alta, carro_rapido, roda_devagar)

    # Regra 4: libera o freio
    regra_4 = pedal_baixa

    aperta_freio = regra_1 + regra_2
    libera_freio = regra_3 + regra_4

    # amostragem para cálculo da união das duas funções 'aperta_freio' e 'libera_freio'
    # é medida com a variável cont que é incrementa em uma unidade a cada iteração até chegar ao valor 100
    cont = 0
    # guarda o valor da união das duas funções
    list_uniao_funcoes = list()
    # guarda os valores individuais das funções 'aperta_freio' e 'libera_freio', respectivamente, em cada iteração
    f1 = 0
    f2 = 0
    while cont < 101:
        # equação da função aperta freio
        valor_func = cont/100

        if valor_func < aperta_freio or valor_func == aperta_freio:
            f1 = valor_func
        else:
            f1 = aperta_freio


        # equação da função libera freio
        valor_func2 = (100 - cont)/100

        if valor_func2 < libera_freio or valor_func2 == libera_freio:
            f2 = valor_func2
        else:
            f2 = libera_freio

        # União da 'área' das duas funções
        list_uniao_funcoes.append(max(f1,f2))
        #print('f1 = %8.3f  \nf2 = %8.3f \nlist_uniao_funcoes[%d] = %8.3f' % (f1, f2, cont, list_uniao_funcoes[cont]))

        cont += 1

    #controle do laço
    cont = 0

    sum1 = 0
    sum2 = 0

    # variável de saída do algoritmo
    pressao_no_freio = 0

    # Cálculo do centro de gravidade
    while cont < 101:
        sum1 += list_uniao_funcoes[cont] * cont
        sum2 += list_uniao_funcoes[cont]
        cont += 1

    pressao_no_freio = sum1 / sum2
    return pressao_no_freio


pressao_freio = inf_de_Mamdani(pressao_pedal, velocidade_roda, velocidade_carro)
print('Pressão no pedal: %d \nVelocidade da roda: %d \nVelocidade do carro: %d \nA pressão a ser aplicada (aproximadamente) = %8.3f' % (pressao_pedal, velocidade_roda, velocidade_carro, pressao_freio))
