def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Iguale maximum ao valor maximo de qualquer conjunto de numeros na linha 3!

maximum = max(0,100,200,-100)

print maximum

'''
A função max() toma qualquer número de argumentos e retorna o maior deles. 
("Maior" pode ter definições estranhas, então é melhor usar max() em números inteiros e de ponto flutuante, 
onde os resultados são simples, não em outros objetos, como strings.)

Por exemplo, max(1,2,3) retornará 3 (o maior número no conjunto de argumentos).
min() retorna então o menor de uma dada série de argumentos.
'''
# Iguale minimum ao menor valor de qualquer conjunto de numeros na linha 3!

minimum = min(1,8,0,-239)

print minimum

'''
A função abs() retorna o módulo do número que toma como argumento — ou seja, 
a distância entre esse número e 0 em uma reta numérica imaginária. Por exemplo, 3 e -3 têm o mesmo módulo: 3. 
A função abs() sempre retorna um valor positivo, ao contrário de max() e min(), ele toma apenas um único número.
'''
absolute = abs(-42)

print absolute

'''
Finalmente, a função type() retorna o tipo dos dados que recebe como um argumento. Se você pedir ao Python para fazer o seguinte:

print type(42)
print type(4.2)
print type('spam')

O resultado do Python será:

<type 'int'>
<type 'float'>
<type 'str'>
'''

# Exiba os tipos de um inteiro (integer), um número de ponto flutuante (float),
# e uma string em linhas separadas abaixo.
print type(42)
print type(4.2)
print type('spam')