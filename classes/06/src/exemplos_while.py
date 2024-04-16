# ********************************* 
print('***** Primeiro while *****')
contador = 1
while contador < 10:
  print(contador)
  contador = contador + 1
print('Fim')

# *********************************
print('***** Gerando vários números *****')
from random import randint
seq = 0
while seq < 5:
  n = randint(1,20)
  print(n)
  seq = seq + 1
print('Fim da geração')

# *********************************
print('***** Contagem regressiva *****')

num = 10
while num > 0:
  print(num)
  num = num - 1
print('Boom!')

# *********************************
print('***** Usando break *****')

from random import randint
while True:
  n = randint(1,10)
  print(n)
  if n == 6:
    break

# *********************************
print('***** Tabela de multiplicação *****')

mult = 0
n = 3
while mult <= 10:
  print(n, 'x', mult, '=', n * mult)
  mult = mult + 1


# *********************************
print('***** Laço com bloco condicional *****')

from random import randint
contador = 1
while contador <= 10:
  n = randint(1, 6)
  print('Sorteamos o número', n)
  if n == 6:
    print('Oba, tiramos o maior número!')
  contador = contador + 1

# *********************************
print('***** Laço infinito *****')


# while True:
#   print('Continue repetindo')


# n = 10
# while n > 5 and n < 20:
#   print('Continue repetindo')
# print('Fim do programa')  

# *********************************
print('***** Laço não executado *****')

n = 10
while n < 0 or n > 100:
  print('Não vou ser executado')
print('Fim do programa')  

# *********************************
print('***** Laço com input *****')

while True:
  senha = input('Digite a senha: ')
  if senha == "abracadabra":
    break
  else:
    print('Senha incorreta. Tente novamente')

# *********************************
print('***** Somatório de valores *****')

from random import randint
i = 1
soma = 0
while i <= 10:
  n = randint(1, 6)
  print('n =', n)
  soma = soma + n
  i = i + 1
print('Somatório:', soma)


# *********************************
print('***** Contador com condição *****')
from random import randint

contador = 1
conta6 = 0
while contador < 10:
  n = randint(1, 6)
  print('Sorteamos', n)
  if n == 6:
    conta6 = conta6 + 1
  contador = contador + 1
print('Quantas vezes sorteamos o número 6?', conta6)



