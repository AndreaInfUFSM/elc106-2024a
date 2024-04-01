from random import randint


print('********** PARTE 1 **********')

"""
Escreva abaixo um programa que:
- Mostre a mensagem "Estou estudando programação em Python"
- Gere um número inteiro entre 1 e 2, armazenando-o em uma variável
- Se o número for igual a 1, mostre a mensagem "Vou fazer mais exercícios"
- Se o número for igual a 2, mostre a mensagem "Vou consultar o material de apoio"
"""

# COMPLETE-ME



print('********** PARTE 2 **********')

"""
Escreva abaixo um programa que:
- Gere 4 números entre 1 e 100, um por vez, armazenando-os em variáveis nomeadas a, b, c, d
- Calcule a média aritmética entre a, b, c usando a função que você definiu na aula anterior
  (copie e cole a função para o arquivo desta aula)
- Calcule a média aritmética entre b, c, d  
- Use a função `print` duas vezes para mostrar os números sorteados e as médias calculadas
  (uma vez para a b c e outra vez para b c d)

A saída do programa deve ser exatamente no formato exemplificado abaixo, só
com números diferentes a cada execução:
  Média entre 83 54 48 igual a 61.666666666666664
  Média entre 54 48 9 igual a 37.0
"""
# COMPLETE-ME



print('********** PARTE 3 **********')

"""
Escreva abaixo um programa que:
- Gere um número inteiro entre 1 e 30 representando um dia
- Armazene o número em uma variável
- Se o número for menor ou igual a 15, mostre a mensagem "Primeira quinzena". 
  Em caso contrário, mostre a mensagem "Segunda quinzena".
"""

# COMPLETE-ME

print('********** PARTE 4 **********')


"""
Escreva abaixo um programa que:
- Gere 5 números inteiros positivos em intervalos variados à sua escolha
- Armazene os números em variáveis com nomes à sua escolha
- Use uma variável contadora que é incrementada a cada vez que um dos números gerados for par
- Use a definição de função `mumeropar(n)` fornecida abaixo
- Use a funçãp `print` para mostrar a quantidade de números pares gerados

A saída deste programa deve ser exatamente neste formato a seguir, mas com 
números diferentes a cada execução:
  Quantidade de números pares: 1
"""

# Função fornecida (não deve ser alterada)
def numeropar(n):
  if n%2 == 0:
    return True
  else:
    return False

# COMPLETE-ME


print('********** PARTE 5 **********')

"""
Escreva abaixo um programa que:
- Complete a função chamada `temfebre` para retornar "sim' ou "não" após
  verificar se uma dada temperatura corporal representa febre (veja referência sobre isso mais abaixo)
- Gere 2 números fracionários representando temperaturas entre 35 e 40, arredondando-os
  com 1 casa decimal e armazenando-os em variáveis
- Use a função `temfebre` com as temperaturas geradas
- Use a função `print` para compor a saída do programa

A saída deste programa deve ser exatamente neste formato a seguir, adaptado
conforme os números gerados:
  Temperatura: 39.8 Tem febre? sim
  Temperatura: 36.9 Tem febre? não

Como saber se tenho febre?
https://drauziovarella.uol.com.br/doencas-e-sintomas/febre/
"""


# COMPLETE a função abaixo 
# (lembre de também remover o caracter #)
# def temfebre(t):

# COMPLETE o restante do programa abaixo


print('********** PARTE 6 **********')

"""
Escreva abaixo um programa que auxilia na distribuição de estudantes em grupos:

1. Complete a função chamada `grupos(n, tam)`, que recebe um número de estudantes `n` e
  um número `tam` representando uma quantidade desejada de estudantes por grupo
  - A função deve retornar o número de grupos formados dividindo-se `n` por `tam`
  - Caso a divisão não seja exata, um dos grupos poderá ter menos que `tam` integrantes
  - Por exemplo: n=36, tam=4, grupos=9; n=37, tam=4, grupos=10
  - Dica: O operador `//` será útil neste exercício

2. Complete o restante do programa:
- Gere um número inteiro entre 30 e 40, representando o número de alunos `n`
- Gere um número inteiro entre 3 e 5, representando `tam`
- Use a função `grupos` para obter o número de grupos formado
- Mostre os dados na tela conforme o modelo abaixo, adaptado conforme os números gerados:
  Número de estudantes: 36
  Quantidade de estudantes por grupo: 4
  Número de grupos calculado: 9
"""


# COMPLETE a função abaixo 
# (lembre de também remover o caracter #)
# def grupos(n, tam):



