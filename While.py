'''
O laço "while" é similar a uma declaração "if": ela executa o código no seu interior se certa condição for verdadeira. 
A diferença é que o laço "while"continuará a ser executado enquanto a condição for verdadeira.
Em outras palavras, em vez de ser executado se (if) uma condição for verdadeira, 
o código será executado enquanto (while) a condição for verdadeira.

A linha 6 decide quando o laço será executado. Então, "enquanto 'count' for menor do que 5" o laço continuará a ser executado. 
A linha 8 aumenta "count" em 1. Isso acontece repetidamente até que "count" seja igual a "5".
'''
count = 0

if count < 5:
    print "Ola, sou uma declaracao if e a contagem e", count
    
while count <= 9:
    print "Ola, sou um while e a contagem e", count
    count += 1

'''
A condição é a expressão que decide se o laço será executado ou não. Há 5 etapas nesse programa:

A variável loop_condition é igualada a True

O laço while verifica para ver se loop_condition é True. Ela é, então o programa entra no laço.

A declaração print é executada.

A variável loop_condition é igualada a False.

O laço while verifica novament se loop_condition é True. Ela não é, por isso o laço não e executado novamente.
'''
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

'''
Dentro de um laço while você pode fazer qualquer coisa que poderia fazer em outro lugar, incluindo operações aritméticas.
'''

num = 1

while num <= 10:  # Preencha com a condicao
    # Exiba o numero ao quadrado
    # Incremente o numero (tenha certeza de ter feito isso!)
    aux = num
    num = num ** 2
    print num
    num = aux
    print num
    num += 1

'''
Uma aplicação comum do laço while é verificar se o que o usuário inseriu é válido. 
Por exemplo, se você pedir ao usuário para inserir y ou n e em vez disso ele digita um 7, 
então você deve pedir que ele insira outra entrada.
'''

choice = raw_input('Gostando do curso? (y/n)')

while choice != 'y' and choice != 'n':  # Preencha a condicao (antes dos dois pontos)
    choice = raw_input("Desculpe, nao entendi. Digite novamente: ")

'''
Um laço infinito é uma laço que nunca termina. Isso pode acontecer por algumas razões:

A condição do laço não pode ser falsa (por exemplo, while 1 != 2)

A lógica do laço impede que a condição do laço se torne falsa.

Exemplo:

count = 10
while count > 0:
    count += 1 # instead of count -= 1
'''
count = 0

while count < 10 :# adicione dois pontos
    print count
    # Contagem de incrementos
    count += 1
    
	
'''
break é uma declaração de uma linha que significa "saia do laço atual". 
Um modo alternativo de sair do laço em execução é com a declaração break.

Primeiro, crie um while com uma condição que seja sempre verdade. O modo mais simples é mostrado.

Usando uma declaração if, você define a condição de interrupção. Dentro do if, você escreve break, o que quer dizer "saia do laço".

A diferença aqui é que esse laço certamente vai ser executado pelo menos uma vez.
'''
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

'''
Algo completamente diferente sobre o Python é a construção while/else. 
while/else é similar a if/else, 
mas há uma diferença: o bloco else será executado sempre que a condição do laço for considerada False. 
Isso significa que ele será executado se o código nunca entrar no laço ou se oo laço for encerrado normalmente. 
Se o laço for interrompido como o resultado de break, a condição else não será executada.

Neste exemplo, o laço será interrompido (break) se um 5 for gerado, e o else não será executado. 
Caso contrário, depois que 3 números forem gerados, a condição do laço se tornará falsa e o else será executado.
'''

import random

print "Numeros da Sorte! Serao gerados 3 numeros."
print "Se um deles for um '5', voce perde!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Lamento, voce perdeu!"
        break
    count += 1
else:
    print "Voce ganhou!"

'''
Agora você deve ser capaz de criar um jogo similar àquele do último exercício. O código do último exercício é mostrado abaixo:

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Lamento, voce perdeu!"
        break
    count += 1
else:
    print "Voce venceu!"
Neste exercício, permita ao usuário tentar descobrir qual é o número três vezes.

guess = int(raw_input("Seu palpite: "))
Lembre-se, raw_input converte a entrada do usuário em uma string, então temos que usar int() para converte-la de volta em um número.
'''
from random import randint

# Gera um numero de 1 a 10, inclusive
random_number = randint(1, 10)
print random_number
guesses_left = 3
# Comece seu jogo!
while guesses_left > 0:
    guess = int(raw_input("Seu palpite: "))
    if guess == random_number:
        print "Voce venceu!"
        break
    guesses_left -= 1
else:
    print "Voce perdeu"

