# Adivinhe o Número

Esse código é um simples jogo interativo onde o jogador deve adivinhar um número aleatório gerado pelo computador.

- O número escolhido pelo computador está entre 1 e 10, e o jogador faz tentativas de adivinhar esse número.
- A cada tentativa, o jogo fornece uma dica, dizendo se o palpite do jogador é maior ou menor que o número correto.
- O objetivo é adivinhar o número com o menor número de tentativas possível.
- O jogo também mantém um registro das tentativas e informa ao jogador o menor número de tentativas que alguém já conseguiu.

## Como funciona:

Entrada:

O jogador entra com seu nome e decide se deseja jogar ou não. Durante o jogo, o jogador entra com palpites para adivinhar o número.

Saída:

O jogo imprime mensagens de boas-vindas, solicita o nome do jogador, fornece dicas se o palpite está alto ou baixo, e imprime o número de tentativas feitas após adivinhar corretamente. Se o jogador jogar novamente, o jogo mostra o menor número de tentativas feitas até o momento.

## Conceitos Aprendidos:

- Criação de funções para organizar o código
- Estruturas de Controle (Uso de if, else, e while para controlar o fluxo do jogo.)
- Manipulação de Strings (Concatenar strings para exibir mensagens personalizadas)
- Manipulação de Listas (Armazenar e acessar dados em listas)
- Tratamento de Exceções (Uso de try e except para capturar erros e garantir que o jogo continue funcionando mesmo se o jogador entrar com um valor inválido.)
- Entrada e Saída de Dados (Uso de input() e print())
- Gerador de Números Aleatórios (Uso de random.randint() para gerar um número aleatório entre 1 e 10)