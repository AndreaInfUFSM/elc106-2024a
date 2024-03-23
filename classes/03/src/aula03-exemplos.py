print('********** Exemplo 01 **********')
from random import randint

sorteado = randint(1, 6)
print('Número sorteado:', sorteado)
if sorteado == 6:
  print('Conseguimos o maior número!')
  print('Temos muita sorte!')
print('Fim do programa')

print('********** Exemplo 02 **********')
from random import randint

x = randint(1, 100)
print('Idade:', x)
if x >= 18:
  print('Maior de idade')
if x < 18:
  print('Menor de idade')
print('Fim do programa')

print('********** Exemplo 03 **********')
from random import randint

a = randint(1, 10)
b = randint(1, 10)
print('Valores:', a, b)
if a > b:
  print('Primeiro valor é maior')
if a <= b:
  print('Primeiro valor é menor ou igual')

print('********** Exemplo 04 **********')
from random import randint

def parouimpar(n):
  if n % 2 == 0:
    return "par"
  if n % 2 == 1:
    return "impar"

n = randint(1, 100)
print('O número', n, 'é', parouimpar(n))


print('********** Exemplo 05 **********')
n = 0
print(n)
n = 1
print(n)
n = n + 1
print(n)
