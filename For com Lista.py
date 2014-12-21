'''
Se voc� quiser fazer algo com todos os itens na lista, pode usar um la�o for. 
Se voc� j� tiver aprendido sobre la�os for em JavaScript, preste aten��o! Eles s�o diferentes em Python.

for variable in list_name:
    # Fa�a alguma coisa!
Um nome de vari�vel se segue � palavra-chave for; ela receber� o valor de cada lista um por vez.

Ent�o, in list_name designa list_name como a lista sobre a qual o la�o vai atuar. 
A linha termina com dois pontos (:) e o c�digo recuado que se segue ser� executado uma vez por item da lista.
'''
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Seu codigo aqui
    print number
    print 2 * number
	
'''
Se sua lista estiver uma bagun�a, voc� pode precisar organiz�-la (sort()).

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal
Primeiro, criamos uma lista chamada animals co mtr�s strings. As strings n�o est�o em ordem alfab�tica.
Ent�o, colocamos animals em ordem alfab�tica. Note que .sort() modifica a lista em vez de retornar uma nova lista.
Ent�o, exibimos cada item em animals, como "ant", "bat", "cat", cada um em uma linha.
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
Um modo alternativo de criar um la�o � o la�o for.
A sintaxe � a seguinte; este exemplo significa que "para cada n�mero i na faixa 0 - 9, exiba i".
'''
print "Contando..."

for i in range(20):
    print i
    
'''
Esse tipo de la�o � �til quando voc� quiser fazer algo certo n�mero de vezes, assim como adicionar algo ao final de uma lista.
'''
hobbies = []

# Adicione seu codigo abaixo!
for i in range(3):
    hobbie = raw_input("Digite o seu Hobbie: ")
    hobbies.append(hobbie)
print hobbies
'''
Usando um la�o for, voc� pode exibir cada caractere individual em uma string.

TO exemplo no editor est� praticamente em portugu�s claro: "para cada caractere c em thing, exiba c".
'''
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Seu codigo vem aqui!
for o in word:
    print o
'''
A manipula��o de strings � �til em la�os for se voc� quiser modificar algum conte�do dentro da string.

word = "Marble"
for char in word:
    print char,
O exemplo acima percorre cada caractere em word e, no final, exibe M a r b l e.

O caracter , depois da declara��o print significa que nossa pr�xima declara��o print continua exibindo o texto na mesma linha.
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
Talvez o mais �til (e mais comum) uso dos la�os for � percorrer uma lista.

A cada itera��o, a vari�vel num ser� o pr�ximo valor da lista. 
Ent�o, da primeira vez, ele ser� 7, da segunda vez, ser� 9, ent�o 12, 54, 99, 
e ent�o o la�o ser� interrompido quando n�o houver mais valores na lista.
'''

numbers  = [7, 9, 12, 54, 99]

print "Esta lista contem: "

for num in numbers:
    print num

# Adicione seu laco abaixo!
for square in numbers:
    print square ** 2
	
'''
Voc� pode estar imaginando como funciona percorrer um dicion�rio. Voc� deveria obter a chave ou o valor?

A resposta curta �: voc� obt�m a chave, que pode usar para obter o valor.

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    if d[key] == 10
        print "Este dicion�rio tem o valor 10!"
Primeiro, criamos um dicion�rio com strings como chaves e n�meros como valores.
Ent�o, percorremos o dicion�rio, armazenando a cada vez a chave em key.
A seguir, verificamos se o valor da chave � igual a 10.
Finalmente, exibimos Este dicionario tem o valor 10!
'''
d = {'a': 'maca', 'b': 'amora', 'c': 'cereja'}

for key in d:
    # Seu codigo vem aqui!
    print key,d[key]
'''
Uma desvantagem de usar este estilo de itera��o for-cada � que voc� n�o sabe o �ndice do que est� examinando. 
Geralmente, isso n�o � um problema, mas �s vezes � �til saber em que ponto da lista voc� est�. 
Felizmente, a fun��o embutida enumerate nos ajuda com isso.

enumerate funciona fornecendo um �ndice correspondente a cada elemento na lista que voc� est� percorrendo. 
Sempre que voc� passa pelo la�o, index se� incrementado um um, e item ser� o pr�ximo item na sequ�ncia. 
� muito similar a usar um la�o for normal com uma lista, 
exceto que isso nos d� um modo f�cil de contar quantos itens vimos at� agora.
'''
choices = ['pizza', 'massa', 'salada', 'nachos']

print 'Suas opcoes sao:'
for index, item in enumerate(choices):
    index += 1
    print index, item

'''
Tamb�m � comum precisar percorrer duas listas ao mesmo tempo. � qui que a fun��o embutida zip se torna �til.

zip criar� pares de elementos quando s�o usadas duas listas, e param no fim da lista mais curta.

zip tamb�m pode tratar tr�s ou mais listas!
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
Assim com while, la�os for podem ter um else associado a eles.

Nesse caso, a declara��o else � executado depois do for, 
mas apenas se o for terminar normalmente � ou seja, n�o com um break. 
Esse c�digo ser� interrompido (break) quando atingir 'tomate', ent�o o bloco else n�o ser� executado.
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
        
