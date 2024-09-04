# -------------------------------------------------------------
# Lançador de Dados
# -------------------------------------------------------------

import random
import os

def numero_dados():
    while True:
        try:
            num_dados = input('Número de dados: ')
            respostas_validas = ['1', 'um', 'dois', '2','tres','3']
            if num_dados not in respostas_validas:
                raise ValueError('Apenas 1, 2 ou 3')
            else:
                return num_dados
        except ValueError as err:
            print(err)


def jogar_dados():
    valor_min = 1
    valor_max = 6
    jogar_novamente = 's'

    while jogar_novamente.lower() == 'sim' or jogar_novamente.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        quantidade = numero_dados()

        if quantidade == '3' or quantidade == 'tres':
            print('Rolando os dados...')
            dado_1 = random.randint(valor_min, valor_max)
            dado_2 = random.randint(valor_min, valor_max)
            dado_3 = random.randint(valor_min, valor_max)

            print('Os valores são:')
            print('Dado Um: ', dado_1)
            print('Dado Dois: ', dado_2)
            print('Dado Três: ', dado_3)
            print('Total: ', dado_1 + dado_2 + dado_3)

            jogar_novamente = input('Jogar Novamente? ')
        elif quantidade == '2' or quantidade == 'dois': 
            print('Rolando os dados...')
            dado_1 = random.randint(valor_min, valor_max)
            dado_2 = random.randint(valor_min, valor_max)

            print('Os valores são:')
            print('Dado Um: ', dado_1)
            print('Dado Dois: ', dado_2)
            print('Total: ', dado_1 + dado_2)

            jogar_novamente = input('Jogar Novamente? ')
        else:
            print('Rolando o dado...')
            dado_1 = random.randint(valor_min, valor_max)
            print(f'O valor é: {dado_1}')

            jogar_novamente = input('Jogar Novamente? ')

if __name__ == '__main__':
    jogar_dados()