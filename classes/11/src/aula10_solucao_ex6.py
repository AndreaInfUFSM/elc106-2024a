
# Escreva uma função chamada `countchars`,
# que receba uma lista de strings e
# retorne a quantidade total de caracteres na lista
# Você deve usar repetição com for neste exercício

# Exemplo de uso:
# >>> countchars(['Era uma vez', 'Há muitos anos atrás'])
# 31


def countchars(list):
  total = 0
  for s in list:
    total = total + len(s)
  return total


print(countchars(['Era uma vez', 'Há muitos anos atrás']))
