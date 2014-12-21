#Lembra-se de como um número par é um número divisível por 2?
def is_even(x):
    if(x%2 == 0):
        print "o numero %s e par" % (x)
        return True
    else: 
        print "O numero %s nao e par" % (x)
        return False
is_even(35)
        