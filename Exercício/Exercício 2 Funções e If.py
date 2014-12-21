'''
Um inteiro é apenas um número sem parte decimal (por exemplo, -17, 0, e 42 são inteiros, mas 98,6 não é).

Para fins desta lição, vamos dizer também que um número com parte decimal igual a 0 também é um inteiro, como 7,0.

Isso significa que, para esta lição, você não pode simplesmente testar a entrada e ver se ela é tipo int.

Se a diferença entre um número e esse mesmo número arredondado para baixo for maior do que zero, 
o que isso diz sobre esse número em particular?
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
    