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
          https://cdn.jsdelivr.net/gh/andreainfufsm/elc106-2023a/classes/13/custom.css

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/13/README.md)

# Aula 13

- Correção das questões da prova
- Exercícios: análise de notas
- Próximas avaliações


## Correção de questões 

Avance para ver soluções das questões.

### Questão 1



Qual será a saída deste código? 


``` python
def func(ns):
   res = []
   for n in ns:
      if n % 2 == 1:
        res.append(n+1)
      else:
        res.append(n)
   return res
   
print(func([89, 22, 45, 46]))
i = 10
z = [i+4, i+5]
print(func(z))
```
@Pyodide.eval


<img src="img/fish-food-chain.png">


<br>
<br>
<h3>Passo-a-passo no Python Tutor</h3>




Execute este programa passo-a-passo no [Python Tutor](https://pythontutor.com/render.html#code=def%20func%28ns%29%3A%0A%20%20%20res%20%3D%20%5B%5D%0A%20%20%20for%20n%20in%20ns%3A%0A%20%20%20%20%20%20if%20n%20%25%202%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20res.append%28n%2B1%29%0A%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20res.append%28n%29%0A%20%20%20return%20res%0A%20%20%20%0Aprint%28func%28%5B89,%2022,%2045,%2046%5D%29%29%0Ai%20%3D%2010%0Az%20%3D%20%5Bi%2B4,%20i%2B5%5D%0Aprint%28func%28z%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false):




<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20func%28ns%29%3A%0A%20%20%20res%20%3D%20%5B%5D%0A%20%20%20for%20n%20in%20ns%3A%0A%20%20%20%20%20%20if%20n%20%25%202%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20res.append%28n%2B1%29%0A%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20res.append%28n%29%0A%20%20%20return%20res%0A%20%20%20%0Aprint%28func%28%5B89,%2022,%2045,%2046%5D%29%29%0Ai%20%3D%2010%0Az%20%3D%20%5Bi%2B4,%20i%2B5%5D%0Aprint%28func%28z%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### Questão 2

Reescreva o código abaixo usando `while`:

``` python
for i in range(1,11):
   print('9 *', i, '=', 9*i)
```
@Pyodide.eval

``` python
i = 1
while i < 11:
   print('9 *', i, '=', 9*i)
   i = i + 1
```
@Pyodide.eval


``` python
i = 0
while i < 10:
  i = i + 1
  print('9 *', i, '=', 9*i)
   
```
@Pyodide.eval



``` python
num = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 10:
   print('9 *', num[i], '=', 9*num[i])
   i = i + 1
```
@Pyodide.eval





### Questão 3


Qual será a saída deste código? 



``` python
def func(a,b):
   if len(a) > len(b):
      return len(a)
   else:
      return len(b)
         
lista = ['programa', 'python', 'algoritmo']
print(func(lista[1], lista[2]))
```
@Pyodide.eval


### Questão 4

Qual será a saída deste código?


``` python
x = 0
for i in range(1, 3):
    for j in ['a', 'b']:
        x = x + i
        print(i, j)
print(x)
```
@Pyodide.eval


Observações:

- Laços aninhados: para cada i, executa todas as repetições para j
- Questão com menor média de acertos



Execute este programa passo-a-passo no [Python Tutor](https://pythontutor.com/render.html#code=x%20%3D%200%0Afor%20i%20in%20range%281,%203%29%3A%0A%20%20%20%20for%20j%20in%20%5B'a',%20'b'%5D%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20x%20%2B%20i%0A%20%20%20%20%20%20%20%20print%28i,%20j%29%0Aprint%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false):




<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=x%20%3D%200%0Afor%20i%20in%20range%281,%203%29%3A%0A%20%20%20%20for%20j%20in%20%5B'a',%20'b'%5D%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20x%20%2B%20i%0A%20%20%20%20%20%20%20%20print%28i,%20j%29%0Aprint%28x%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


### Questão 5


Obs.: Questão com **maior** média de acertos

Deseja-se definir uma função que retorne a soma S dos N primeiros termos da série
abaixo:

$ S = \sum{1 + \frac{1}{4} + (\frac{1}{4})^2 + (\frac{1}{4})^3 + (\frac{1}{4})^4 + ...} $

Após ser definida, essa função deverá ser chamada para calcular a soma dos 20
primeiros termos da série.

Desembaralhe:



``` python
return soma
print(serie(20))
for i in range(n):
def serie(n):
soma = 0
soma = soma + (1/4)**i
```
@Pyodide.eval


<details>
  <summary>Clique para ver a solução</summary>
  <pre>  
  def serie(n):<br>
      soma = 0<br>
      for i in range(n):<br>
          soma = soma + (1/4)**i<br>
      return soma<br>
  print(serie(20))<br>
  </pre>
</details> 






## Exercícios: análise de notas


O que faz este programa?

``` python
q1 = [0.9,1,1,0.8,0.2,0.4,0,0,0.1,0,0.2,0,0.5,0,0.5,0,0.9,0.2,1,1,0.2,1]
q2 = [1,1,1,0.5,0,1,0.5,0,0.1,0,0,0,1,0,0,0,1,0.2,1,1,0,1]
q3 = [1,1,1,0.7,0.8,0.7,1,0,1,0,0,0,1,0,0.4,0.7,0.9,0.6,1,0.8,0.7,1]
q4 = [0.7,0.8,1,0.8,0.2,0.5,0,0,0.2,0,0.2,0,0,0,0.4,0,0.4,0.7,0.8,0.4,0.8,1]
q5 = [0.8,0.9,1,0.8,0.5,1,0.8,0,0.9,0,0.4,0,0.8,0,0.8,1,0.4,0.8,1,1,1,0.8]

soma = 0
for nota in q1:
  soma += nota
resultado = soma / len(q1)

print(resultado)
```
@Pyodide.eval


### Modifique (1)

- **Copie** este programa para o Repl.it 
- Qual foi a média de notas da questão 5? Modifique o programa para calcular e mostrar essa média, a fim de responder à questão

``` python
q1 = [0.9,1,1,0.8,0.2,0.4,0,0,0.1,0,0.2,0,0.5,0,0.5,0,0.9,0.2,1,1,0.2,1]
q2 = [1,1,1,0.5,0,1,0.5,0,0.1,0,0,0,1,0,0,0,1,0.2,1,1,0,1]
q3 = [1,1,1,0.7,0.8,0.7,1,0,1,0,0,0,1,0,0.4,0.7,0.9,0.6,1,0.8,0.7,1]
q4 = [0.7,0.8,1,0.8,0.2,0.5,0,0,0.2,0,0.2,0,0,0,0.4,0,0.4,0.7,0.8,0.4,0.8,1]
q5 = [0.8,0.9,1,0.8,0.5,1,0.8,0,0.9,0,0.4,0,0.8,0,0.8,1,0.4,0.8,1,1,1,0.8]

soma = 0
for nota in q1:
  soma += nota
resultado = soma / len(q1)

print(resultado)
```
@Pyodide.eval

### Modifique (2)

- **Copie** este programa para o Repl.it 
- Modifique-o para calcular e mostrar as médias de notas de cada uma das 5 questões (recomendação: defina uma função para o cálculo da média e use-a 5 vezes!)


``` python
q1 = [0.9,1,1,0.8,0.2,0.4,0,0,0.1,0,0.2,0,0.5,0,0.5,0,0.9,0.2,1,1,0.2,1]
q2 = [1,1,1,0.5,0,1,0.5,0,0.1,0,0,0,1,0,0,0,1,0.2,1,1,0,1]
q3 = [1,1,1,0.7,0.8,0.7,1,0,1,0,0,0,1,0,0.4,0.7,0.9,0.6,1,0.8,0.7,1]
q4 = [0.7,0.8,1,0.8,0.2,0.5,0,0,0.2,0,0.2,0,0,0,0.4,0,0.4,0.7,0.8,0.4,0.8,1]
q5 = [0.8,0.9,1,0.8,0.5,1,0.8,0,0.9,0,0.4,0,0.8,0,0.8,1,0.4,0.8,1,1,1,0.8]

soma = 0
for nota in q1:
  soma += nota
resultado = soma / len(q1)

print(resultado)
```
@Pyodide.eval


### Modifique (3)


- **Copie** este programa para o Repl.it 
- Quantos estudantes tiveram nota máxima na questão 1? Modifique o programa para obter esse valor, de forma a responder à questão


``` python
q1 = [0.9,1,1,0.8,0.2,0.4,0,0,0.1,0,0.2,0,0.5,0,0.5,0,0.9,0.2,1,1,0.2,1]
q2 = [1,1,1,0.5,0,1,0.5,0,0.1,0,0,0,1,0,0,0,1,0.2,1,1,0,1]
q3 = [1,1,1,0.7,0.8,0.7,1,0,1,0,0,0,1,0,0.4,0.7,0.9,0.6,1,0.8,0.7,1]
q4 = [0.7,0.8,1,0.8,0.2,0.5,0,0,0.2,0,0.2,0,0,0,0.4,0,0.4,0.7,0.8,0.4,0.8,1]
q5 = [0.8,0.9,1,0.8,0.5,1,0.8,0,0.9,0,0.4,0,0.8,0,0.8,1,0.4,0.8,1,1,1,0.8]

soma = 0
for nota in q1:
  soma += nota
resultado = soma / len(q1)

print(resultado)
```
@Pyodide.eval


### Modifique (4)

- **Copie** este programa para o Repl.it 
- Modifique o programa para obter, para cada questão, a quantidade de estudantes que acertaram totalmente a questão (nota máxima, `==1`)


``` python
q1 = [0.9,1,1,0.8,0.2,0.4,0,0,0.1,0,0.2,0,0.5,0,0.5,0,0.9,0.2,1,1,0.2,1]
q2 = [1,1,1,0.5,0,1,0.5,0,0.1,0,0,0,1,0,0,0,1,0.2,1,1,0,1]
q3 = [1,1,1,0.7,0.8,0.7,1,0,1,0,0,0,1,0,0.4,0.7,0.9,0.6,1,0.8,0.7,1]
q4 = [0.7,0.8,1,0.8,0.2,0.5,0,0,0.2,0,0.2,0,0,0,0.4,0,0.4,0.7,0.8,0.4,0.8,1]
q5 = [0.8,0.9,1,0.8,0.5,1,0.8,0,0.9,0,0.4,0,0.8,0,0.8,1,0.4,0.8,1,1,1,0.8]

soma = 0
for nota in q1:
  soma += nota
resultado = soma / len(q1)

print(resultado)
```
@Pyodide.eval


### Pense, analise, programe (5)

Agora é sua vez de **pensar** em questões que podem ser perguntadas/respondidas sobre as notas das avaliações:

- Observe os dados
- Formule uma questão
- Escreva o programa para responder à questão
- Se necessário, você pode pesquisar e utilizar funções pré-definidas em bibliotecas


### Entregue no Moodle

- No projeto no Repl.it criado para esta aula, você deve ter soluções e/ou registros (código parcial e comentários) sobre o que você tentou
- No referido projeto no Repl.it, copie o link do projeto criado para esta aula (por exemplo: https://replit.com/@seunome/aula13)
- Entregue o link na atividade do Moodle correspondente à aula 13
- Certifique-se de que o projeto esteja em modo público 



## Próximas avaliações

Veja a seguir as orientações sobre as próximas avaliações.

### Registro de prática extraclasse (peso 3.0)

- Cada estudante deverá entregar link para 3 screencasts
- Cada screencast deverá:

  - explicar uma solução de um exercício proposto que você considerou difícil
  - ter uma linguagem espontânea (não vale ler uma explicação)
  - mostrar a execução do código
  - ter no máximo 5min (você pode cortar alguma parte, se necessário)
  - ser entregue até a semana seguinte à aula em que foi proposto

- Opcionalmente, caso você se interesse em ir além do que é visto em aula, ou até mesmo adiantar alguma entrega, você pode combinar com a professora outro(s) exercício(s), em substituição àqueles propostos em aula

- O terceiro screencast deve, preferencialmente, abordar o projeto final (todo ou parte do código do projeto)

- A avaliação levará em conta a atenção aos requisitos, a explicação / demonstração e o alinhamento do grau de dificuldade com as avaliações anteriores

- Sugestão de software para gravação de screencast: Loom (https://www.loom.com/signup), ou procure por outros similares

### Projeto final (peso 7.0)

- O projeto final consistirá na proposta e desenvolvimento incremental de um programa em Python, a fim de resolver um problema e/ou explorar outros recursos de programação (bibliotecas, funções, etc.)
- A proposta deve ser enviada no Moodle e validada pela professora
- O trabalho poderá ser desenvolvido de forma individual ou em dupla, mas a nota será individual, baseada no progresso, contribuição e aproveitamento de cada estudante, em coerência com as avaliações anteriores, verificado durante as aulas e na apresentação
- Data de apresentação: 24/07/2024



<h4>Apresentação</h4>

- O programa deverá ser demonstrado para a turma usando o Repl.it (ou qualquer ferramenta que permita executar o programa).
- Em aproximadamente 5 minutos, deve ser explicado/mostrado:

  - A proposta / enunciado do problema (o que o programa resolve)
  - O processo de resolução (detalhar também recursos/ferramentas auxiliares, prompts usados, etc.)
  - Uma ou mais execuções do programa
  - Detalhamento de algumas linhas de código consideradas mais "difíceis" de entender
  
- Em caso de trabalho em dupla, cada integrante deve participar, alternando momentos de fala e de operação no computador


<h4>Rubricas de avaliação</h4>



<!-- data-type="none" -->
| Descrição   | Nota   |
| :--------- | :--------- |
| Trabalho completamente alinhado com as instruções, demonstrando domínio de lógica e recursos de programação | 10 |
| Trabalho aderente a algumas instruções ou com demonstração de domínio parcial de recursos de programação  | 7 a 9 |
| Trabalho desalinhado com instruções ou com demonstração de pouco domínio de lógica e programação, mas com progresso evidente em relação a outras avaliações  | 5 a 7 |
| Trabalho muito distante das instruções  | < 5  |
| Trabalho não entregue ou com indícios de desonestidade acadêmica   | 0 |