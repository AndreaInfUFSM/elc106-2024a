# Deseja-se completar um programa que gera números pseudoaleatórios
# entre 20 e 99 e os mostre escritos por extenso.
# Para isso, você deve completar as funções
# - dezena_por_extenso: recebe um número de 2 a 9 e retorna "vinte" a "noventa"
# - unidade_por_extenso: recebe um número de 0 e 9 e retorna a unidade por extenso
# O restante do programa deve ficar inalterado
# Ao final do programa, há 2 exemplos com lógica semelhante que podem servir
# de referência

# Exemplo de saída do programa
# sessenta e quatro
# oitenta e três
# vinte e um
# noventa
# vinte e oito
# sessenta e nove
# setenta e seis
# setenta e oito
# setenta e quatro
# trinta e oito
    
def dezena_por_extenso(n):
  # COMPLETE

def unidade_por_extenso(n):
  # COMPLETE
    
def por_extenso(n):
  if n < 20 or n > 99:
    return "Número inválido"
  else:
    dezena = n // 10
    unidade = n % 10
    return dezena_por_extenso(dezena) + unidade_por_extenso(unidade)

from random import randint
i = 0
while i < 10:
  n = randint(20,99)
  print(por_extenso(n))
  i += 1

# Exemplos de funções com lógica semelhante.
# A primeira versão usa só condicionais
# A segunda versão usa uma lista
def dia_da_semana_v1(n):
  if   n == 1: return 'Dom'
  elif n == 2: return 'Seg'
  elif n == 3: return 'Ter'
  elif n == 4: return 'Qua'
  elif n == 5: return 'Qui'
  elif n == 6: return 'Sex'
  elif n == 7: return 'Sab'
  else: return ''

def dia_da_semana_v2(n):
  dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
  if n < 1 or n > 7:
    return ''
  else:
    return dias[n-1]
