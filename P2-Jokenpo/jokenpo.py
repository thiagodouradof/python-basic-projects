# -------------------------------------------------------------
# Jokenpo
# -------------------------------------------------------------

import random
import os
import re

def verificar_status_jogo(pontuacao_usuario, pontuacao_computador):
    respostas_validas = ['sim', 'não', 's']
    while True:
        try:
            resposta = input('Você deseja jogar novamente? (Sim ou Não): ')
            if resposta.lower() not in respostas_validas:
                raise ValueError('Apenas Sim ou Não')

            if resposta.lower() in ['sim', 's']:
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Obrigado por jogar!')
                print(f'Pontuação Final - Você: {pontuacao_usuario}, Computador: {pontuacao_computador}')
                exit()

        except ValueError as err:
            print(err)

def jogar_jokenpo():
    pontuacao_usuario = 0
    pontuacao_computador = 0
    jogar = True

    while jogar:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Pedra, Papel, Tesoura - Já!')

        escolha_usuario = input('Escolha sua arma: [Pe]edra, [Pa]apel ou [T]esoura: ')

        if not re.match("[PpTt]", escolha_usuario):
            print('Por favor, escolha uma letra válida:')
            print('[Pe]dra, [Pa]pel ou [T]esoura')
            continue

        print(f'Você escolheu: {escolha_usuario.upper()}')

        opcoes = ['Pe', 'T', 'Pa']
        escolha_oponente = random.choice(opcoes)

        print(f'Eu escolhi: {escolha_oponente}')

        if escolha_oponente == escolha_usuario.upper():
            print('Empate!')
        elif escolha_oponente == 'Pe' and escolha_usuario.upper() == 'T':
            print('Pedra vence tesoura, eu ganho!')
            pontuacao_computador += 1
        elif escolha_oponente == 'T' and escolha_usuario.upper() == 'Pa':
            print('Tesoura vence papel! Eu ganho!')
            pontuacao_computador += 1
        elif escolha_oponente == 'Pa' and escolha_usuario.upper() == 'Pe':
            print('Papel vence pedra, eu ganho!')
            pontuacao_computador += 1
        else:
            print('Você ganhou!\n')
            pontuacao_usuario += 1

        print(f'Pontuação - Você: {pontuacao_usuario}, Computador: {pontuacao_computador}')
        
        jogar = verificar_status_jogo(pontuacao_usuario, pontuacao_computador)

if __name__ == '__main__':
    jogar_jokenpo()