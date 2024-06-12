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

script:   https://cdn.jsdelivr.net/pyodide/v0.24.0/full/pyodide.js


@Pyodide.exec: @Pyodide.exec_(@uid,```@0```)

@Pyodide.exec_
<script>
async function run(code, force=false) {
    if (!window.pyodide_running || force) {
        window.pyodide_running = true
    
        const plot = document.getElementById('target_@0')
        plot.innerHTML = ""
        document.pyodideMplTarget = plot

        if (!window.pyodide) {
            try {
                window.pyodide = await loadPyodide({fullStdLib: false})
                window.pyodide_modules = []
                window.pyodide_running = true
            } catch(e) {
                send.lia(e.message, false)
                send.lia("LIA: stop")
            }
        }

        try {
            window.pyodide.setStdout((text) => console.log(text))
            window.pyodide.setStderr((text) => console.err(text))

            window.pyodide.setStdin({stdin: () => {
            return prompt("stdin")
            }})
        
            const rslt = await window.pyodide.runPython(code)
            
            if (rslt !== undefined) {
                send.lia(rslt)
            } else {
                send.lia("")
            }
        } catch(e) {
            let module = e.message.match(/ModuleNotFoundError: The module '([^']+)/i)

            window.console.warn("Pyodide", e.message)
        
            if (!module) {
                send.lia(e.message, false)
            
            } else {
                if (module.length > 1) {
                    module = module[1]

                    if (window.pyodide_modules.includes(module)) {
                        console.warn(e.message)
                        send.lia(e.message, false)
                    } else {
                        send.lia("downloading module => " + module)
                        window.pyodide_modules.push(module)
                        await window.pyodide.loadPackage(module)
                        await run(code, true)
                    }
                }
            }
        }
        send.lia("LIA: stop")
        window.pyodide_running = false
    } else {
        setTimeout(() => { run(code) }, 1000)
    }
}

setTimeout(() => { run(`@1`) }, 500)

"calculating, please wait ..."

</script>

<div id="target_@0"></div>
@end





@Pyodide.eval: @Pyodide.eval_(@uid)

@Pyodide.eval_
<script>
async function run(code) {

    const plot = document.getElementById('target_@0')
    plot.innerHTML = ""
    document.pyodideMplTarget = plot

    if (!window.pyodide) {
        try {
            window.pyodide = await loadPyodide({fullStdLib: false})
            window.pyodide_modules = []
            window.pyodide_running = true
        } catch(e) {
            console.error(e.message)
            send.lia("LIA: stop")
        }
    }

    try {
        window.pyodide.setStdout({ write: (buffer) => {
            const decoder = new TextDecoder()
            const string = decoder.decode(buffer)
            console.stream(string)
            return buffer.length
        }})

        window.pyodide.setStderr({ write: (buffer) => {
            const decoder = new TextDecoder()
            const string = decoder.decode(buffer)
            console.err(string)
            return buffer.length
        }})

        window.pyodide.setStdin({stdin: () => {
          return prompt("stdin")
        }}) 
       
        const rslt = await window.pyodide.runPython(code)

        if (typeof rslt === 'string') {
            send.lia(rslt)
        }
    } catch(e) {
        let module = e.message.match(/ModuleNotFoundError: The module '([^']+)/i)

        window.console.warn("Pyodide", e.message)
    
        if (!module) {
            const err = e.message.match(/File "<exec>", line (\d+).*\n((.*\n){1,3})/i)

            if (err!== null && err.length >= 3) {
                send.lia( e.message,
                  [[{ row : parseInt(err[1]) - 1,
                      column : 1,
                      text : err[2],
                      type : "error"
                  }]],
                  false)
            } else {
                console.error(e.message)
            }
        } else {
            if (module.length > 1) {
                module = module[1]

                if (window.pyodide_modules.includes(module)) {
                    console.error(e.message)
                } else {
                    console.debug("downloading module =>", module)
                    window.pyodide_modules.push(module)
                    await window.pyodide.loadPackage(module)
                    await run(code)
                }
            }
        }
    }
    send.lia("LIA: stop")
    window.pyodide_running = false
}

