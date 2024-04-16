# *********************************
print('***** Tamanho da lista *****')

frutas = ['goiaba', 'laranja', 'ameixa']
print(len(frutas))
vazio = []
print(len(vazio))

# *********************************
print('***** Acesso a um item *****')

frutas = ['goiaba', 'laranja', 'ameixa']
# primeira fruta
print(frutas[0])
# terceira fruta
print(frutas[2])
# ultimo elemento (forma genérica)
ultima = len(frutas) - 1
print(frutas[ultima])

# *********************************
print('***** Percorrer com while *****')

frutas = ['abacaxi','goiaba', 'laranja', 'ameixa']
indice = 0
while (indice < len(frutas)):
  print('Gosto de', frutas[indice])
  indice += 1

# *********************************
print('***** Adicionar elemento *****')

frutas = ['abacaxi','goiaba', 'laranja']
print(len(frutas))
frutas.append('banana')
print(len(frutas))
frutas.insert(0, 'ameixa')
print(len(frutas))

# *********************************
print('***** Somar elementos com while *****')
numeros = [10,20,30,40]
i = 0
soma = 0
while (i < len(numeros)):
  soma = soma + numeros[i]
  i = i + 1
print(soma) 

# *********************************
print('***** Lista de notas *****')

notas = [10, 8.5, 9.5, 7]

print(len(notas))
print(sum(notas))
print(sum(notas)/len(notas))

