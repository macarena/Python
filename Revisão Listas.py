'''
Este exerc�cio elaborar� sobre modos de remover itens de uma lista. Na verdade, voc� tem algumas op��es. Para uma lista chamada n:

n.pop(index) remover� o item em index da lista e retornar�:
n = [1, 3, 5]
n.pop(1)
# Retorna 3 (o item no indice 1)
print n
# exibe [1, 5]
n.remove(item) remover� o pr�prio item se o encontrar:
n.remove(1)
# Remove 1 da lista,
# NAO o item no indice 1
print n
# exibe [3, 5]
del(n[1]) � como .pop no sentido em que ele ir� remover o item no �ndice dado, mas n�o vai retorn�-lo:
del(n[1])
# Nao retorna nada
print n
# exibe [1, 5]
'''

n = [1,3,5]
n.pop(0)

print n

'''
 A fun��o range() do Python � apenas um atalho para gerar uma lista, 
 ent�o voc� pode usar faixas em todas as mesmas situa��es em que usaria listas.

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
A fun��o range tem tr�s fun��es diferentes:

range(stop)
range(start, stop)
range(start, stop, step)
Em todos os casos, a fun��o range() retorna uma lista de n�meros a partir de start at� (mas n�o incluindo) stop. 
Cada item � incrementado em step.

Se omitido, start ter� valor padr�o de zero e step ter� valor padr�o de um
'''

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function([0,1,2]) # Adicione sua faixa entre os parenteses!

'''
M�todo 1 - for item in list:

for item in list:
    print item
M�todo 2 - itera��o atrav�s de �ndices:

for i in range(len(list)):
    print list[i]
O m�todo 1 � um pouco mais f�cil, mas pode causar problemas quando se tenta modificar a lista. 
O m�todo 2 � muito mais seguro. Como n�o estamso modificando a lista, fique � vontade para usar qualquer um dos dois nesta li��o!
'''

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(0,len(numbers)):
        result = result + numbers[i]
    return result
print total(n)

'''
Agora vamos tentar trabalhar com strings!

for item in list:
    print item

for i in range(len(list)):
    print list[i]
O exemplo acima � apenas um lembrete dos dois m�todos de percorrer uma lista.
'''
n = ["Michael", "Lieberman"]
# Adicione sua funcao aqui
def join_strings(words):
    result = ""
    for i in range(len(words)):
        result = result + words[i]
    return result

print join_strings(n)

'''
Usar m�ltiplas listas em uma fun��o n�o � diferente de usar m�ltiplos argumentos em uma fun��o!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# exibe [1, 2, 3, 4, 5, 6]
O exemplo acima � apenas um lembrete sobre como concatenar duas listas.
'''

m = [1, 2, 3]
n = [4, 5, 6]

# Adicione seu codigo aqui!
def join_lists(x,y):
    return x + y




print join_lists(m, n)
# Voce quer que isso exiba [1, 2, 3, 4, 5, 6]
'''
UNI�O DUAS LISTAS
'''
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Adicione sua funcao aqui
def flatten(lists):
    results = []
    for i in range(len(lists)):
        for numbers in range(len(lists[i])):
            results.append(numbers)
    return results



print flatten(n)