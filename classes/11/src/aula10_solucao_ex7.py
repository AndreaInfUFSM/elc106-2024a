# Usando `while` ou `for`, escreva uma função que receba um número N
# inteiro e positivo e que retorne o resultado S da seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

# Exemplo de uso:
# >>> serie(8)
# 2.7178571428571425


def serie(N):
  soma = 0
  for i in range(1, N + 1):
    print("1 /", i, '+')
    soma += 1 / i
  return soma

def serie_com_while(N):
  soma = 0
  i = 1
  while i <= N:
    print("1 /", i, '+')
    soma += 1 / i
    i += 1
  return soma

  
print(serie(8))
print(serie_com_while(8))