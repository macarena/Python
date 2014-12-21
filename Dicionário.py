'''
Um dicion�rio � similar a uma lista, mas voc� acessa valores procurando uma chave em vez de um �ndice. 
Uma chave pode ser qualquer string ou n�mero. Dicion�rios s�o contidos entre chaves, assim:

d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
Este � um dicion�rio chamado d com tr�s ** pares chave-valor**. 
A chave 'key1' aponta para o valor 1, 'key2' para 2, e assim por diante.

Dicion�rios s�o �timos para coisas como listas telef�nicas (combinando um nome a um n�mero de telefone), 
p�ginas de acesso de websites (combinando um endere�o de e-mail com um nome de usu�rio), e mais!
'''
# Atribuir um dicionario com tres pares chave-valor para residentes:
residents = {'Fradinho' : 104, 'Preguica' : 105, 'Piton de Burma' : 106}

print residents['Fradinho'] # Exibe o numero do quarto do fradinho

# Seu codigo aqui!
print residents['Preguica']
print residents['Piton de Burma']

'''
Como as listas, os dicion�rios s�o "mut�veis". 
Isso significa que eles podem ser modificados depois de serem criados. 
Uma vantagem disso � que podemos adicionar novos pares chave/valor ao dicion�rio depois que ele � criado, assim:

dict_name[new_key] = new_value
Um par vazio de chaves {} � um dicion�rio vazio, assim como um par vazio de [] � uma lista vazia.

O comprimento len() de um dicion�rio � o n�mero de pares chave-valor que ele tem. 
Cada par � contado apenas uma vez, mesmo se o valor for uma lista (Isso mesmo: voc� pode colocar listas dentro de dicion�rios!).
'''

menu = {} # Empty dictionary
menu['Frango Alfredo'] = 14.50 # Adicionando um novo par chave-valor
print menu['Frango Alfredo']

# Seu codigo aqui: Adicione alguns pares prato-preco a menu!
menu['Frango da Vovo'] = 20.40
menu['Black Widows baby'] = 11.50
menu['Festa no sabado'] = 20


print "Ha " + str(len(menu)) + " itens no cardapio."
print menu

'''
como os dicion�rios s�o mut�veis, eles podem ser mudados de muitas formas. 
Itens podem ser removidos de um dicion�rio com o comando del:

del dict_name[key_name]
remover� a chave key_name e o valor associado do dicion�rio.

Um novo valor pode ser associado a uma chave atribuindo-se um valor � chave, assim:

dict_name[key] = new_value
'''

# key - animal_name : value - location 
zoo_animals = { 'Unicornio' : 'Casa de Algodao Doce',
'Preguica' : 'Exibicao da Floresta Tropical',
'Tigre de Bengala' : 'Casa da Selva',
'Fradinho do Atlantico' : 'Exibicao Artica',
'Pinguim Saltador da Rocha' : 'Exibicao Artica'}
# Uma declaracao de dicionario (ou lista) pode ocupar mais de uma linha

# Removendo a entrada 'Unicornio'( Unicornios sao incrivelmente caros).
del zoo_animals['Unicornio']

# Seu codigo aqui!
del zoo_animals['Preguica']
del zoo_animals['Tigre de Bengala']
zoo_animals['Pinguim Saltador da Rocha'] = 'Casa de Algodao Doce'


print zoo_animals

'''
Vamos repassar algumas observa��es sobre dicion�rios

my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]
No exemplo acima, criamos um dicion�rio que cont�m muitos tipos de valores.
A chave 'fish" tem uma lista, a chave "cash" contem um int, e a chave "luck" contem uma string.
Finalmente, exibimos a letra 'c'. Quando acessamos um valor no dicion�rio, como my_dict["fish"].
Temos acesso direto a esse valor. Ent�o podemos acessor o item no �ndice '0' da lista armazenado sob a chave "fish"
'''

inventory = {
    'gold' : 500,
    'pouch' : ['silex', 'barbante', 'pedra preciosa'], # Atribuido uma nova lista a chave 'pouch'
    'backpack' : ['xilofone','adaga', 'saco de dormir','pedaco de pao']
    
}

# Adicionando uma chave 'burlap bag' a atribuindo uma lista a ela
inventory['burlap bag'] = ['maca', 'pequeno rubi', 'bicho preguica']

# Organizando a lista encontrada sob a chave 'pouch'
inventory['pouch'].sort() 


# Seu codigo aqui
inventory['pocket'] =  ['concha', 'amora estranha', 'sujeira']
inventory['backpack'].sort()
inventory['backpack'].remove('adaga')
inventory['gold'] += 50
print inventory

'''
Voc� tamb�m pode usar um la�o for em um dicion�rio para percorrer suas chaves, assim:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar" 
Note que os dicion�rios s�o desordenados, 
o que significa que sempre que voc� percorre um la�o, 
voc� passar� por todas as chaves, mas voc� n�o tem garantias de obt�-las em nenhuma ordem em particular.
'''

webster = {
	"Tatu" : "O astro de um popular desenho animado.",
    "Bee" : "O som que uma cabra faz.",
    "Tapete": "Fica no chao.",
    "Pouco": "Uma quantia pequena."
}

# Adicione seu codigo abaixo!
for key in webster:
    print webster[key]
	
