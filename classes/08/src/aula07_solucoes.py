from random import randint

def somatorio(lista):
  soma = 0
  indice = 0
  while (indice < len(lista)):
    soma = soma + lista[indice]
    indice = indice + 1
  return soma
  
def media(lista):
  soma = 0
  indice = 0
  while (indice < len(lista)):
    soma = soma + lista[indice]
    indice = indice + 1
  return soma / len(lista)
  
# def outramedia(lista):
#   return somatorio(lista) / len(lista)
  
lista0 = []
lista1 = [1,1,1,1,1]
lista2 = [2,4,6]
print(somatorio(lista0))
print(somatorio(lista1))
print(somatorio(lista2))

quant = 0
lista = []
while (quant < 10):
  lista.append(randint(1,6))
  quant = quant + 1
  
print(lista)
print(somatorio(lista))
print(media(lista))
# print(outramedia(lista))
