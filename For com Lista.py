'''
Se você quiser fazer algo com todos os itens na lista, pode usar um laço for. 
Se você já tiver aprendido sobre laços for em JavaScript, preste atenção! Eles são diferentes em Python.

for variable in list_name:
    # Faça alguma coisa!
Um nome de variável se segue à palavra-chave for; ela receberá o valor de cada lista um por vez.

Então, in list_name designa list_name como a lista sobre a qual o laço vai atuar. 
A linha termina com dois pontos (:) e o código recuado que se segue será executado uma vez por item da lista.
'''
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Seu codigo aqui
    print number
    print 2 * number
	
'''
Se sua lista estiver uma bagunça, você pode precisar organizá-la (sort()).

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal
Primeiro, criamos uma lista chamada animals co mtrês strings. As strings não estão em ordem alfabética.
Então, colocamos animals em ordem alfabética. Note que .sort() modifica a lista em vez de retornar uma nova lista.
Então, exibimos cada item em animals, como "ant", "bat", "cat", cada um em uma linha.
'''

start_list = [5, 3, 1, 2, 4]
square_list = []

# Seu codigo aqui!
for square in start_list:
    power = square ** 2
    square_list.append(power)
square_list.sort()
print square_list

'''
Um modo alternativo de criar um laço é o laço for.
A sintaxe é a seguinte; este exemplo significa que "para cada número i na faixa 0 - 9, exiba i".
'''
print "Contando..."

for i in range(20):
    print i
    
'''
Esse tipo de laço é útil quando você quiser fazer algo certo número de vezes, assim como adicionar algo ao final de uma lista.
'''
hobbies = []

# Adicione seu codigo abaixo!
for i in range(3):
    hobbie = raw_input("Digite o seu Hobbie: ")
    hobbies.append(hobbie)
print hobbies
'''
Usando um laço for, você pode exibir cada caractere individual em uma string.

TO exemplo no editor está praticamente em português claro: "para cada caractere c em thing, exiba c".
'''
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Seu codigo vem aqui!
for o in word:
    print o
'''
A manipulação de strings é útil em laços for se você quiser modificar algum conteúdo dentro da string.

word = "Marble"
for char in word:
    print char,
O exemplo acima percorre cada caractere em word e, no final, exibe M a r b l e.

O caracter , depois da declaração print significa que nossa próxima declaração print continua exibindo o texto na mesma linha.
'''
phrase = "Um passaro na mao..."

# Adicione seu laco for
for char in phrase:
    if (char == 'a') or (char == 'A'):
        print 'X',
    else:
        print char,




#Nao delete esta declaracao print!
print

'''
Talvez o mais útil (e mais comum) uso dos laços for é percorrer uma lista.

A cada iteração, a variável num será o próximo valor da lista. 
Então, da primeira vez, ele será 7, da segunda vez, será 9, então 12, 54, 99, 
e então o laço será interrompido quando não houver mais valores na lista.
'''

numbers  = [7, 9, 12, 54, 99]

print "Esta lista contem: "

for num in numbers:
    print num

# Adicione seu laco abaixo!
for square in numbers:
    print square ** 2
	
'''
Você pode estar imaginando como funciona percorrer um dicionário. Você deveria obter a chave ou o valor?

A resposta curta é: você obtém a chave, que pode usar para obter o valor.

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    if d[key] == 10
        print "Este dicionário tem o valor 10!"
Primeiro, criamos um dicionário com strings como chaves e números como valores.
Então, percorremos o dicionário, armazenando a cada vez a chave em key.
A seguir, verificamos se o valor da chave é igual a 10.
Finalmente, exibimos Este dicionario tem o valor 10!
'''
d = {'a': 'maca', 'b': 'amora', 'c': 'cereja'}

for key in d:
    # Seu codigo vem aqui!
    print key,d[key]
'''
Uma desvantagem de usar este estilo de iteração for-cada é que você não sabe o índice do que está examinando. 
Geralmente, isso não é um problema, mas às vezes é útil saber em que ponto da lista você está. 
Felizmente, a função embutida enumerate nos ajuda com isso.

enumerate funciona fornecendo um índice correspondente a cada elemento na lista que você está percorrendo. 
Sempre que você passa pelo laço, index seá incrementado um um, e item será o próximo item na sequência. 
É muito similar a usar um laço for normal com uma lista, 
exceto que isso nos dá um modo fácil de contar quantos itens vimos até agora.
'''
choices = ['pizza', 'massa', 'salada', 'nachos']

print 'Suas opcoes sao:'
for index, item in enumerate(choices):
    index += 1
    print index, item

'''
Também é comum precisar percorrer duas listas ao mesmo tempo. É qui que a função embutida zip se torna útil.

zip criará pares de elementos quando são usadas duas listas, e param no fim da lista mais curta.

zip também pode tratar três ou mais listas!
'''
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Adicione seu codigo aqui!
    if a > b:
        print a
    else: 
        print b
'''
Assim com while, laços for podem ter um else associado a eles.

Nesse caso, a declaração else é executado depois do for, 
mas apenas se o for terminar normalmente — ou seja, não com um break. 
Esse código será interrompido (break) quando atingir 'tomate', então o bloco else não será executado.
'''

fruits = ['banana', 'maca', 'laranja', 'tomate', 'pera', 'uva']

print 'Voce tem...'
for f in fruits:
    if f == 'tomate':
        print 'O tomate nao e uma fruta!' # (Na verdade, e sim.)
        break
    print 'A', f
else:
    print 'Uma excelente selecao de frutas!'
	
classes = ["Knight", "Paladin", "Druid", "Sorcerer"]
for i in classes:
    print i
else:
    op = raw_input("Escolha uma classe: ")
    if(op.lower() == "knight"):
       print "Boa escolha Campeao"
    elif (op.lower() == "paladin"):
        print "Entao voce gosta de ataques a longa distancia?"
    elif(op.lower() == "druid"):
        print "Voce pertecne a natureza"
    elif(op.lower() == "sorcerer"):
        print "Aproveite seus poderes de destruicao"
    else:
        print "Classe invalida"
        
