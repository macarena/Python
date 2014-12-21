def factorial(x):
    resultado = x
    i = 1
    for i in range(1,x):
        if(x==1):
            return 1
        resultado = factorial(x-1)*x
        
    return resultado
print factorial(10)