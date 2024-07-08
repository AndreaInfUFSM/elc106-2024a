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
          https://cdn.jsdelivr.net/gh/andreainfufsm/elc106-2023a/classes/14/custom.css

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/14/README.md)

# Aula 14


Nesta aula:

- Manipulação de dados em arquivos
- Biblioteca `csv`
- Biblioteca `matplotlib`
- Exercícios


## Manipulando dados em arquivos


![https://www.howtogeek.com/wp-content/uploads/2018/06/file-extensions-on-a-blue-background.jpg?width=1198&trim=1,1&bg-color=000&pad=1,1](https://www.howtogeek.com/wp-content/uploads/2018/06/file-extensions-on-a-blue-background.jpg?width=1198&trim=1,1&bg-color=000&pad=1,1)

- Trabalhar com dados em arquivos é abordagem "profissional": generalização, separação dados-código
- Linguagens de programação costumam ter **funções** para manipular arquivos
- Para escolher as funções apropriadas, é importante saber o **tipo/formato** do conteúdo do arquivo
- Conteúdo: textual (strings) ou binário
- Tipo/formato específico de um arquivo geralmente é expresso pela **extensão**
- Exemplos: imagens (.png, .gif, .jpeg, .jpg, .bmp, etc.), vídeos (.mp4, .mkv, etc.), dados textuais (.txt), dados tabulares (.csv, .xlsx, .ods, etc.), entre muitos outros
- Ver mais em https://www.file-extensions.org/


### Arquivos CSV

- Formato *Comma Separated Values* (CSV)
- Dados tabulares
- "Separados por vírgula" (mas podem ter outros delimitadores)

![](https://peltiertech.com/images/2017-02/csv-data-1.png)






### Bibliotecas

Muitas bibliotecas em Python facilitam a manipulação deste tipo de arquivo:

- Standard Library: https://docs.python.org/pt-br/3/library/csv.html
- NumPy: https://numpy.org/doc/stable/user/how-to-io.html
- Pandas: https://pandas.pydata.org/docs/reference/io.html
- Standard x Pandas: https://realpython.com/python-csv/
- Polars: https://pola.rs/ (melhor desempenho que Pandas)

> Pandas é a opção mais popular para análises de dados e uso profissional com pouca escrita de código.

> Para quem é iniciante em lógica de programação, vale treinar com a biblioteca CSV (built-in, standard).







## Biblioteca `csv`


Operações básicas:

- Abrir arquivo com `open` (biblioteca padrão)
- Gravar dados com funções `csv.writer` e `writerow`
- Ler dados com função `csv.reader`
- Manipular dados em listas (biblioteca padrão)
- Fechar arquivo com `close` (biblioteca padrão)

### Funções reader e writer

- Usamos essas funções depois de abrir arquivos para leitura / escrita 
- Função `writer` retorna um tipo de variável com capacidade de escrita em arquivo CSV
- Função `reader` retorna um tipo de variável com capacidade de leitura

``` python
import csv

f = open('notas.csv', 'w')
w = csv.writer(f)
w.writerow(['matricula', 'nota'])
w.writerow(['1234', '9'])
w.writerow(['1235', '10'])
w.writerow(['1236', '8.5'])
f.close()

f = open("notas.csv", "r")
r = csv.reader(f)
for row in r:
  print(row)
f.close()
```
@Pyodide.eval

### Cabeçalho

E se quisermos "pular" o cabeçalho?



 <details>
  <summary>Saiba como...</summary>
  <p>Podemos usar next(), uma função que se aplica a "iteráveis" em Python. 
Saiba mais em: https://cienciaprogramada.com.br/2021/08/iteradores-e-iteraveis-em-python/
  </p>
</details>



``` python
import csv

f = open('notas.csv', 'w')
w = csv.writer(f)
w.writerow(['matricula', 'nota'])
w.writerow(['1234', '9'])
w.writerow(['1235', '10'])
w.writerow(['1236', '8.5'])
f.close()

f = open("notas.csv", "r")
r = csv.reader(f)
next(r)
for row in r:
  print(row)
f.close()
```
@Pyodide.eval



### Exemplos com CSV

- Avance para ver alguns exemplos de código
- Execute os exemplos no Repl.it para ver os arquivos gerados

#### Escrita e leitura de arquivo

Escrita e leitura de arquivo usando biblioteca `csv`

``` python
import csv

f = open('matrix.csv', 'w')
w = csv.writer(f)
w.writerow(['x', 'y', 'z'])
for i in range(5):
  for j in range(4):
    w.writerow([i, j, i+j])
f.close()

f = open("matrix.csv", "r")
r = csv.reader(f)
matrix = []
for row in r:
  matrix.append(row)
f.close()
print(f'This matrix has {len(matrix)} rows and {len(matrix[0])} columns')

```
@Pyodide.eval

#### Download de CSV pela rede

Combinando CSV com a biblioteca `requests`

``` python
import requests
import csv

url = "http://www.inf.ufsm.br/~andrea/DATA.csv"

# Download the CSV file
response = requests.get(url)
content = response.text 

f = open("DATA.csv", "w")
f.write(content)
f.close()
print("Arquivo salvo com sucesso!")
```

> Atenção! No Repl.it, na aba Shell, digite `pip install requests` para instalar a biblioteca.

Saiba mais em...

- Simplificado: https://www.alura.com.br/conteudo/python-apis-conhecendo-biblioteca-requests
- Oficial: https://requests.readthedocs.io/en/latest/


#### Download e processamento

- Sem salvar arquivo em disco
- Trabalhando com delimitadores

``` python
import requests
import csv

url = "http://www.inf.ufsm.br/~andrea/DATA.csv"

# Download the CSV file
response = requests.get(url)
content = response.content.decode("utf-8").splitlines()


# Read the CSV content using csv module
reader = csv.reader(content, delimiter=';')
for row in reader:
  print(row[0]) ## primeira coluna, índice 0
```




## Biblioteca `matplotlib`


- Uma das mais "clássicas" bibliotecas de visualização de dados em Python
- Há muitas outras: 

  - Seabord, ggpy (como ggplot em R)
  - Mais "modernas", baseadas em JavaScript: Plotly, Bokeh, Vega

- Saiba mais em:

  - https://pyviz.org/overviews/ 
  - *The Python Visualization Landscape* (PyCon 2017): https://www.youtube.com/watch?v=FytuB8nFHPQ


![](https://rougier.github.io/python-visualization-landscape/landscape-colors.png)




### Tipos de gráficos

Há funções na biblioteca `matplotlib` para construir diversos tipos de gráficos: https://matplotlib.org/stable/plot_types/index.html

??[](https://matplotlib.org/stable/plot_types/index.html)

### Gráfico de linha

``` python
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7] 
#x = range(8)
y = x

plt.close('all')
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico X x Y')
plt.show()
```
@Pyodide.eval

### Gráfico de dispersão

``` python
import matplotlib.pyplot as plt

# Data from:
# https://www.datacamp.com/tutorial/tutorial-datails-on-correlation

experience = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35]

salary = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]

plt.close('all')
plt.scatter(experience,salary)
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Experience x Salary')
plt.show()
```
@Pyodide.eval


### Gráfico de barras


```python
import matplotlib.pyplot as plt

prova = ['Leitura', 'Escrita']
media = [8.5,7]

plt.close('all')
plt.bar(prova, media)
#plt.bar(prova, media, color='green')
#plt.barh(prova, media)

plt.xlabel('Prova')
plt.ylabel('Média')
plt.title('Médias por Tipo de Prova')
plt.show()
```
@Pyodide.eval



### Com `csv`

Observações:

- O código abaixo precisa ser copiado para o Repl.it
- Coloque também no Repl.it este arquivo: [prova2cols.csv](src/prova2cols.csv)

```python
import csv
import matplotlib.pyplot as plt

filename = 'prova2cols.csv'

leitura = []
escrita = []
# Obtém dados do do CSV e preenche listas
with open(filename, "r") as f:
  r = csv.reader(f)
  next(r) # salta cabeçalho
  for row in r:
    leitura.append(float(row[0]))
    escrita.append(float(row[1]))

# Plota notas da prova de leitura
# Eixo x = sequência gerada
# Eixo y = notas de leitura
plt.bar(range(len(leitura)), leitura)
# Ordenar: sorted(leitura)

# Alternativa: 
# gerar letras para designar cada estudante
#names = [chr(ord('A')+i) for i in range(len(leitura))]
#plt.bar(names,leitura)

plt.xlabel('Estudante')
plt.ylabel('Nota')
plt.title('Notas em Leitura de Código')
plt.show()
```






## Exercícios

Avance para ver os exercícios propostos.

### Exercício 1


Escreva um programa que processe o arquivo [presencas.csv](src/presencas.csv), que contém uma matriz de frequência de estudantes em um curso. Cada linha do arquivo contém um nome de estudante (anonimizado) e uma sequência de números 0 ou 1, representando ausência ou presença.

Você deverá abrir e ler o arquivo para calcular e mostrar o percentual de frequência de cada estudante, considerando todas as aulas do curso.

Exemplo de saída do programa:

``` text
estudante0: 93.3 de frequência
estudante1: 86.7 de frequência
estudante2: 0.0 de frequência
estudante3: 6.7 de frequência
estudante4: 80.0 de frequência
estudante5: 20.0 de frequência
estudante6: 33.3 de frequência
estudante7: 26.7 de frequência
estudante8: 100.0 de frequência
estudante9: 80.0 de frequência
```

Dicas:

- Guarde cada linha do CSV em uma lista, usando append, para compor uma matriz
- Processe cada linha da matriz para obter a frequência de cada estudante



### Exercício 2


Escreva um programa que crie um arquivo com o mesmo formato de [presencas.csv](src/presencas.csv), com dados gerados  pseudo-aleatoriamente para 20 estudantes e 30 aulas. O arquivo terá 20 linhas, uma para cada estudante, e 31 colunas (nome e 30 aulas).



### Exercício 3

Escreva um programa que processe o arquivo [presencas.csv](src/presencas.csv) e mostre alguma informação à sua escolha (por exemplo, estudante com maior/menor número de presenças, lista de pessoas presentes em uma determinada aula, etc). Você pode pesquisar funções de bibliotecas que ajudem a extrair o dado que você deseja.
Dica: armazene todos os dados do arquivo em uma matriz (lista de listas), pois isso facilita a manipulação.



### Exercício 4

Escreva um programa que processe o arquivo [presencas.csv](src/presencas.csv) e mostre algum gráfico à sua escolha, usando todos os dados ou somente uma parte deles.