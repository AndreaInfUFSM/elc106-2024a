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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/09/README.md)


# Exercícios de Revisão

- [Exercícios com variáveis](#1-exercícios-com-variáveis)
- [Exercícios com estruturas condicionais](#2-exercícios-com-estruturas-condicionais)
- [Exercícios com funções](#3-exercícios-com-funções)
- [Exercícios com repetição](#4-exercícios-com-repetição-while)
- [Exercícios com listas](#5-exercícios-com-listas)
- [Homework](#6-homework)

## 1 Exercícios com variáveis

Variáveis foram vistas inicialmente na [aula 03](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/03/README.md#15) e continuaram sendo usadas em todas aulas seguintes

Avance para resolver exercícios com foco em variáveis.

### Exercício 1.1


Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
contador = 0
contador = contador + 3
contador = contador + 3
print(contador)
```


- [( )] 0
- [( )] 3
- [(x)] 6
- [( )] 9


### Exercício 1.2




Quando o código abaixo for executado, o que exatamente será mostrado na tela?

```python
saldo = 1000
print('Saldo:', saldo)
debito = 200
saldo = saldo - debito
print('Saldo:', saldo)
```

(a)

```
Saldo inicial
Saldo final
```

(b)

```
1000
200
```

(c)

```
Saldo: 1000
Saldo: 800
```

- [( )] (a)
- [( )] (b)
- [(x)] (c)


### Exercício 1.3

                 

Quando o código abaixo for executado, qual será sua saída?

``` python
from math import sqrt

a = 2
b = 4
c = 2
d = b**2 - 4*a*c
s = 10.5 + sqrt(d)
print(s)
```

- [( )] 12.4
- [(x)] 10.5
- [( )] 18.4
- [( )] 11.5

               

### Exercício 1.4




Qual será a saída do código abaixo?

``` python
r = len("abracadabra")
s = len(["abra","cadabra"])
print(r + s)
```


- [( )] 10
- [( )] 11
- [( )] 12
- [(x)] 13





### Exercício 1.5



Execute o programa abaixo. Note que o programa vai solicitar que você digite uma resposta para a pergunta. 



<iframe src="https://trinket.io/embed/python3/2a55179d46" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Modifique o início do programa para solicitar ao usuário que digite um nome, armazenando-o na variável `nome`. O restante do programa ficará como está.

Este exercício não tem correção automática. Você deve executar seu código com o botão ⯈ para verificar se está correto.

























## 2 Exercícios com estruturas condicionais


Estruturas condicionais (if/then/else) foram vistas inicialmente na [aula 03](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/03/README.md#15) e continuaram sendo usadas em aulas seguintes

Avance para resolver exercícios com foco em estruturas condicionais.


### Exercício 2.1

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
n = 4
r = n % 2  # calcula resto da divisão por 2
if r == 0:
  print('caso 1')
else:
  print("caso 2") 
```

- [(x)] caso 1
- [( )] caso 2



### Exercício 2.2




Quando o código abaixo for executado, qual será sua saída?

```python
chuva = True
temp = 15

if not chuva or temp > 20:
  print('caso 1')
elif temp < 10:
  print('caso 2')
else:
  print('caso 3')
```

- [( )] caso 1
- [( )] caso 2
- [(x)] caso 3





### Exercício 2.3

Quando o código abaixo for executado, e depois que o usuário digitar o número 42, o que será mostrado na tela?

```python
dia = input('Que dia do mês é hoje?')
dia = int(dia)
if dia <= 15:
  q = 1
else:
  q = 2
print('Estamos na ' +  str(q) + 'a quinzena')
```


- [( )] Nada
- [( )] Estamos na 1a quinzena
- [(x)] Estamos na 2a quinzena
- [( )] Erro


### Exercício 2.4


Modifique o código para que seja mostrada a mensagem 'Dia inválido' caso o dia digitado seja menor que 1 ou maior que 31. Nos outros casos, indique a quinzena, aproveitando os prints já presentes no programa. Use if/elif/else.

<iframe src="https://trinket.io/embed/python3/facfe92f06" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



Este exercício não tem correção automática. Você deve executar seu código com o botão ⯈ para verificar se está correto.






































## 3 Exercícios com funções



Começamos a lidar com funções desde a [aula 02](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/02/README.md)

Nem todo programa precisa definir funções, mas mesmo programas curtos costumam chamar/usar funções (por exemplo, `print`)

Avance para resolver exercícios com foco em funções.


### Exercício 3.1

Quando o código abaixo for executado, qual será sua saída?

```python
def func(x, y):
  return x + y*2

resultado = func(4, 5)
print(resultado)
```


- [(x)] 14
- [( )] 20
- [( )] 29


### Exercício 3.2

Quando o código abaixo for executado, qual será sua saída?

```python
def func(x, y):
  a = x + 1
  b = y + 2
  return a + b

dado = 10
print(func(dado, dado + 1))
```


- [( )] 6
- [( )] 12
- [(x)] 24
- [( )] 36


### Exercício 3.3

Quando o código abaixo for executado, qual será sua saída?

```python
def delta(a, b, c):
  return b**2 - 4*a*c
x = 2
y = x + 3
z = 3
print(1 + delta(x, y, z))
```


- [( )] 1
- [(x)] 2
- [( )] 3
- [( )] 4


### Exercício 3.4

No código abaixo, complete a função para que retorne verdadeiro se algum dos parâmetros for igual a 10 ou se a soma deles for 10.



<iframe src="https://trinket.io/embed/python3/d671de24f2" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


### Exercício 3.5

No código mais abaixo, os parâmetros da função is_square representam um retângulo, sendo (x1,y1) o ponto no canto superior esquerdo e (x2,y2) o ponto no canto inferior direito, conforme o diagrama a seguir: 

<!--
style="
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 315px;
  stroke: green;" -->
``` ascii
(x1,y1) +------+ 
        |      |
        |      |
        |      |
        +------+ (x2,y2)
```


Complete a função para que retorne verdadeiro caso as coordenadas passadas representem um quadrado (ou seja, ambos os lados tenham o mesmo tamanho).




<iframe src="https://trinket.io/embed/python3/c12bdf5d29" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>














## 4 Exercícios com repetição (`while`)

- Repetições foram introduzidas na [aula 06](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/06/README.md#15) e continuamos na [aula07](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/07/README.md#1).

- Comando `while`: executa um bloco de comandos **repetidamente**, **enquanto** uma condição resultar `True`

- Exemplo:

  <iframe src="https://trinket.io/embed/python3/a6fbc19887" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


- **Super importante** saber:

  - Bloco de comandos a repetir deve ser **recuado** à direita (indent) 
  - Se condição resultar `True`, bloco de comandos é executado
  - Ao final do bloco de comandos, execução "salta" para verificar condição novamente
  - Quando condição resultar `False`, execução "salta" para depois do bloco de comandos
  





### Exercício 4.1

Quando o código abaixo for executado, qual será sua saída (ou seja, o que exatamente será mostrado na tela)?

```python
i = 1
n = 10
while i < 4:
  n = n * 2
  i = i + 1  
print(n) 
```

- [( )] 10
- [( )] 20
- [(x)] 80
- [( )] 104
- [( )] 400

Ficou em dúvida? No papel, anote os valores de `i` e `n` a cada passo.

### Exercício 4.2

O que faz o código abaixo?


``` python
from random import randint
i = 0
soma = 0
while i < 100:
  soma = soma + randint(1,6)
  i += 1  
print(soma/100)
```


- [( )] Mostra o somatório de 100 valores sorteados
- [( )] Mostra 100 valores sorteados, linha por linha
- [(x)] Mostra a média aritmética de 100 valores sorteados


### Exercício 4.3

Considerando o código abaixo, qual das afirmações a seguir está correta?


``` python
while True:
  senha = input('Digite a senha: ')
  if senha == "1234":
    break
  else:
    print('Acesso negado. Digite a senha novamente')
print('Acesso permitido')
```

O código:

- [( )] repete o bloco de comandos 1234 vezes
- [( )] está errado, pois executa um loop infinito, que nunca poderá terminar
- [(x)] solicita digitação de string até que uma dada sequência seja digitada
- [( )] mostra 1234 vezes a mensagem 'Acesso negado. Digite a senha novamente'


### Exercício 4.4

Qual dos códigos abaixo sempre executará a mesma quantidade de repetições do bloco de comandos?


(a)

``` python
from random import randint
i = 0
lista = []
while i < 100:
  lista.append(randint(1,6))
  i += 1  
print(lista)
```

(b)

``` python
from random import randint
i = 0
while i < 100:
  n = randint(1,6)
  i += 1
  if (n == 6):
    break
print(i)
``` 


- [(x)] (a)
- [( )] (b)


### Exercício 4.5

Uma entrevista gerou uma lista de valores 1, 2 ou 3, representando respostas de diferentes pessoas para uma determinada questão. 
O código abaixo deve mostrar o número de ocorrências da alternativa 2 na lista. Desembaralhe o código para que funcione como desejado.

IMPORTANTE: 

- para a correção automática funcionar, comece o código com a seguinte sequência de inicialização de variáveis

  ``` python
  respostas = [1, 3, 2, 3, 1, 2, 1, 2, 1]
  i = 0
  ocorrencias = 0
  ```
- para verificar sua solução, clique no botão "Get feedback"  


<iframe src="https://parsons.problemsolving.io/puzzle/3fe903d9b9194ac9b6c701c5db0a8695" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>































































## 5 Exercícios com listas


- Listas em Python são tipos de dados compostos, contendo um conjunto de elementos que podem ser acessados por um índice. 

- Para definir uma lista de valores, usamos colchetes e separamos os elementos com vírgulas. Por exemplo: 

  ``` python
  vogais = ['a', 'e', 'i', 'o', 'u']
  ```


- Para acessar os elementos de uma lista, usamos o nome da variável seguido de um índice entre colchetes. O primeiro elemento de uma lista terá terá índice 0, o segundo terá índice 1, e assim por diante. 

- Por exemplo, na lista `vogais`:

  - `vogais[0]` acessa o elemento `'a'`,
  - `vogais[4]` acessa o elemento `'u'`, etc.





### Exercício 5.1



Considere a lista:

``` python
linguagens = ["Java", "Python", "R", "JavaScript"]
```

Qual das opções abaixo acessa o elemento `Python`?

- [( )] linguagens["Python"]
- [(x)] linguagens[1]
- [( )] linguagens[2]


### Exercício 5.2

Qual dos códigos abaixo mostrará uma mensagem para cada um dos elementos da lista de nomes, um por linha?

(a)

```python
nomes = ['Beltrano', 'Fulano', 'Sicrano']
i = 0
while i < len(nomes):
  print('Bom dia,', nomes[i])
  i = i + 1
```


(b)

```python
nomes = ['Beltrano', 'Fulano', 'Sicrano']
i = 1
while i < len(nomes):
  print('Bom dia,', nomes[i])
  i = i + 1
```


- [(x)] (a) 
- [( )] (b)


### Exercício 5.3

Qual será a saída deste código?



```python
cores = ['azul', 'verde', 'vermelho']

def misterio(lista):
  i = 0
  conta = 0
  while i < len(lista):
    if len(lista[i]) > 5:
      conta = conta + 1
    i = i + 1
  return conta
  
print(misterio(cores))

```

- [( )] 3
- [( )] 2
- [(x)] 1


### Exercício 5.4

Complete a função `contem2` no código abaixo, de forma que retorne `True` se existir o elemento `2` na lista, ou `False` em caso contrário.



<iframe src="https://trinket.io/embed/python3/2bf791d52c" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>






## 6 Homework


Nesta parte, temos exercícios extraclasse com foco em escrita de código.

**IMPORTANTE** 

- Resolva cada exercício incrementalmente, usando como referência outros códigos de exemplo que você consegue ler e entender.
- Resista à tentação de usar geradores de código e soluções prontas - você está exercitando a **sua inteligência** (que tende a estagnar se você usá-la pouco 😎)


### Exercício 6.1 

Escreva um programa que inicie sorteando um número e, depois, use a função `input` repetidamente, solicitando que o usuário digite um número para tentar adivinhar o número sorteado. Quando o usuário acertar o número, mostre uma mensagem e interrompa a repetição.

Dicas:

- Revise exemplos de repetições com `while`, com atenção às condições usadas para continuar a repetição
- Pense no bloco de instruções que deve ser repetido
- Revise a endentação do seu código, lembrando que cada bloco recuado está "sob influência" de um comando mais acima (`while`, `if`, etc.)


### Exercício 6.2

Escreva uma função `def geralista(n):` que retorne uma lista contendo `n` números gerados aleatoriamente. Depois de definir a função, utilize-a para gerar e mostrar uma lista com 5 números e outra lista com 10 números. 

Dicas:

- Você vai precisar de diferentes variáveis
- Inicie com uma lista vazia (`[]`)
- Revise as funções que manipulam listas, em especial a função `append`

### Exercício 6.3

Escreva uma função `def desviopadrao(lista):` que receba uma lista de números como parâmetro e retorne o desvio padrão do conjunto de números. Você não deve usar funções prontas que fazem os cálculos - seu objetivo é pensar no algoritmo e expressá-lo em Python. Teste sua função, escrevendo um código simples que calcula o desvio padrão de uma lista à sua escolha (você pode enumerar os elementos manualmente ou usar a função `geralista`).

Dicas:

- Antes de resolver este exercício, você deve ter resolvido os exercícios de cálculo de somatório e cálculo de média
- Pesquise a fórmula do desvio padrão antes de começar a escrever seu código!



### Exercício 6.4

Escreva uma função `def filtrapalavras(lista):` que receba uma lista de palavras (por exemplo: ["tenha", "um", "bom", "dia"]) e retorne outra lista contendo apenas as palavras com mais de 2 caracteres (nesse exemplo, ["tenha", "bom", "dia"]).

Dicas:

- Este é um exercício que usa repetição para percorrer a `lista` elemento por elemento.
- Você vai precisar construir uma nova lista adicionando nela apenas as palavras que satisfizerem a condição.




