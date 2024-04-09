print('********** Questão 1 **********')

# Escreva uma função em Python nomeada `delta` para calcular
# o discriminante de uma função quadrática, 
# dados seus coeficientes a, b, c
# Calcule o `delta` conforme estas orientações:
# https://brasilescola.uol.com.br/matematica/relacao-parabola-com-delta-funcao-segundo-grau.htm

def delta(a, b, c):
  return b**2 - 4*a*c
  


print('********** Questão 2 **********')
# Escreva um programa que:
# - gere 3 valores de coeficientes a, b, c de una função quadrática
# - calcule o delta usando a função do exercício anterior
# - mostre os valores de a, b, c
# - mostre o valor do delta
# - informe se a função terá duas, uma ou nenhuma raiz real, 
#   dependendo do valor do delta 
#   (consulte o link do exercício anterior para saber as condições)
#   Exemplo de saída:
#     a = 6 b = 5 c = 1
#     delta = 1
#     duas raízes reais

from random import randint

a = randint(1,10)
b = randint(1,10)
c = randint(1,10)

# a = 6
# b = 5
# c = 1
d = delta(a,b,c)
print('a =', a, 'b =', b, 'c =', c)
print('delta:', d)
if d > 0:
  print("duas raízes reais")
elif d == 0:
  print("uma raiz real")
else:
  print("sem raízes reais")



print('********** Questão 3 **********')

# Exercício adaptado de: 
# https://programming-22.mooc.fi/part-1/5-conditional-statements

# Escreva um programa de recomendações baseadas em 
# condições meteorológicas!
# Para isso, comece gerando 2 números aleatórios:
# - um número representando uma temperatura de 0 a 40 graus Celsius
# - um número 0 ou 1, que representará ausência / ocorrência de chuva
# Com base nesses números, mostre mensagens na tela informando
# as condições meteorológicas e recomendações de vestuário / comportamento
# As recomendações devem mudar se a temperatura estiver acima de
# 30, 20, 10 ou 5, e também se houver chuva prevista.

# Você pode definir as mensagens de recomendação ao seu gosto, desde que
# variem conforme as condições.
# Abaixo estão alguns possíveis exemplos de saída deste programa:

# Temperatura: 22
# Chuva prevista? não
# Recomendação:
# Vista jeans e camiseta

# Temperatura: 33
# Chuva prevista? sim
# Recomendação: 
# Vista bermuda e camiseta
# Leve um guarda-chuva 

# Temperatura: 15
# Chuva prevista? sim
# Recomendação: 
# Vista calça, camiseta e casaco
# Use galocha e leve um guarda-chuva

# Temperatura: 4
# Chuva prevista? sim
# Recomendação: 
# Use pijama
# Evite sair da cama! :-)

temperatura = randint(0,40)
chuva = randint(0,1)

print('Temperatura:', temperatura)
if chuva == 1:
  print('Chuva prevista? sim')
else:
  print('Chuva prevista? não')

print('Recomendação:')

if temperatura > 30:
  print("Vista bermuda e camiseta")
  if chuva == 1:
    print("Com este calor, nem precisa levar guarda-chuva!") 
elif temperatura > 20:
  print("Vista jeans e camiseta")
  if chuva == 1:
    print("Leve um guarda-chuva!") 
elif temperatura > 10:
  print('Vista calça, camiseta e casaco')
  if chuva == 1:
    print("Use galocha e leve um guarda-chuva!")
elif temperatura > 5:
  print('Não esqueça de levar casaco!')
  if chuva == 1:
    print("Galocha e guarda-chuva são seus amigos!")
else:
  print('Use pijama')
  if chuva == 1:
    print("Evite sair da cama! :-)")

print('********** Questão 4 **********')

# O IBGE oferece um serviço de consulta de frequência de nomes:
# https://servicodados.ibge.gov.br/api/docs/nomes?versao=2
# As séries de dados estão organizadas por décadas, de 1930 a 2010
# Uma das consultas possíveis é o ranking de nomes por década:
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada=2010
# Para fazer esta consulta, precisamos fornecer um ano válido,
# pois do contrário o serviço não retornará dados
# Ao todo, há 9 valores válidos, de 1930 a 2010 (inclusive)
# Somente é válido o ano de início de uma década. 
# Por exemplo, 1940 é válido, mas 1941 não é

# Sabendo disso, defina uma função `valida_ano(ano)`, que retorne
# True se o ano for válido ou False se não for
# Exemplos de uso da função:
# >>> valida_ano(1930)
# True
# >>> valida_ano(2013)
# False


