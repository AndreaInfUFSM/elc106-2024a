
# Fonte: https://programming-23.mooc.fi/part-2

# Deseja-se mostrar uma contagem regressiva como no exemplo abaixo:

# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!


# O código abaixo tenta fazer isso, mas tem um erro. Corrija-o para obter a saída desejada.

# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number > 0:
#     break
# print("Now!")

# O erro está na condição usada no if: deveria ser "number < 1" e não "> 0":

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number < 1:
    break
print("Now!")