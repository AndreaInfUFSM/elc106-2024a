print('********** Questão 1 **********')


# Escreva um programa que mostre na tela todos os anos da década de 90, um por linha. 
# Para isso, use uma variável para representar o ano, inicialize-a com o primeiro ano da década 
# e use `while` para mostrar o ano e incrementar a variável. 
# Atenção: qual a condição que deverá ser satisfeita a cada repetição?

ano = 1990
while ano < 2000:
  print(ano)
  ano = ano + 1

# Qual a condição que deverá ser satisfeita a cada repetição?
# Resposta: como o ano está sendo incrementado, a condição é que esteja dentro da década,
# ou seja, seja menor que o início da próxima década (ano < 2000)
# Outra alternativa seria a condição: ano <= 1999

print('********** Questão 2 **********')

# Uma pizzaria oferece desconto para o "sabor do dia", que é definido por sorteio 
# a partir de uma lista de sabores. 
# Escreva um programa que sorteie 7 vezes um sabor qualquer da lista (um para cada dia da semana) 
# e mostre na tela uma saída no formato exemplificado abaixo.

#    Exemplo de saída:

#    ```
#    Dia 1 : Bacon
#    Dia 2 : Calabresa
#    Dia 3 : Marguerita
#    Dia 4 : Calabresa
#    Dia 5 : Bacon
#    Dia 6 : Marguerita
#    Dia 7 : Calabresa
#    ```

#    Observações:

#    - Você deve usar while
#    - Lembre da função choice, que sorteia um elemento de uma lista

from random import choice

sabores = ['Calabresa', 'Bacon', 'Vegetariana', 'Marguerita']

i = 0
while i < 7:
  escolha = choice(sabores)
  print('Dia', i+1, ':', escolha)
  i = i + 1

