#Lembra-se de como um n�mero par � um n�mero divis�vel por 2?
def is_even(x):
    if(x%2 == 0):
        print "o numero %s e par" % (x)
        return True
    else: 
        print "O numero %s nao e par" % (x)
        return False
is_even(35)
        