# -------------------------------------------------------------
# Adivinhe o Número
# -------------------------------------------------------------

import random

def mostrar_pontuacao(lista_tentativas):
    if not lista_tentativas:
        print("Atualmente não há uma melhor pontuação," " é sua para conquistar!")

    else:
        print(f"A melhor pontuação atual é" f" {min(lista_tentativas)} tentativas")


def iniciar_jogo():
    tentativas = 0
    numero_aleatorio = random.randint(1, 10)
    lista_tentativas = []

    print("Olá, viajante! Bem-vindo ao jogo de adivinhação!")
    nome_jogador = input("Qual é o seu nome? ")
    quer_jogar = input(
        f"Olá, {nome_jogador}, você gostaria de jogar "
        f"o jogo de adivinhação? (Digite Sim/Não): "
    )

    if quer_jogar.lower() != "sim":
        print("Tudo bem, obrigado!")
        exit()
    else:
        mostrar_pontuacao(lista_tentativas)

    while quer_jogar.lower() == "sim":
        try:
            palpite = int(input("Escolha um número entre 1 e 10: "))
            if palpite < 1 or palpite > 10:
                raise ValueError(
                    "Por favor, escolha um número dentro do intervalo especificado"
                )

            tentativas += 1

            if palpite == numero_aleatorio:
                lista_tentativas.append(tentativas)
                print("Parabéns! Você acertou!")
                print(f"Você precisou de {tentativas} tentativas")
                quer_jogar = input("Gostaria de jogar novamente? (Digite Sim/Não): ")
                if quer_jogar.lower() != "sim":
                    print("Tudo bem, tenha um bom dia!")
                    break
                else:
                    tentativas = 0
                    numero_aleatorio = random.randint(1, 10)
                    mostrar_pontuacao(lista_tentativas)
                    continue
            else:
                if palpite > numero_aleatorio:
                    print("É menor")
                elif palpite < numero_aleatorio:
                    print("É maior")

        except ValueError as err:
            print("Oh não! Esse valor não é válido. Tente novamente...")
            print(err)


if __name__ == "__main__":
    iniciar_jogo()
