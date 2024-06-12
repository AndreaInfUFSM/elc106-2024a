# Escreva um programa que gere e mostre 5 números pseudoaleatórios representando anos no período entre 2010 e 2020 (inclusive).  
# No final, o programa deve mostrar quantos números gerados são maiores que 2015. 
# Resolva este exercício primeiro usando `while`, depois usando `for`.

# Exemplo de saída:

# ```
# 2020
# 2012
# 2015
# 2020
# 2016
# Maiores que 2015: 3
# ```


# Solução com while

from random import randint
i = 0
contador = 0
while i < 5:
  ano = randint(2010,2020)
  print(ano)
  if ano > 2015:
    contador = contador + 1
  i = i + 1  
print('Maiores que 2015:', contador)

# Solução com for

contador = 0
for i in range(5):
  ano = randint(2010,2020)
  print(ano)
  if ano > 2015:
    contador = contador + 1
print('Maiores que 2015:', contador)

