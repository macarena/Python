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
A fun��o max() toma qualquer n�mero de argumentos e retorna o maior deles. 
("Maior" pode ter defini��es estranhas, ent�o � melhor usar max() em n�meros inteiros e de ponto flutuante, 
onde os resultados s�o simples, n�o em outros objetos, como strings.)

Por exemplo, max(1,2,3) retornar� 3 (o maior n�mero no conjunto de argumentos).
min() retorna ent�o o menor de uma dada s�rie de argumentos.
'''
# Iguale minimum ao menor valor de qualquer conjunto de numeros na linha 3!

minimum = min(1,8,0,-239)

print minimum

'''
A fun��o abs() retorna o m�dulo do n�mero que toma como argumento � ou seja, 
a dist�ncia entre esse n�mero e 0 em uma reta num�rica imagin�ria. Por exemplo, 3 e -3 t�m o mesmo m�dulo: 3. 
A fun��o abs() sempre retorna um valor positivo, ao contr�rio de max() e min(), ele toma apenas um �nico n�mero.
'''
absolute = abs(-42)

print absolute

'''
Finalmente, a fun��o type() retorna o tipo dos dados que recebe como um argumento. Se voc� pedir ao Python para fazer o seguinte:

print type(42)
print type(4.2)
print type('spam')

O resultado do Python ser�:

<type 'int'>
<type 'float'>
<type 'str'>
'''

# Exiba os tipos de um inteiro (integer), um n�mero de ponto flutuante (float),
# e uma string em linhas separadas abaixo.
print type(42)
print type(4.2)
print type('spam')