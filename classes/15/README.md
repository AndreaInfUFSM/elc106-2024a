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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/elc106-2024a/master/classes/15/README.md)

# Aula 15


Nesta aula:


- Biblioteca `json`
- JSON e biblioteca `requests`
- CSV e biblioteca `requests`
- Biblioteca `pandas`
- Exercícios


## Biblioteca `json`


- JSON (JavaScript Object Notation) 
- Formato de intercâmbio de dados, muito usado para ler/escrever dados de/para servidores
- Independente de linguagem, facilmente utilizado nas linguages modernas (Python inclusive)
- Alternativa ao CSV, principalmente em transferências de dados que não envolvem arquivos


### Formato JSON

Combinação de 2 estruturas para formatação dos dados:

1. Conjunto de pares chave-valor que descrevem um "objeto":


``` json
    {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
    }
```

- um objeto começa com `{` (chave aberta) e termina com `}` (chave fechada)
- cada chave é seguida por `:` (dois pontos) e os pares chave/valor são separados por `,` (vírgula)


2. Lista ordenada de valores:

``` json
[
  "laranja",
  "maçã",
  "banana"
]
```

- começa com `[` (colchete aberto) e termina com `]` (colchete fechado)
- valores são separados por `,` (vírgula)



### Exemplo

Listas e objetos geralmente são combinados:

``` json
[
    {
        "id": 1,
        "nota1": 8.5,
        "nota2": 9.0
    },
    {
        "id": 2,
        "nota1": 7.8,
        "nota2": 8.2
    },
    {
        "id": 3,
        "nota1": 9.2,
        "nota2": 7.5
    }
]
```

### Em Python






``` python
registros_json = '''
[
    {
        "id": 1,
        "nota1": 7.0,
        "nota2": 8.0
    },
    {
        "id": 2,
        "nota1": 7.5,
        "nota2": 9.5
    }
]
'''
```
@Pyodide.eval


#### Carregar e processar

``` python
import json 
# Carrega os dados JSON em uma lista
lista = json.loads(registros_json)

# Para cada estudante, calcula e mostra a média
for estudante in lista:
    media = (estudante['nota1'] + estudante['nota2']) / 2
    estudante['media'] = media
    print(estudante['id'], media)

```
@Pyodide.eval

``` python
registros_json = '''
[
    {
        "id": 1,
        "nota1": 7.0,
        "nota2": 8.0
    },
    {
        "id": 2,
        "nota1": 7.5,
        "nota2": 9.5
    }
]
'''
```
@Pyodide.eval

#### Entenda

``` python
import json 
# Carrega os dados JSON em uma lista
lista = json.loads(registros_json)

# Para cada estudante, calcula e mostra a média
for estudante in lista:
    media = (estudante['nota1'] + estudante['nota2']) / 2
    estudante['media'] = media
    print(estudante['id'], media)

```
@Pyodide.eval

- Função `json.loads` recebe dados em JSON e os converte para representação em memória
- Variável `lista` designa a lista com 2 objetos contidos neste JSON

  - Por exemplo `lista[0]` vai conter o primeiro objeto

- Cada objeto é um conjunto chave-valor
- Para obter um valor, usamos uma chave (semelhante a usar um índice)

  - Por exemplo, `lista[0]['nota1']` vai conter o valor `7.0`




## JSON e biblioteca `requests` 


https://realpython.com/python-api/

![](img/Consuming-APIs-in-Python_Watermarked.718777293942.avif)


### Exemplo: API Nomes IBGE

- Obtém a frequência de nascimentos por década para o nome consultado
- Documentação: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2

Copie para o Repl.it e pequise pelo seu nome:


``` python
import requests

# Obtém a frequência de nascimentos por década para o nome consultado
# Documentação: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2
# Este programa não verifica possíveis erros de rede
name = 'seunome'
url = 'http://servicodados.ibge.gov.br/api/v2/censos/nomes/'
response = requests.get(url + name)


print(response.json())
if len(response.json()) > 0:
  data = response.json()[0]['res']
  print('Frequência de nascimentos por década para o nome:', name)
  for item in data: 
    print(item['periodo'], ":", item['frequencia'])
else:
  print('O IBGE não retornou dados para o nome:', name)
```

### Exemplo: Open-Meteo Weather API

API Open-Meteo (previsão do tempo): https://open-meteo.com/

