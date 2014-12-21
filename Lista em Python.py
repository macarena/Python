'''
	LISTA!
'''
zoo_animals = ["pangolin", "cassowary", "sloth", "White Dragon"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "O primeiro animal do zoo e " + zoo_animals[0]
	print "O segundo animal do zoo e " + zoo_animals[1]
	print "O terceiro animal do zoo e " + zoo_animals[2]
	print "O quarto animal do zoo e " + zoo_animals[3]

'''	
Voc� pode acessar um item individual na lista pelo seu �ndice.
Um �ndice � como um endere�o que identifica a posi��o do item na lista. 
O �ndice aparece diretamente depois do nome da lista, entre colchetes, assim: list_name[index].

Os �ndices de lista come�am em 0, n�o 1! 
voc� acessa o primeiro item de uma lista dessa forma: list_name[0]. 
O segundo item em uma lista est� no �ndice 1: list_name[1]. 
Os cientistas da computa��o adoram contar a partir do zero.
'''
numbers = [5, 6, 7, 8]

print "Somando os numeros nos indices 0 e 2..."
print numbers[0] + numbers[2]
print "Somando os numeros nos indices 1 e 3..."
# Seu codigo vem aqui!
print numbers[1] + numbers[3]

'''
Um �ndice de lista se comporta como qualquer outro nome de vari�vel! Ele pode ser usado para acessar e atribuir valores.

Voc� viu como acessar um �ndice de lista assim:

zoo_animals[0]
# Recebe o valor "pangolin"
Voc� pode como funcionam as atribui��es na linha 5:

zoo_animals[2] = "hiena"
# Muda "preguica" to "hiena"
'''

zoo_animals = ["pangolin", "casuar", "preguica", "tigre"]
# Noite passada a preguica do zoologico atacou brutalmente 
# o pobre tigre e o devorou inteiro.

# A feroz preguica foi substituida por uma amigavel hiena.
zoo_animals[2] = "hiena"

# Que animal deveria preencher o vazio deixado pelo pobre tigre falecido?
# Seu codigo aqui!
zoo_animals[3] = "Goblin"

'''
Uma lista n�o precisa ter um comprimento fixo. Voc� pode adicionar itens ao fim e uma lista sempre que quiser!

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters
No exemplo acima, primeiro criamos uma lista chamada letters.
Ent�o, adicionamos a string 'd' ao fim da lista letters.
Depois, exibimos 4, o comprimento da lista letters.
Finalmente, exibimos ['a', 'b', 'c', 'd'].
'''

#lista.APPEND adiciona no final da lista um item

suitcase = [] #Lista sem limite e sem item adicionado
suitcase.append("oculos escuros")

# Seu codigo aqui!
suitcase.append("Sabe o que um Knight pode fazer contigo?")
suitcase.append("Qual classe voce gostaria de ser? Druid, Sorcerer, Knight ou Paladin?")
suitcase.append("Boa escolha, jovem aventureiro")



list_length = len(suitcase) # Iguale ao comprimento da valise

print "Ha %d itens na valise." % (list_length)
print suitcase

suitcase = ["oculos escuros", "chapeu", "passaporte", "laptop", "camisa", "sapatos"]

first  = suitcase[0:2]  # O primeiro e segundo itens (indices zero e um)
middle = suitcase[2:4]  # Terceiro e quarto itens (indices dois e tres)
last   = suitcase[4:6]  # Os ultimos dois itens (indices quatro e cinco)
#suitcase[4:6] quer dizer que ele imprime o valor suitcase[4] e suitcase[5]
#quando chega no 6 ele n�o imprime
print first
print middle
print last

animals = "catdogfrog"
cat  = animals[:3]   # Os tres primeiros caracteres de animals
dog  = animals[3:6]  # O quarto ate sexto caracteres
frog = animals[6:]   # A partir do setimo caractere ate o final
print cat
print dog 
print frog

'''
�s vezes voc� precisar procurar por um item em uma lista.

animals = ["ant", "bat", "cat"]
print animals.index("bat")
Primeiro, criamos uma lista chamada animals com tr�s strings.
Ent�o, exibimos o primeiro �ndice que cont�m a string "bat", o que exibir� 1.
Tamb�m podemos inserir itens em uma lista.

animals.insert(1, "dog")
print animals
Inserimos "dog" no �ndice 1, que move tudo 1 unidade.
Exibimos ["ant", "dog", "bat", "cat"]
'''
animals = ["tatu", "texugo", "pato", "emu", "raposa"]
duck_index = animals.index("pato") # Use index() para encontrar "pato"

# Seu codigo aqui!
animals.insert(duck_index, "cobra")


print animals # Observe o que e exibido depois da operacao de insercao

'''
�s vezes voc� precisa remover algo de uma lista.

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
>> ["john","paul","george","ringo"]
Criamos uma lista chamada beatles com 5 strings.
Ent�o, removemos o primeiro item de beatles que corresponda a string "stuart". Note que .remove(item) nao retorna nada.
Finalmente, exibimos a lista para confirmar que "stuart" foi realmente removido.
'''

backpack = ['xilofone', 'adaga', 'tenda', 'pedaco de pao']

backpack.remove('adaga')
print backpack


names = ["Adam","Alex","Mariah","Martine","Columbus"]
for item in names:
    item.lower()
    first = item[0]
    if first == "A":
        print names
    else:
        print "Palavra nao inicia com A, inicia com: " + first

'''
Os blocos de c�digo em um la�o for podem ser t�o grandes ou pequenos quanto necess�rio.

Durante o la�o, voc� pode querer realizar diferentes a��es, dependendo do item em particular na lista.

numbers = [1, 3, 4, 7]
for number in numbers: 
    if number > 6:
        print number
print "We printed 7."
No exemplo acima, criamos uma lista com 4 n�meros.
Ent�o, percorremos a lista numbers e armazenamos cada item da lista na vari�vel number.
Em cada la�o, se number for maior do que 6, n�s o exibimos (print). Ent�o, exibimos 7.
Finalmente, exibimos uma senten�a.
Tenha certeza de de manter o controle sobre seus recuos, ou pode ficar confuso!
'''

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for key in a:
    if key%2  == 0:
        print key
print "Imprimimos somente os numeros pares"

'''
Fun��es tamb�m podem tomar listas como entradas e realizar diversas opera��es nessas listas.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small
No exemplo acima, definimos uma fun��o count_small que tem um argumento, numbers.
Inicializamos uma vari�vel total que podemos usar no la�o for.
Para cada item n em numbers, se n for menor do que 10, incrementamos total.
Depois do la�o for, retornamos total.
Depois da defini��o da fun��o, criamos um array de n�meros chamado lost.
Chamamos a fun��o count_small, inserimos lost, e armazenamos o resultado em small.
Finalmente, exibimos o resultado, que � 2, j� que apenas 4 e 8 s�o menores do que 10.
'''
# Escreva sua funcao abaixo!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count
fizz_count(["fizz", "cat", "fizz"])


for letter in "Codecademy":
    print letter
    
# Linhas em branco deixam a saida bonita
print
print

word = "E divertido programar!"

for letter in word:
    # Exiba apenas a letra i
    if letter == "i":
        print letter