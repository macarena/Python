'''
O la�o "while" � similar a uma declara��o "if": ela executa o c�digo no seu interior se certa condi��o for verdadeira. 
A diferen�a � que o la�o "while"continuar� a ser executado enquanto a condi��o for verdadeira.
Em outras palavras, em vez de ser executado se (if) uma condi��o for verdadeira, 
o c�digo ser� executado enquanto (while) a condi��o for verdadeira.

A linha 6 decide quando o la�o ser� executado. Ent�o, "enquanto 'count' for menor do que 5" o la�o continuar� a ser executado. 
A linha 8 aumenta "count" em 1. Isso acontece repetidamente at� que "count" seja igual a "5".
'''
count = 0

if count < 5:
    print "Ola, sou uma declaracao if e a contagem e", count
    
while count <= 9:
    print "Ola, sou um while e a contagem e", count
    count += 1

'''
A condi��o � a express�o que decide se o la�o ser� executado ou n�o. H� 5 etapas nesse programa:

A vari�vel loop_condition � igualada a True

O la�o while verifica para ver se loop_condition � True. Ela �, ent�o o programa entra no la�o.

A declara��o print � executada.

A vari�vel loop_condition � igualada a False.

O la�o while verifica novament se loop_condition � True. Ela n�o �, por isso o la�o n�o e executado novamente.
'''
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

'''
Dentro de um la�o while voc� pode fazer qualquer coisa que poderia fazer em outro lugar, incluindo opera��es aritm�ticas.
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
Uma aplica��o comum do la�o while � verificar se o que o usu�rio inseriu � v�lido. 
Por exemplo, se voc� pedir ao usu�rio para inserir y ou n e em vez disso ele digita um 7, 
ent�o voc� deve pedir que ele insira outra entrada.
'''

choice = raw_input('Gostando do curso? (y/n)')

while choice != 'y' and choice != 'n':  # Preencha a condicao (antes dos dois pontos)
    choice = raw_input("Desculpe, nao entendi. Digite novamente: ")

'''
Um la�o infinito � uma la�o que nunca termina. Isso pode acontecer por algumas raz�es:

A condi��o do la�o n�o pode ser falsa (por exemplo, while 1 != 2)

A l�gica do la�o impede que a condi��o do la�o se torne falsa.

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
break � uma declara��o de uma linha que significa "saia do la�o atual". 
Um modo alternativo de sair do la�o em execu��o � com a declara��o break.

Primeiro, crie um while com uma condi��o que seja sempre verdade. O modo mais simples � mostrado.

Usando uma declara��o if, voc� define a condi��o de interrup��o. Dentro do if, voc� escreve break, o que quer dizer "saia do la�o".

A diferen�a aqui � que esse la�o certamente vai ser executado pelo menos uma vez.
'''
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

'''
Algo completamente diferente sobre o Python � a constru��o while/else. 
while/else � similar a if/else, 
mas h� uma diferen�a: o bloco else ser� executado sempre que a condi��o do la�o for considerada False. 
Isso significa que ele ser� executado se o c�digo nunca entrar no la�o ou se oo la�o for encerrado normalmente. 
Se o la�o for interrompido como o resultado de break, a condi��o else n�o ser� executada.

Neste exemplo, o la�o ser� interrompido (break) se um 5 for gerado, e o else n�o ser� executado. 
Caso contr�rio, depois que 3 n�meros forem gerados, a condi��o do la�o se tornar� falsa e o else ser� executado.
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
Agora voc� deve ser capaz de criar um jogo similar �quele do �ltimo exerc�cio. O c�digo do �ltimo exerc�cio � mostrado abaixo:

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
Neste exerc�cio, permita ao usu�rio tentar descobrir qual � o n�mero tr�s vezes.

guess = int(raw_input("Seu palpite: "))
Lembre-se, raw_input converte a entrada do usu�rio em uma string, ent�o temos que usar int() para converte-la de volta em um n�mero.
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

