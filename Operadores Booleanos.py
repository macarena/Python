"""
Vamos começar com o aspecto mais simples do controle de fluxo: comparadores. Existem seis:

Igual a ("==")
Diferente de ("!=")
Menor do que ("<")
Menor ou igual a ("<=")
Maior que (">")
Maior ou igual a (">=")
Comparadores verificam se um valor é (ou não) igual, maior do que (ou igual a), ou menor que (ou igual a) outro valor.

Note que "==" compara se duas coisas são iguais, e "=" atribui um valor a uma variável.
"""

"""
     Operadores Booleanos
------------------------      True and True e True
True and False e False
False and True e False
False and False e False

True or True e True
True or False e True
False or True e True
False or False e False

Not True e False
Not False e True

"""
#AND
bool_one = 1 > 2 and 50 < 2

bool_two = -(-(-(-2))) == -2 and 4 >=16**0.5

bool_three = 19 % 4 != 300/ 10 / 10 and False

bool_four = -(1**2) < 2**0 and 10%10 <=20 - 10*2

bool_five = True and True

#OR
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1

#NOT
bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False


"""
Operadores booleanos não são simplesmente avaliados da esquerda para a direita. 
Assim como os operadores aritméticos, há uma ordem na execução dos operadores booleanos:

not é o primeiro a ser avaliado;
and é o segundo a ser avaliado;
or é o último a ser avaliado.
Por exemplo, True or not False and False retorna True. Se isto não tiver ficado claro, leia a Dica.


Parênteses () garantem que suas expressões sejam avaliadas na ordem que você quer. 
Qualquer coisa entre parênteses é avaliada como uma unidade separada.
"""
bool_one = False and not True and True

bool_two = False and not Tue or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

# Use expressoes booleanas nas linhas abaixo conforme apropriado!

# Torne-me falso!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # Fizemos esta para voce!

# Torne-me verdadeiro!
bool_two = not 44 < 43

# Torne-me falso!
bool_three = not 44 > 43

# Torne-me verdadeiro!
bool_four = 1 < 100000

# Torne-me verdadeiro!
bool_five = 1 == 2**0

response = 'Y'

answer = "Left"
if answer == "Left":
    print "Esta e a Sala de Abuso Verbal, seu monte de caca de papagaio!"
    
# A declaracao print acima sera exibida no console?
# Iguale response a 'Y' se achar que sim, ou 'N' se achar que nao.

i = 1
def using_control_once():
    if i ==1:
        return "Successo #1"

def using_control_again():
    if not not i == 1:
        return "Successo #2"

print using_control_once()
print using_control_again()

answer = "E so um arranhao!"

def black_knight():
    if answer == "E so um arranhao!":
        return True
    else:             
        return False      # Tenha certeza de que isso retorna False

def french_soldier():
    if answer == "Va embora, ou vou zombar de voce mais uma vez!":
        return True
    else:             
        return False       # Tenha certeza de que isso retorna False
		
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

"""
Comparadores

3 < 4
5 >= 5
10 == 10
12 != 13
Operadores booleanos

True or False 
(3 < 4) and (5 >= 5)
this() and not that()
Declaracoes condicionais

if this_might_be_true():
    print "This really is true."
elif that_might_be_true():
    print "That is true."
else:
    print "None of the above."

"""
# Tenha certeza que the_flying_circus() retorna True
def the_flying_circus(teste):
    if teste < 5 and teste > 0:    # Comece seu codigo aqui!
        # Nao esqueca de recuar
        # o codigo dentro deste bloco!
        return True
    elif teste > 5 or teste < 0:
        # Continue aqui.
        # Voce vai querer adicionar tambem a declarao else!
        return False
    else:
        return 1
    
print the_flying_circus(3)
