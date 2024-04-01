
# 1. Defina uma função chamada `media3`, que receba como parâmetros 3 números `x,y,z` e retorne a média aritmética desses números.

#   Exemplo de uso:
#   >>> media3(4,6,8)
#   6.0


def media3(x,y,z):
  return (x + y + z)/3
  
# 2. Defina uma função chamada `media4`, que receba como parâmetros 4 números `x,y,z,w`  e retorne a média aritmética desses números.

#    Exemplo de uso:
#    >>> media4(1,2,3,4)
#    2.5


def media4(x,y,z,w):
  return (x + y + z + w)/4

# 3. Defina uma função chamada `imc`, que calcule o Índice de Massa Corporal para um dado peso `p` (em quilogramas) e uma dada altura `h` (em metros). O IMC é calculado dividindo-se o peso pelo quadrado da altura.

#    Exemplo de uso:
#    >>> imc(80, 1.70)
#    27.68166089965398


def imc(p, h):
  return p/h**2

# 4. Defina uma função chamada `distanciapt`, que calcule a distância entre 2 pontos A e B em um plano. 
# Essa função deverá receber 4 parâmetros representando coordenadas `xa,ya` do ponto A e `xb,yb` do ponto B. 
# A distância deve ser calculada pela raiz quadrada de: (xb-xa) ao quadrado + (yb-ya) ao quadrado

#    Exemplo de uso:
#    >>> distanciapt(2,3,2,3)
#    0.0
#


def distanciapt(xa,ya,xb,yb):
  return ((xb-xa)**2 + (yb-ya)**2)**(0.5)

# Outra solução, usando a função sqrt:

from math import sqrt

def distanciapt_v2(xa,ya,xb,yb):
  return sqrt((xb-xa)**2 + (yb-ya)**2)



# 5. Defina uma função chamada `days2sec`, que converta dias em segundos. Essa função deve receber como parâmetro um número `d` representando uma quantidade de dias e retornar o número equivalente em segundos.

#    Exemplo de uso:
#    >>> days2sec(2)
#    172800

def days2sec(d):
  return d*24*60*60

# 6. Suponha que, em um restaurante próximo à Universidade, o preço do quilo no buffet seja de R$ 57,90. Defina uma função chamada `prato` que receba um peso `p` em gramas de uma porção servida no buffet e retorne o preço a pagar.

#    Exemplo de uso:
#    >>> prato(400)
#    23.16

def prato(peso):
  return peso * 57.90 / 1000

# 7. Suponha que você tenha passado em uma disputada seleção para um cargo na área de *data science* de uma empresa multinacional. Parabéns! Logo no primeiro ano na empresa, você faz uma viagem a trabalho no exterior. Quando chega no hotel depois de uma longa viagem, você nota que o quarto está frio. Você verifica o termostato do ar condicionado e percebe que está indicando 53.6 graus Fahrenheit. 

# Qual será a temperatura do quarto em Celsius? Para calcular isso, defina uma função chamada `f2c` que receba uma temperatura `t` em Fahrenheit e retorne o equivalente em Celsius. Para converter, subtraia 32 de `t` e multiplique o resultado por 5/9.

#    Exemplo de uso:
#    >>> f2c(53.6)
#    12.0

#    ```

def f2c(t):
  return (t-32) * 5/9


# 8. Agora defina outra função `c2f` para fazer a conversão inversa, e assim descobrir como ajustar o termostato para uma temperatura equivalente a agradáveis 22 graus Celsius. Essa função deverá multiplicar a temperatura `t` por 9/5 e adicionar 32.

def c2f(t):
  return t*9/5 + 32


# 9. Depois de definir todas estas funções, use cada uma delas no final do programa, junto com o comando `print`, aplicando-as a valores à sua escolha. Pelo menos um dos valores deverá estar armazenado em uma variável. Além disso, você deve acrescentar pelo menos um `print` com texto. 

#    Exemplo:
#    print('Temperatura em Fahrenheit:', c2f(30))

print('====> Função 1')
# Função 1: Uso básico, mostrando apenas resultado
print(media3(4,6,8))

# Função 1: Uso com variáveis e texto
a = 4
b = 6
c = 8
print('Média de a, b, c =', media3(a, b, c))

print('====> Função 2')
# Função 2:
print('Média de 1,2,3,4:', media4(1,2,3,4))

print('====> Função 3')
# Função 3: Uso básico, mostrando apenas resultado
print(imc(80,1.70))

# Função 3: Uso com variáveis e texto
peso = 60
altura = 1.60
print('IMC =', imc(peso, altura))

print('====> Função 4')
# Função 4: 
print(distanciapt(2,3,2,3))

# Função 4: Segunda versão (resultado será idêntico ao da versão anterior)
print(distanciapt_v2(2,3,2,3))

print('====> Função 5')
# Função 5: Com mensagem de texto
print("2 dias equivalem a", days2sec(2), "segundos")

# Função 5: Com variável
dias = 5
print(dias, "dias equivalem a", days2sec(dias), "segundos")

print('====> Função 6')
# Função 6: 
peso = 400
print("Meu almoço pesou", peso, "gramas")
print("Minha conta foi de", prato(peso), "reais")

print('====> Função 7')
# Função 7: 
print("Temperatura em Fahrenheit:", 53.6)
print("Equivalente em Celsius", f2c(53.6))

tempf = 53.6
print(tempf, 'Fahrenheit =', f2c(tempf), 'Celsius')

print('====> Função 8')
# Função 8: 
tempc = 20
print("Temperatura em Celsius:", tempc)
print("Equivalente em Fahrenheit", c2f(tempc))

