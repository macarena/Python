def digit_sum(n):
    result = 0
    
    for i in str(n):
        print i
        result += int(i)
    print result
    return result
numer = raw_input("Digite um numero")
digit_sum(numer)