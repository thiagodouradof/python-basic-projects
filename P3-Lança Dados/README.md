# Lançador de Dados

Este código implementa um simulador de lançamento de dados em Python. O usuário pode escolher quantos dados (1, 2 ou 3) deseja lançar, e o programa irá gerar aleatoriamente os valores desses dados e exibi-los. O usuário pode optar por lançar os dados novamente após cada rodada. O jogo continua até que o usuário decida não jogar mais.

## Como funciona:

Entrada:

Entrada do usuário para escolher o número de dados a serem lançados (1, 2 ou 3).
Entrada do usuário para decidir se deseja lançar os dados novamente após cada rodada.

Saída:

Os valores gerados para cada dado lançado.
A soma total dos valores dos dados.
Mensagem perguntando se o usuário deseja jogar novamente.

## Conceitos Aprendidos:

- Estruturas Condicionais: Uso de if-elif-else para determinar a quantidade de dados a serem lançados e para lidar com a resposta do usuário sobre jogar novamente.
- Laços de Repetição (Loops): Uso de while para repetir o jogo até que o usuário decida parar.
- Funções: Separação do código em funções como numero_dados() e jogar_dados() para modularizar o código, facilitando a manutenção e a leitura.
- Manipulação de Strings: Uso de funções como input() e lower() para obter e manipular as entradas do usuário.
- Tratamento de Erros: Uso de try-except para capturar e lidar com entradas inválidas do usuário, garantindo que o jogo continue funcionando corretamente.
- Listas e Condicionais de Comparação: Armazenamento e comparação de opções válidas para a quantidade de dados, garantindo que o usuário insira valores permitidos.