Exemplo de requisição (temperatura do ar, 2m acima do solo): https://api.open-meteo.com/v1/forecast?latitude=-29.7&longitude=-53.8&hourly=temperature_2m


Longitude: <script default="-53.8" input="range" min="-180" max="180" output="longitude">@input</script>

Latitude: <script default="-29.7" input="range" min="-90" max="90" output="latitude">@input</script>

<script run-once="true" style="display: block">
  fetch("https://api.open-meteo.com/v1/forecast?latitude=@input(`latitude`)&longitude=@input(`longitude`)&hourly=temperature_2m")
    .then(response => response.json())
    .then(data => {
      let table = "<!-- data-show data-type='line' data-title='Open-Meteo Wheather API' -->\n"

      table += "| Time | Temperature |\n"
      table += "| ---- | ----------- |\n"

      for (let i=0; i < data.hourly.time.length; i++) {
        table += "| " + data.hourly.time[i] + " | " + data.hourly.temperature_2m[i] + " |\n"
      }
      send.lia("LIASCRIPT: "+table) }
    )
    .catch(e => {
      send.lia("ups, something went wrong")
    })
  "waiting for the weather"
</script>

Copie para o Repl.it: código para obter os dados (sem gráfico)

``` python

import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=-29.7&longitude=-53.8&hourly=temperature_2m'
response = requests.get(url)

#print(response.json())
temperaturas = response.json()['hourly']['temperature_2m']
print(temperaturas)
```


### Exemplo: API Sidra IBGE (PNAD-C)

- Serviços de dados do IBGE: https://servicodados.ibge.gov.br/api/docs/
- Exemplo: Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD-C)

  - Rendimento médio mensal nominal das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido em todos os trabalhos
  - https://apisidra.ibge.gov.br/values/t/6390/n1/all/v/5929,5933/p/all?formato=json
  - cada tabela tem um número (p.ex. 6390), obtido na documentação da API

``` python
import requests

url = 'https://apisidra.ibge.gov.br/values/t/6390/n1/all/v/5929,5933/p/all?formato=json'
response = requests.get(url)

#print(response.json())
dados = response.json()
for linha in dados:
  print(linha['D3C'], linha['V'])
```


## CSV e biblioteca `requests` 

Avance para ver exemplos...

### Exemplo: Planilha no Google Sheets

Como publicar planilha?

- File > Share > Publish to Web: escolher aba, selecionar formato CSV > Publish
- Copiar link, por exemplo: https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv


Leitura da planilha:


``` python
import requests
import csv

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Obtém conteúdo do arquivo disponibilizado na URL
response = requests.get(url)
# Transforma o conteúdo para leitura por linhas
# Conteúdo fica na memória principal (não salvo em arquivo)
content = response.content.decode("utf-8").splitlines()

# Lê o conteúdo usando a biblioteca csv
reader = csv.reader(content, delimiter=',')
## Para cada linha...
for row in reader: 
  ## Mostra elemento da primeira coluna (índice 0)
  print(row[0]) 
```


### Exemplo: Usando apenas Pandas

Usando Pandas, sem necessidade de usar as bibliotecas `requests` nem `csv`:


``` python
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Lê o conteúdo do arquivo CSV diretamente da URL usando pandas
df = pd.read_csv(url)

# Mostra elemento da primeira coluna (índice 0) de cada linha
#for value in df.iloc[:, 0]: # outra forma de selecionar a 1a coluna
for value in df['nota1']: 
    print(value)
```





### Exemplo: Download condicional 

- Não é uma boa prática fazer download a cada execução
- Se arquivo não estiver no computador, vamos obtê-lo pela rede
- Caso contrário, vamos ler do arquivo
- Biblioteca `os`:

  - acesso ao sistema operacional / sistema de arquivos
  - aqui, iremos usar para verificar se o arquivo está no computador
  - exemplos: https://www.geeksforgeeks.org/os-module-python-examples/


```python
import os
import csv
import requests

filename = "data.csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Verifica se arquivo está presente no computador
if not os.path.isfile(filename):
  print('Fazendo download...')
  response = requests.get(url)
  f = open(filename, "wb")
  f.write(response.content)
  f.close()
  print('Download concluído...')

f = open(filename, "r")
r = csv.reader(f)
for row in r:
  print(row)
f.close()  
```



### Exemplo: Usando `with`

