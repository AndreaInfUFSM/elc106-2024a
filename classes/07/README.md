<!--
author:   Andrea Charão

email:    andrea@inf.ufsm.br

version:  0.0.1

language: PT-BR

narrator: Brazilian Portuguese Female

comment:  Material de apoio para a disciplina
          ELC106 - Algoritmo e Programação,
          da Universidade Federal de Santa Maria

translation: English  translations/English.md

link:     custom.css
          https://fonts.googleapis.com/css?family=Quattrocento%20Sans
-->
<!--
liascript-devserver --input README.md --port 3001 --live
link:     https://cdn.jsdelivr.net/gh/liascript/custom-style/custom.min.css
          https://cdn.jsdelivr.net/gh/andreainfufsm/elc106-2023a/classes/05/custom.css
          https://fonts.googleapis.com/css?family=Abril%20Fatface

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/07/README.md)


# Aula 07

- Muitos exercícios: variáveis, condicionais, funções, listas, repetição/loops
- Dinâmica: missão possível




### Exercícios com variáveis

               
                 {{1}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
x = 10
y = x + 5
x = y - 3
print(x, y)
```


- [( )] 10 5
- [(x)] 12 15
- [( )] 7 15
- [( )] 15 12

************************************************



                 {{2}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
ano = 2020
idade = 4
nome = 'Lulu'
print(nome, 'tinha', idade, 'anos em', ano)
n = 5
print(nome, 'terá', idade+n, 'anos em', ano+n)
```

(a)

```
2020
4 
Lulu
5
```

(b)

```
nome idade ano
```


(c)

```
Lulu tinha 4 anos em 2020
Lulu terá 9 anos em 2025
```

- [( )] (a)
- [( )] (b)
- [(x)] (c)

************************************************



               
                 {{3}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
from math import sqrt

r = sqrt(9)
s = len("texto")
s = s + 1
print(r + s)
```

- [( )] 1.0
- [( )] 3.0
- [(x)] 9.0
- [( )] 10.0


************************************************


                 {{4}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
r = 10
s = 20
print(r + 2 + s)
r = s + 1
print(r)
```

************************************************


### Exercícios com estruturas condicionais


                 {{1}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
n = 10 % 2
if n == 0:
  print('abra')
else:
  print("cadabra") 
```


- [(x)] abra
- [( )] cadabra
- [( )] abracadabra


************************************************



                 {{2}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
n = 10 ** 2
if n > 150:
  n = n + 1
else:
  n = n * 2
print(n) 
```

- [( )] 102 
- [( )] 150
- [( )] 151
- [(x)] 200


************************************************


                 {{3}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)? Explique passo-a-passo.

```python
x = 2 ** 2
y = 11 // 5
if x < y:
  print('ax')
elif x > y:
  print('bx')
else:
  print('cx')
```



************************************************






### Exercícios com funções


                 {{1}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
def func(a, b):
  return a**2 + b
x = 2
y = x + 1
print(func(x, y))
```


- [( )] 4
- [( )] 2
- [(x)] 7
- [( )] 6

************************************************


                 {{2}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)? Explique passo-a-passo.

```python
def funcA(x):
  x = x + 1
  return x**2

def funcB(y):
  y = y - 1
  return y

a = 2
b = 3

print(funcA(a))
print(funcB(b))
```

************************************************






### Exercícios com listas


                 {{1}}
************************************************

Listas em Python são tipos de dados compostos, contendo um conjunto de elementos que podem ser acessados por um índice. 

Podemos nomear uma variável do tipo lista como fazemos com qualquer outra variável. Para definir valores, devemos usar colchetes para delimitar os elementos. Por exemplo: `letras = ['a', 'b', 'c']`.

Para acessar os elementos de uma lista, usamos o nome da variável seguido de colchetes. O primeiro elemento de uma lista sempre terá índice 0, o segundo terá índice 1, e assim por diante. Por exemplo: `letras[0]` acessa o elemento `a`,`letras[1]` acessa o elemento `b`, etc.

Sabendo disso, considerando a lista `colors = ["red", "green", "blue", "pink", "yellow"]`, qual das opções abaixo acessa o elemento `pink`?

- [( )] elemento = colors["pink"]
- [( )] elemento = lista[1]
- [(x)] elemento = colors[3]
- [( )] elemento = lista[]


************************************************



                 {{2}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
lista = [2,4,6,8]
i = len(lista) // 2
print(lista[i])
```

- [( )] 2 
- [( )] 4
- [(x)] 6
- [( )] 8


************************************************

                 {{3}}
************************************************

Considerando o código abaixo, marque as variáves que são do tipo lista.

```python
w = "lista"
x = 10
y = [9,10]
z = [sqrt(9)]
```

- [( )] w
- [( )] x
- [(x)] y
- [(x)] z



************************************************


### Exercícios com repetição


                 {{1}}
************************************************

Deseja-se sortear 100 números inteiros de 1 a 6 e guardá-los em uma lista. Qual dos códigos abaixo resolve este problema?

(a)
``` python
from random import randint
i = 1
lista = []
while i < 100:
  lista.append(randint(1,6))
  i += 1  
print(len(lista))
```

(b)
``` python
from random import randint
i = 0
lista = []
while i < 100:
  lista.append(randint(1,6))
  i += 1  
print(len(lista))
``` 
- [( )] (a)
- [(x)] (b)

************************************************

                 {{2}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
i = 1
n = 10
while i < 4:
  n = n * i
  i += 1  
print(n) 
```

 
- [(x)] 60
- [( )] 40
- [( )] 10



************************************************

                 {{3}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
i = 0
while True:
  i = i + 2
  if i > 8:
    break
print(i) 
```

- [( )] 16 
- [(x)] 10
- [( )] 8



************************************************


                 {{4}}
************************************************

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)? Explique passo-a-passo.

```python
text = ''
while True:
  text = text + 'a'
  if len(text) > 3:
    break
print(text) 
```




************************************************





### Exercícios de escrita de código

1. Defina uma função `def somatorio(numeros):` que receba uma lista de números como argumento e retorne o somatório desses números. Use `while` para expressar o padrão de cálculo repetitivo. Obs.: existem bibliotecas que já oferecem o cálculo de somatório em funções pré-definidas, mas você não deve usar estas funções.

2. Defina uma função `def media(numeros):` que receba uma lista de números como argumento e retorne a média aritmética desses números. Use `while` para expressar um padrão de cálculo repetitivo. Obs.: existem bibliotecas que já oferecem o cálculo de média em funções pré-definidas, mas você não deve usar estas funções.

3. Crie um programa que gere (pseudo-)aleatoriamente um conjunto de 50 números inteiros entre 1 e 20, guarde-os em uma lista e, ao final, mostre o somatório e/ou a média dos números. 




