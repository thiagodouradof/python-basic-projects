# Adivinhe o Número

Esse código implementa uma versão em Python do clássico jogo "Jokenpo" (Pedra, Papel, Tesoura). O jogo é jogado entre um usuário e o computador, onde ambos escolhem uma das três opções: Pedra, Papel ou Tesoura. O resultado de cada rodada é determinado pelas regras tradicionais:

- Pedra vence Tesoura
- Tesoura vence Papel
- Papel vence Pedra
- O jogo continua em um loop até que o jogador decida não jogar mais. Ao final de cada rodada, o jogo exibe a pontuação atual e pergunta ao jogador se ele deseja continuar jogando. Se o jogador decidir parar, a pontuação final é mostrada e o jogo encerra.

## Como funciona:

Entrada:

Entrada do usuário para escolher entre Pedra, Papel ou Tesoura.
Entrada do usuário para decidir se deseja jogar novamente após cada rodada.

Saída:

A escolha do jogador e a escolha do computador.
O resultado da rodada (vitória, derrota ou empate).
A pontuação atual após cada rodada.
A pontuação final ao encerrar o jogo.

## Conceitos Aprendidos:

- Estruturas Condicionais: Uso de if-elif-else para determinar o vencedor de cada rodada com base nas escolhas do jogador e do computador.
- Laços de Repetição (Loops): Uso de while para repetir o jogo até que o jogador decida parar.
- Manipulação de Strings: Uso de funções como input(), lower(), upper() e re.match() para obter e manipular as escolhas do jogador.
- Uso da biblioteca os para limpar a tela do console entre rodadas.
- Listas: Armazenamento das opções disponíveis (Pe, Pa, T) em uma lista para facilitar a escolha aleatória do computador.
- Tratamento de Erros: Uso de try-except para lidar com entradas inválidas e garantir que o jogo continue funcionando de maneira - previsível.
- Interação com o Usuário: Solicitação de entradas e exibição de mensagens ao usuário para manter o jogo interativo e informativo.