if (window.pyodide_running) {
  setTimeout(() => {
    console.warn("Another process is running, wait until finished")
  }, 500)
  "LIA: stop"
} else {
  window.pyodide_running = true

  setTimeout(() => {
    run(`@input`)
  }, 500)

  "LIA: wait"
}
</script>

<div id="target_@0"></div>
@end

-->




<!--
liascript-devserver --input README.md --port 3001 --live
link:     https://cdn.jsdelivr.net/gh/liascript/custom-style/custom.min.css
          https://cdn.jsdelivr.net/gh/andreainfufsm/elc106-2023a/classes/10/custom.css

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/11/README.md)

# Aula 11

- Revisão
- Mais repetição com `for` 


## Revisão 

Avance para ver soluções de exercícios da aula passada e novos exercícios de revisão.

### Correção da questão de concurso


Qual será a saída deste código? (problema proposto na [seção de revisão](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/10/README.md#5) da aula passada)


``` python
def xpto(n1, n2):
  while n1 != n2:
    if (n1 < n2):
      n2 = n2 - n1
    else:
      n1 = n1 - n2
  return n1
print(xpto(20,5))
```
@Pyodide.eval

Fonte: Questão adaptada de prova de concurso elaborada pela FGV 


#### Resposta (curta) em tabela

![](img/trace-table-xpto.png)


#### Resposta (longa) em detalhes


Para entender este código, você precisa lembrar que o computador vai executar as instruções passo-a-passo.

``` python
def xpto(n1, n2):
  while n1 != n2:
    if (n1 < n2):
      n2 = n2 - n1
    else:
      n1 = n1 - n2
  return n1
print(xpto(20,5))
```
@Pyodide.eval


Vamos detalhar isso e aproveitar para revisar conteúdos importantes vistos nas aulas.

> Clique na seta -> abaixo para avançar



                 {{1}}
************************************************

**Execução de sequências**

Em muitos programas, alguns passos ocorrem em sequência, uma linha imediatamente após a outra. Sequências de instruções são a forma mais simples de construir um programa.

Por exemplo, no código abaixo, temos apenas instruções em sequência:

```python
num = 0
print('O número é', num)
num = num + 1
print('Agora o número é', num)
```
@Pyodide.eval

************************************************



                 {{2}}
************************************************

**Execução de funções, condicionais e repetições**

Algumas instruções que vimos nas aulas alteram a ordem de execução, provocando "desvios" ou "saltos" de uma linha para outra. Isso acontece, por exemplo, com funções, com condicionais (`if`/`elif`/`else`) e com repetições (`while`/`for`),

Para entender essas instruções mais "poderosas" (e nada óbvias), você também precisa entender que o Python agrupa linhas em **blocos**. Linhas que formam um mesmo bloco precisam estar alinhadas - devem iniciar na mesma coluna. Além disso, blocos afetados por algumas instruções (`def`, `if/elif/else`, `while`, `for`, etc.) devem estar recuados em relação à instrução. Chamamos esse recuo de "endentação", "indentação" ou "indent".


************************************************

                 {{3}}
************************************************

**Blocos endentados em funções**

Quando temos uma definição de função, as linhas que compõem os comandos dessa função fazem parte de um bloco. Esse bloco precisa estar recuado em relação à primeira linha da função. 

No exemplo abaixo, as linhas 2, 3 e 4 estão recuadas e formam o bloco de instruções da função `func`. As linhas 5 e 6 não fazem parte do bloco - essas linhas compõem o bloco principal do programa, que é executado em sequência.

```python
def func(x):
  x = x + 1
  x = x * 2
  return x
resultado = func(4)
print(resultado)  
```
@Pyodide.eval


************************************************



                 {{4}}
************************************************

**Blocos endentados em condicionais**


Aqui temos um código que sorteia um número entre 2 opções: 0 ou 1, usando a função `randint`. Se (`if`) o número for igual (`==`) a 0, o programa mostra na tela o texto `Cara`. Caso contrário (senão, `else`), mostra o texto `Coroa`. As linhas 4 e 6 estão endentadas/recuadas porque são as instruções que serão executadas em cada situação, ou seja, se a condição for verdadeira (n igual a 0) ou se a condição for falsa (n diferente de 0). Caso tivéssemos mais instruções a executar em cada caso, as linhas de código deveriam estar recuadas também, exatamente como as linhas 4 e 6.

Note que as linhas 3, 4, 5 e 6 nunca serão executadas juntas em sequência. Conforme a condição for verdadeira ou falsa, um dos blocos (linha 4 ou linha 6) será executado e outro não.

```python
from random import randint
n = randint(0,1)
if n == 0:
  print('Cara')
else:
  print('Coroa')
```
@Pyodide.eval

************************************************

                 {{5}}
************************************************

**Blocos endentados em repetições**

Neste outro código, temos uma repetição com `for`. Para cada item de uma lista de sabores de sorvete, o programa mostrará uma mensagem na tela. A linha 2 está endentada/recuada porque é a instrução que será repetida. A linha 3 não faz parte do bloco `for` e, portanto, não será repetida - será executada somente depois que a execução do loop (laço) terminar.


```python
for sabor in ['morango', 'chocolate', 'flocos']:
  print('Gosto de sorvete de', sabor)
print('Fim')  
```
@Pyodide.eval


************************************************




                 {{6}}
************************************************

**Voltando ao código inicial**

Depois da breve revisão, vamos nos concentrar de novo no código que estávamos analisando.

Veja que este código possui várias linhas recuadas, compondo diferentes blocos.

```python
1: def xpto(n1, n2):
2:   while n1 != n2:
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1
8: print(xpto(20,5))
```

************************************************

                 {{7}}
************************************************

**Linha 1 - definição de função**

Quando o computador encontra uma linha de definição de função, ele apenas guarda essa definição na memória, para uso futuro. A função só será executada quando for chamada em outra linha de código, com valores para seus argumentos. Ou seja, uma definição de função não tem efeito imediato na execução do programa.

Então, quando a execução passo-a-passo chegar em uma linha de definição de função, a execução continua após o bloco de comandos da função.

No código abaixo, a definição da função vai da linha 1 até a linha 7. Então, a execução do programa salta da linha 1 para a linha 8, que é a próxima (e única) linha após a definição da função. Como sabemos isso? Porque a linha 8 não está recuada como as linhas 2 a 7. 

```python
1: def xpto(n1, n2):
2:   while n1 != n2:
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1
8: print(xpto(20,5))
```
************************************************

                 {{8}}
************************************************

**Linha 8 - chamada de função**


Na linha 8, temos o comando `print`, que é um comando de saída - serve para instruir o computador a mostrar algo na tela. 
Este `print` é bem simples: o único dado a ser impresso vai ser o resultado da função `xpto`  aplicada aos valores `20` e `5`.
O `print` só poderá ser feito quando tivermos o resultado de `xpto`, por isso a execução vai saltar da linha 8 para a linha 1, desta vez para realmente executar a função `xpto`.

Quando chamamos (ou aplicamos) uma função, colocamos entre parênteses valores para seus parâmetros. Chamamos isso de passagem de argumentos/parâmetros. Esses valores serão usados na execução da função, na ordem em que foram passados, da mesma forma que usamos variáveis.
No exemplo, o parâmetro `n1` receberá o valor `20` e o parâmetro `n2` receberá o valor `5`. 

************************************************

                 {{9}}
************************************************

**Linha 2 - repetição**


Agora que temos valores de `n1`  e `n2`, podemos prosseguir na execução passo-a-passo. A próxima linha a ser executada será a 2, que inicia um bloco de repetição `while`.  Este comando do Python serve para repetir a execução de um bloco de comandos enquanto uma dada condição for verdadeira. Neste exemplo, a condição é `n1 != n2`, que significa "n1 diferente de n2". Como neste ponto realmente `n1` é diferente de `n2` (pois 20 é diferente de 5), a execução prossegue na linha 3.

```python
1: def xpto(n1, n2):
2:   while n1 != n2:    # <== estamos aqui
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1
8: print(xpto(20,5))
```

************************************************


                 {{10}}
************************************************

**Linha 3 - condicional**

Na linha 3, temos uma instrução `if` com a condição `n1 < n2`. Neste ponto da execução, a condição será `False`, pois n1 (20) não é menor que n2 (5). A execução não entra no bloco representado pela linha 4 - essa linha só seria executada se n1 fosse menor que n2. Ocorre um salto da execução para o `else` (senão), que instrui o que deve ser feito caso a condição da linha 3 não seja verdadeira. 

```python
1: def xpto(n1, n2):
2:   while n1 != n2:    
3:     if (n1 < n2):      # <== aqui testamos a condição
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2     # <== esta linha será executada
7:   return n1
8: print(xpto(20,5))
```

Na linha 6, que é o bloco do `else`, ocorre uma atualização da variável `n1`: seu valor era 20 e agora passa a ser 20-5, que é igual a 15.
Após a linha 6, a execução **não** segue para a linha 7! A linha 6 faz parte do bloco do `while`, que representa um laço, e por isso a execução salta para o início do `while`, linha 2. 

************************************************

                 {{11}}
************************************************

**Linha 2 - repetição continua**


```python
1: def xpto(n1, n2):
2:   while n1 != n2:    # <== voltamos para cá
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1
8: print(xpto(20,5))
```

Neste ponto da execução, o `while` vai verificar novamente a condição. Desta vez, temos `n1=15` e `n2=5`. Os valores mudaram, mas a condição `n1 != n2` continua
verdadeira, pois 15 é diferente de 5.  

A execução vai novamente para a linha 3, onde temos a instrução `if` com a condição `n1 < n2`, que será novamente `False`, pois 15 não é menor que 5. Ocorre novamente um salto da execução para o `else`, que faz executar a linha 6.

Na linha 6, temos novamente a atualização de `n1`: seu valor era 15 e agora passa a ser 15-5, que é igual a 10.
Após a linha 6, a execução salta para o início do laço, linha 2.

************************************************

                 {{12}}
************************************************

**Linha 2 - repetindo mais uma vez**


```python
1: def xpto(n1, n2):
2:   while n1 != n2:    # <== repetindo mais uma vez
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1
8: print(xpto(20,5))
```

Mais uma vez, o `while` vai verificar a condição. Desta vez, temos `n1=10` e `n2=5`. Os valores mudaram de novo, mas a condição `n1 != n2` continua
verdadeira, pois 10 é diferente de 5.  A execução vai novamente para a linha 3, onde temos a instrução `if` com a condição `n1 < n2`, que será mais uma vez `False`, pois 10 não é menor que 5. Ocorre novamente um salto da execução para o `else`, que faz executar a linha 6.

Na linha 6, temos outra vez a atualização de `n1`: seu valor era 10 e agora passa a ser 10-5, que é igual a 5.
Após a linha 6, a execução salta para o início do laço, linha 2.


************************************************


                 {{13}}
************************************************

**Linha 2 - repetição chega ao fim**

```python
1: def xpto(n1, n2):
2:   while n1 != n2:    # <== finalmente vai ser False
3:     if (n1 < n2):
4:       n2 = n2 - n1
5:     else:
6:       n1 = n1 - n2
7:   return n1          # <== agora podemos retornar
8: print(xpto(20,5))
```

Na linha 2, o `while` vai verificar novamente a condição. Agora temos `n1=5` e `n2=5`. A condição `n1 != n2` (n1 diferente de n2) finalmente será `False`, então termina a repetição do bloco. Qual a próxima linha depois do bloco? É a linha 7, que indica que a função deve **retornar** (`return`) o resultado (n1=5) para o ponto do código em que foi chamada, ou seja, a linha 8.

************************************************

                 {{14}}
************************************************

**Linha 8 - resultado final**

Na linha 8, agora temos o resultado da função `xpto`, que é 5. Portanto, finalmente o `print` poderá mostrar esse resultado na tela.

************************************************



#### Passo-a-passo no Python Tutor




Execute este programa passo-a-passo no [Python Tutor](https://pythontutor.com/visualize.html#code=def%20xpto%20%28n1,%20n2%29%3A%0A%20%20while%20n1%20!%3D%20n2%3A%0A%20%20%20%20if%20%28n1%20%3C%20n2%29%3A%0A%20%20%20%20%20%20n2%20%3D%20n2%20-%20n1%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20n1%20%3D%20n1%20-%20n2%0A%20%20return%20n1%0Aprint%28xpto%2820,5%29%29&cumulative=false&curInstr=15&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false):



<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20xpto%20%28n1,%20n2%29%3A%0A%20%20while%20n1%20!%3D%20n2%3A%0A%20%20%20%20if%20%28n1%20%3C%20n2%29%3A%0A%20%20%20%20%20%20n2%20%3D%20n2%20-%20n1%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20n1%20%3D%20n1%20-%20n2%0A%20%20return%20n1%0Aprint%28xpto%2820,5%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=15&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>



### Solução de exercícios

Soluções para os exercícios de escrita de código propostos na aula passada:

- [Exercício 1](src/aula10_solucao_ex1.py)
- [Exercício 2](src/aula10_solucao_ex2.py)
- [Exercício 3](src/aula10_solucao_ex3.py)
- [Exercício 4](src/aula10_solucao_ex4.py)
- [Exercício 5](src/aula10_solucao_ex5.py)
- [Exercício 6](src/aula10_solucao_ex6.py)
- [Exercício 7](src/aula10_solucao_ex7.py)

### Vídeo

> Ative legenda automática em português!

Veja este vídeo que resume os conceitos de sequências, condicionais/seleções e laços/loops/iterações usando exemplos do dia-a-dia (não é Python!)



<iframe width="560" height="315" src="https://www.youtube.com/embed/eSYeHlwDCNA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### Questões




                 {{1}}
************************************************

Quais linhas fazem parte do bloco de instruções da função `func`?

```python
1: def func(x):
2:   x = x + 1
3:   x = x + 2
4:   return x
5: z = func(10)
6: print(z)
```


- [( )] 2 a 3
- [(x)] 2 a 4
- [( )] 1 a 6

************************************************



                 {{3}}
************************************************

Qual será a saída do programa abaixo?

```python
def func(x):
  x = x + 1
  x = x + 2
  return x
z = func(10)
print(z)
```


- [( )] 10
- [( )] 12
- [(x)] 13

************************************************



                 {{4}}
************************************************

Qual será a saída do programa abaixo?

```python
def func(a, b):
  a += 2
  b += 3
  if b > a:
    return b
  else:
    return a  
z = func(10, 11)
print(z)
```


[( )] 13
[(x)] 14
[( )] 15

************************************************




                 {{5}}
************************************************

O que será mostrado na saída deste programa?

```python
words = ['I', 'love', 'Python']
for w in words:
  if len(w) > 6:
    print(w)   
```


[( )] `Python`
[(x)] nada
[( )] não sei

************************************************


                 {{6}}
************************************************

O que será mostrado ao final deste programa?

```python
pets = ['bird', 'cat', 'dog', 'pumpkin']
s = ''
for i in range(len(pets)):
  s += pets[i][0]
print(s) 
```


[( )] `bird`
[( )] vazio
[(x)] `bcdp`

************************************************

                 {{7}}
************************************************

Sabendo que a função `sum` calcula o somatório de elementos de uma lista/sequência, qual será o resultado de:

```python
sum(range(10,20,5))
```

[[25]]



************************************************



                 {{8}}
************************************************

No código abaixo, quais linhas fazem parte do bloco de instruções do `for` (ou seja, qual o bloco a ser repetido)?


```python
1: from random import randint
2: for contador in range(5): # contador não é usado
3:    n = randint(1, 6)
4:    print('Sorteamos o número', n)
5:    if n == 6:
6:       print('Oba, tiramos o maior número!')
```
 



- [( )] 1 a 6
- [( )] 3 e 4
- [(x)] 3 a 6

************************************************






## Mais repetição com `for`


Tanto `while` como `for` repetem um bloco de instruções...


<img src="img/python-while-loop.png" width="350"> 
<img src="img/python-for-loop.png" width="350"> 


### Laços aninhados

> Em inglês: nested loops

Bloco de comandos de um laço pode conter outro(s) laço(s)!



Qual será a saída?

```python  
for w in ['happ', 'bus']:
  for s in ['y', 'ier','iest']:
    word = w+s
    print(word)
    #print(f'{w}{s}')
```
@Pyodide.eval


Observações:

- Note a concatenação de strings: `w+s`
- Veja no comentário uma outra forma de formar novas strings: `f'{w}{s}'` (recurso chamado f-string em Python)


#### Outro exemplo

Qual será a saída?

```python  
for i in range(3):
  for j in [4,5,6]:
    print(i, j, i+j)
    #print(f'{i}+{j} = {i+j}')
```
@Pyodide.eval

#### Passo-a-passo


Passo-a-passo no Python Tutor:


<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20i%20in%20range%283%29%3A%0A%20%20for%20j%20in%20%5B4,5,6%5D%3A%0A%20%20%20%20print%28i,%20j,%20i%2Bj%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


#### Elefantes incomodam

Como fazer um programa para gerar a letra desta música para um número `n` de elefantes?


```
1 elefante incomoda muita gente
2 elefantes incomodam, incomodam muito mais!
3 elefantes incomodam muita gente
4 elefantes incomodam, incomodam incomodam, incomodam muito mais!
5 elefantes incomodam muita gente
6 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam muito mais!
7 elefantes incomodam muita gente
8 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam muito mais!
9 elefantes incomodam muita gente
10 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam muito mais!
```

Marque os recursos de programação que podem ajudar neste problema:

- [[x]] repetição com `for`
- [[ ]] função `math.sqrt`
- [[x]] condicional com `if`/`else`
- [[x]] função `print`
- [[ ]] função `random.randint`
- [[x]] concatenação de strings
- [[x]] cálculo de resto de divisão
- [[x]] função `range`
- [[ ]] `append` em lista

## Exercícios

### Exercício 1

(Adaptado de [fmasanori](https://github.com/fmasanori/PPZ)) Escreva um programa que leia o valor (inteiro) de uma conta e o valor de um pagamento efetuado, e mostre como fornecer o troco usando um mínimo de cédulas de 50, 20, 10, 5, 2 e 1.

Exemplos de execução:

```
Conta: 167
Pagamento: 200
Uma nota de 20
Uma nota de 10
Uma nota de 2
Uma nota de 1
```

```
Conta: 56
Pagamento: 100
Uma nota de 20
Uma nota de 20
Uma nota de 2
Uma nota de 2
```


### Exercício 2

Escreva um programa que peça repetidamente ao usuário para digitar um número inteiro n dentro do intervalo fechado 1 e 20 (use `while True:` e `break`). Depois que obtiver um n válido, o programa deve mostrar a música dos elefantes para o número n, conforme o exemplo abaixo:

Exemplo de execução:

```
Digite n: -1
Precisamos de elefantes. Digite novamente.
Digite n: 99
Muitos elefantes. Digite novamente.
Digite n: 0
Precisamos de elefantes. Digite novamente.
Digite n: 6
1 elefante incomoda muita gente
2 elefantes incomodam, incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam, incomodam, incomodam, incomodam muito mais
5 elefantes incomodam muita gente
6 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam muito mais
```


### Exercício 3

Deseja-se escrever uma função que receba uma lista de palavras e retorne o total de vogais minúsculas destas strings. Por exemplo, se a lista for `['roxo', 'amarelo', 'verde']`, o resultado da função será 8. 

O código abaixo resolve este problema, mas está embaralhado. Desembaralhe o código para que funcione como esperado. Clique em "Get feedback" para verificar sua solução.


<iframe src="https://parsons.problemsolving.io/puzzle/a09df6fec5c5480ea71fab713ffd06c0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

