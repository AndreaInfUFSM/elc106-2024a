# (Adaptado de: https://programming-23.mooc.fi/part-2)

# Usando `while`, escreva um programa que use a função `input` repetidamente para entrada (leitura) de um número inteiro. 
# Se o número for negativo, o programa deve mostrar a mensagem "Número inválido". 
# Se o número for maior do que zero, o programa deve mostrar a raiz quadrada do número. 
# Em qualquer desses casos, o programa deve continuar solicitando a digitação do próximo número. 
# Se o número for igual a zero, o programa deve mostrar uma mensagem e sair do laço.
# Dica: use a função `int(...)` para converter para inteiro a string lida pela função `input`

# Exemplo de execução:

# Digite um número: 9
# 3.0
# Digite um número: 4
# 2.0
# Digite um número: 6
# 2.449489742783178
# Digite um número: -2
# Número inválido
# Digite um número: 0
# Terminando...

from math import sqrt
while True:
  n = int(input('Digite um número: '))
  if n < 0:
    print('Número inválido')
  elif n > 0:
    print(sqrt(n))
  else:
    print('Terminando...')
    break