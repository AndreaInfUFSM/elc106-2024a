# Um sistema de automação residencial possui sensores de temperatura
# que, periodicamente, produzem uma lista de valores representando
# um conjunto de temperaturas medidas.
# De vez em quando, alguns sensores falham e retornam medidas absurdas,
# incompatíveis com a localidade e a estação do ano.
# Sua tarefa é criar uma função que receba uma lista e 2 números
# representando limiares de temperatura, e verifique se todos os elementos
# da lista estão dentro dos limiares. A função deverá retornar True se todos
# os elementos estiverem dentro dos limiares, ou False em caso contrário.
# Resolva este exercício primeiro usando `while`, depois usando `for`.

# Dica: um laço while pode ser interrompido com return

# Exemplo de uso:
# temperaturas = [32,31,22,33,34]
# temperaturas_validas(temperaturas, 0, 40)
# True
# temperaturas = [32,31,22,-99,33,34]
# temperaturas_validas(temperaturas, 0, 40)
# False

def temperaturas_validas(lista, inferior, superior):
  i = 0
  while i < len(lista):
    if lista[i] < inferior or lista[i] > superior:
      return False
    i += 1
  return True

def temperaturas_validas_usando_for(lista, inferior, superior):
  for temp in lista:
    if temp < inferior or temp > superior:
      return False
  return True # chegou no final do laço e não encontrou nenhuma temperatura fora do limiar



temperaturas = [32,31,22,33,34]
print(temperaturas_validas(temperaturas, 0, 40)) # deve retornar True
temperaturas = [32,31,22,-99,33,34]
print(temperaturas_validas_usando_for(temperaturas, 0, 40)) # deve retornar False