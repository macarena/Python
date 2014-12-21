'''
Este exercício elaborará sobre modos de remover itens de uma lista. Na verdade, você tem algumas opções. Para uma lista chamada n:

n.pop(index) removerá o item em index da lista e retornará:
n = [1, 3, 5]
n.pop(1)
# Retorna 3 (o item no indice 1)
print n
# exibe [1, 5]
n.remove(item) removerá o próprio item se o encontrar:
n.remove(1)
# Remove 1 da lista,
# NAO o item no indice 1
print n
# exibe [3, 5]
del(n[1]) é como .pop no sentido em que ele irá remover o item no índice dado, mas não vai retorná-lo:
del(n[1])
# Nao retorna nada
print n
# exibe [1, 5]
'''

n = [1,3,5]
n.pop(0)

print n

'''
 A função range() do Python é apenas um atalho para gerar uma lista, 
 então você pode usar faixas em todas as mesmas situações em que usaria listas.

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
A função range tem três funções diferentes:

range(stop)
range(start, stop)
range(start, stop, step)
Em todos os casos, a função range() retorna uma lista de números a partir de start até (mas não incluindo) stop. 
Cada item é incrementado em step.

Se omitido, start terá valor padrão de zero e step terá valor padrão de um
'''

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function([0,1,2]) # Adicione sua faixa entre os parenteses!

'''
Método 1 - for item in list:

for item in list:
    print item
Método 2 - iteração através de índices:

for i in range(len(list)):
    print list[i]
O método 1 é um pouco mais fácil, mas pode causar problemas quando se tenta modificar a lista. 
O método 2 é muito mais seguro. Como não estamso modificando a lista, fique à vontade para usar qualquer um dos dois nesta lição!
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
O exemplo acima é apenas um lembrete dos dois métodos de percorrer uma lista.
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
Usar múltiplas listas em uma função não é diferente de usar múltiplos argumentos em uma função!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# exibe [1, 2, 3, 4, 5, 6]
O exemplo acima é apenas um lembrete sobre como concatenar duas listas.
'''

m = [1, 2, 3]
n = [4, 5, 6]

# Adicione seu codigo aqui!
def join_lists(x,y):
    return x + y




print join_lists(m, n)
# Voce quer que isso exiba [1, 2, 3, 4, 5, 6]
'''
UNIÃO DUAS LISTAS
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