def valida_ano(ano):
  if ano < 1930 or ano > 2010:
    return False
  else:
    if ano%10 == 0:
      return True
    else:
      return False


# Teste sua função
ano = 1930
print('Ano:', ano)
if valida_ano(ano):
  print('Este ano é válido')
else:
  print('Este ano é inválido')




print('********** Questão 5 **********')


# Adaptado de: https://novatec.com.br/livros/introducao-python-3ed/
# Escreva uma função nomeada `aprova_emprestimo`, que retorne
# True ou False, aprovando ou não um empréstimo bancário para 
# compra de uma casa. 
# Essa função deve receber como argumentos: 
# o valor da casa a comprar, 
# o salário do solicitante e o
# prazo de pagamento do empréstimo, em anos. 
# Para aprovação, o valor da prestação mensal não pode ser superior 
# a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar
# dividido pelo número de meses a pagar.

# Exemplo de uso da função:
# >>> aprova_emprestimo(200000, 5500, 10)
# False
# >>> aprova_emprestimo(200000,5800,10)
# True

def aprova_emprestimo(valor, salario, anos):
  prestacao = valor/(anos*12)
  if prestacao > salario*0.3:
    return False
  else:
    return True



# Teste sua função

v = 200000
s = 5500
anos = 10
if aprova_emprestimo(v, s, anos):
  print('Empréstimo aprovado')
else:
  print('Empréstimo recusado')







print('********** Questão 6 **********')


# Adaptado de: https://novatec.com.br/livros/introducao-python-3ed/
# Escreva uma função que calcule o valor a pagar pelo fornecimento de energia elétrica, a partir da quantidade de KWh consumida e da categoria de uso: 'R' para residências, 'C' para comércios e 'I' para indústrias.
# Calcule o valor de acordo com as regras a seguir:

# Categoria Residencial (R) até 500: R$ 0,40 x KWh
# Categoria Residencial (R) acima de 500: R$ 0,65 x KWh
# Categoria Comercial (C) até 1000: R$ 0,55 x KWh
# Categoria Comercial (C) acima de 1000: R$ 0,60 x KWh
# Categoria Industrial (I) até 1000: R$ 0,55 x KWh
# Categoria Industrial (I) acima de 1000: R$ 0,60 x KWh

# Exemplo de uso da função:
# >>> conta_energia(800,'R')
# 520.0

def conta_energia(kwh, categoria):
  if categoria == 'R':
    if kwh <= 500:
      return 0.4 * kwh
    else:
      return 0.65 * kwh
  elif categoria == 'C':
    if kwh <= 1000:
      return 0.55 * kwh
    else:
      return 0.60 * kwh
  elif categoria == 'I':
    if kwh <= 1000:
      return 0.55 * kwh
    else:
      return 0.60 * kwh


# Teste sua função
consumo = 800
categoria = 'R'
print('Valor da conta:', conta_energia(consumo, categoria))



print('********** Questão 7 **********')

# O código abaixo usa a função `choice` para escolher
# (pseudo)aleatoriamente um dos nomes de uma lista
# Altere o código para:
# - Substituir os nomes ('Fulano', etc.), de forma 
#   que a lista tenha seu nome e de mais 3 colegas
# - Caso seu nome não seja o sorteado, mostrar a mensagem
#   'Hoje escapei, amanhã não sei'
from random import choice

nomes = ['Nome A', 'Nome B', 'Nome C', 'Nome D']
escolha = choice(nomes)
print('Quem vai apresentar um trabalho hoje?')
print(escolha)
if escolha != 'Nome A':
  print('Hoje escapei, amanhã não sei')





print('********** Questão 8 **********')

# Escreva um programa que sorteie 5 vezes um nome
# a partir de uma lista, usando a função choice
# vista no exercício anterior.
# A lista deve incluir seu nome e deve ter pelo
# menos mais 2 nomes.
# O programa deverá contar quantas vezes seu nome foi sorteado
# e mostrar o valor deste contador no final.


nomes = ['Nome A', 'Nome B', 'Nome C', 'Nome D']
contador = 0

# Este código é bastante repetitivo, mas expressa a lógica corretamente
# Mais adiante veremos uma forma de melhorá-lo

escolha = choice(nomes)
if escolha == 'Nome A':
  contador = contador + 1

escolha = choice(nomes)
if escolha == 'Nome A':
  contador = contador + 1

escolha = choice(nomes)
if escolha == 'Nome A':
  contador = contador + 1

escolha = choice(nomes)
if escolha == 'Nome A':
  contador = contador + 1

escolha = choice(nomes)
if escolha == 'Nome A':
  contador = contador + 1

print('Nome A foi sorteado', contador, 'vezes')