- Forma mais avançada de lidar com arquivos
- Especifica blocos de código que precisam de uma "proteção" contra exceções
- Fecha arquivo automaticamente ao final do bloco (sem close)
- Exemplos em: https://www.geeksforgeeks.org/with-statement-in-python/

Versão com `with`:

``` python
import os
import csv
import requests

filename = "data.csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Verifica se arquivo está presente no computador
if not os.path.isfile(filename):
  print('Fazendo download...')
  response = requests.get(url)
  with open(filename, "wb") as f:
    f.write(response.content)
  print('Download concluído...')

with open(filename, "r") as f:
  r = csv.reader(f)
  for row in r:
    print(row)
```


Versão sem `with`:


``` python
import os
import csv
import requests

filename = "data.csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Verifica se arquivo está presente no computador
if not os.path.isfile(filename):
  print('Fazendo download...')
  response = requests.get(url)
  f = open(filename, "wb")
  f.write(response.content)
  f.close()
  print('Download concluído...')

f = open(filename, "r")
r = csv.reader(f)
for row in r:
  print(row)
f.close()  
```



### Exemplo: Armazenamento em lista


- Para analisar um dataset, é conveniente armazená-lo em alguma estrutura de dados (lista, etc)
- Neste exemplo, armazenamos em lista e processamos uma das colunas para obter o total de elementos que satisfazem uma condição


```python
import os
import csv
import requests

filename = "data.csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"

# Verifica se arquivo está presente no computador
if not os.path.isfile(filename):
  print('Fazendo download...')
  response = requests.get(url)
  with open(filename, "wb") as f:
    f.write(response.content)
  print('Download concluído...')

# Armazena dados em lista
data = []
with open(filename, "r") as f:
  r = csv.reader(f)
  for row in r:
    data.append(row)

# Processa lista verificando uma condição
count = 0
for row in data:
  to_count = row[1] # coluna de índice 1
  if to_count == '10':
      count += 1
  print(to_count)
print('Total:', count) 
```

### Exemplo: Equivalente com Pandas






``` python
import os
import requests
import pandas as pd

filename = "data.csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csv"


# Verifica se arquivo está presente no computador
if not os.path.isfile(filename):
  print('Fazendo download...')
  # Faz o download do arquivo e salva localmente
  df = pd.read_csv(url)
  df.to_csv(filename, index=False) 
  print('Download concluído...')


# Lê o conteúdo do arquivo CSV diretamente da URL usando pandas
df = pd.read_csv(filename)

count = (df['nota2'] == 10).sum()
print(count)
```










## Biblioteca `pandas`

- Abrevia muitas tarefas frequentes de manipulação de datasets
- Veja um resumo em: https://pt.wikipedia.org/wiki/Pandas_(software)
- O exemplo abaixo faz o mesmo que fizemos antes com `csv` e `request`, porém é bem mais curto
- Não usamos `requests` e `csv` porque `pandas` tem funções equivalentes
- Pandas torna simples tarefas complicadas, mas pode complicar tarefas simples por causa de sua sintaxe "avançada" 

```python
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSIKZs-niC-Rc7FG-qaLdaygCh9oBQxLcfuvWFFlmNUX1jTRomOVaXmZpsWuGErJ8uDvUfSozhRBdSl/pub?gid=0&single=true&output=csvv"

df = pd.read_csv(url)
total = (df['nota2'] == '10').sum()
print('Total:', total)
```




#### DataFrame

- Um recurso importante em Pandas é uma estrutura de dados chamada `DataFrame`
- Semelhante a uma matriz/tabela, com linhas e colunas rotuladas
- Muito mais sofisticado que "listas de listas"
- Veja uma explicação aqui: https://www.covildodev.com.br/artigo/criar-dataframes-pandas-python

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/creating_dataframe1.png)

Fonte: https://www.geeksforgeeks.org/creating-a-pandas-dataframe/

#### Para saber mais...

- Há muitos tutoriais e documentação online sobre **Pandas**
- Nessa disciplina não há tempo para ver mais detalhes
- Além disso, o mais importante é saber a base da linguagem, não decorar exemplos e nomes de funções

- Algumas sugestões de material de referência:

  - Python para Estatísticos, capítulo 3.3: https://tmfilho.github.io/pyestbook/math/04_pand.html
  - Pandas Tutorial W3Schools: https://www.w3schools.com/python/pandas/default.asp (resumido, em inglês)
  - Não sabe inglês? Que tal tentar mesmo assim? Nesta área, é essencial e abre muitas portas!
  - Faça uma busca e selecione materiais que fazem mais sentido para você




