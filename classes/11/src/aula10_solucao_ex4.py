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

# Uma versão da solução    
def dezena_por_extenso(n):
  # COMPLETE
  if   n == 2: return "vinte"
  elif n == 3: return "trinta"
  elif n == 4: return "quarenta"
  elif n == 5: return "cinquenta"
  elif n == 6: return "sessenta"
  elif n == 7: return "setenta"
  elif n == 8: return "oitenta"
  elif n == 9: return "noventa"
  else: return ""  

# Outra versão da solução
def dezena_por_extenso_v2(n):
  dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
  if n < 2 or n > 9:
    return ''
  else:
    return dezenas[n-2]
  
# Outra versão da solução, com uma sintaxe mais "avançada" (outra forma de usar if/else)
def dezena_por_extenso_v3(n):
  dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
  return '' if n < 2 or n > 9 else dezenas[n-2]

  
def unidade_por_extenso(n):
  # COMPLETE
  if   n == 1: return " e um"
  elif n == 2: return " e dois"
  elif n == 3: return " e três"
  elif n == 4: return " e quatro"
  elif n == 5: return " e cinco"
  elif n == 6: return " e seis"
  elif n == 7: return " e sete"
  elif n == 8: return " e oito"
  elif n == 9: return " e nove"
  else: return ""  
    
def por_extenso(n):
  if n < 20 or n > 99:
    return "Número inválido"
  else:
    dezena = n // 10
    unidade = n % 10
    print(n)
    return dezena_por_extenso_v3(dezena) + unidade_por_extenso(unidade)

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