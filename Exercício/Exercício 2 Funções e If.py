'''
Um inteiro � apenas um n�mero sem parte decimal (por exemplo, -17, 0, e 42 s�o inteiros, mas 98,6 n�o �).

Para fins desta li��o, vamos dizer tamb�m que um n�mero com parte decimal igual a 0 tamb�m � um inteiro, como 7,0.

Isso significa que, para esta li��o, voc� n�o pode simplesmente testar a entrada e ver se ela � tipo int.

Se a diferen�a entre um n�mero e esse mesmo n�mero arredondado para baixo for maior do que zero, 
o que isso diz sobre esse n�mero em particular?
'''
def is_int(x):
    
    
    if x <= 0:
      x = -x
      if( x > int(x)):
        return False
      else:
        return True
    elif x > 0 and x > int(x):
        return False        
    else:
        return True
is_int(-3.4)
    