## Exercícios

Avance para ver os exercícios propostos.

### Exercício 1

<h4>Correlação de Pearson</h4>

O coeficiente de correlação de Pearson é uma medida de associação linear entre variáveis. Essa medida pode nos ajudar a responder muitas perguntas sobre um dado conjunto de dados. Por exemplo: se tivermos um conjunto de dados com valores de salários e de anos de experiência de pessoas em um grupo (empresa, área, etc.), podemos verificar, por exemplo, se pessoas com mais experiência tendem a ter salários mais altos.


Dados n valores medidos para 2 variáveis X e Y, o coeficiente de correlação de Pearson entre X e Y é dado pela fórmula apresentada em https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson :

![](img/602e9087d7a3c4de443b86c734d7434ae12890bc.svg)

Essa fórmula requer o cálculo da média de X e da média de Y, além de somatórios para calcular o numerador e o denominador da fórmula.

Para saber mais: https://www.datacamp.com/tutorial/tutorial-datails-on-correlation

Interpretando o resultado (conforme consta na Wikipedia):

- `0.9` a `1.0` positivo ou negativo indica uma correlação muito forte
- `0.7` a `0.9` positivo ou negativo indica uma correlação forte
- `0.5` a `0.7` positivo ou negativo indica uma correlação moderada
- `0.3` a `0.5` positivo ou negativo indica uma correlação fraca
- `0` a `0.3` positivo ou negativo indica uma correlação desprezível

<h4>Programe</h4>

- Copie o código mais abaixo para o Repl.it 
- Complete a função `pearson(x,y)`, de forma a calcular e retornar o coeficiente de correlação de Pearson para as listas de valores x e y
- Construa sua função incrementalmente, aproveitando outros exercícios com listas e repetição (média, somatório, desvio padrão...). Você pode supor que x e y tenham sempre mesmo tamanho (não é necessário verificar com condicionais). 

<h4>Teste seu código</h4>



- No final do código fornecido, há um caso de uso desse coeficiente de correlação, buscando medir a associação entre variáveis 'tempo de experiência' e 'salário'. Neste exemplo, é usada a função `pearsonr` da biblioteca scipy.stats
- Para verificar se sua função está correta, descomente a última linha de código e compare os resultados das 2 funções (a sua função `person` e a função `personr`, que está na biblioteca scopy.stats) 



``` python
# def pearson(x, y):
# COMPLETE-ME  


import scipy.stats as stats


experience = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35]

salary = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]

corr, _ = stats.pearsonr(experience, salary)
print(corr)


#print(pearson(experience, salary))
```

### Exercício 2

Na plataforma Kaggle, existem conjuntos de dados públicos usados em estudos, pesquisas e competições. Um desses datasets está descrito abaixo:

- Nome: Students Performance Dadaset
- Localização: https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset
- Descrição:  dados (anonimizados) sobre desempenho de estudantes, incluindo seus índices de desempenho e variáveis que podem (ou não) influenciá-los

<h4>Download dos dados</h4>

- Faça download do arquivo CSV disponível no Kaggle (melhor fazer isso manualmente, porque o Kaggle não disponibiliza uma simples URL para download do arquivo)
- Coloque este arquivo em um projeto no Repl.it

<h4>Programe</h4>

Faça um programa para:

- Ler o dataset do arquivo CSV (já baixado)
- Calcular e mostrar o coeficiente de correlação de Pearson entre as variáveis `Absences` (ausências) and `GPA` (índice de desempenho)
- Gerar um gráfico de `Ausências` X `GPA`



### Exercício 3

- Coloque no Google Sheets uma planilha com os dados do Exercício 1
- Publique esta planilha conforme o [Exemplo: Planilha no Google Sheets](#exemplo-planilha-no-google-sheets)
- Partindo do código do Exercício 1, modifique-o para ler os dados da planilha no Google Sheets


### Exercício 4

Escolha um dos exemplos em [JSON e biblioteca requests](#json-e-biblioteca-requests) e complemente o programa com um gráfico e/ou alguma análise dos dados obtidos (pode ser algo simples, como uma contagem ou média, ou uma análise mais elaborada, conforme seu interesse).