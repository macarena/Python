def is_prime(x):
    i=2
    if(x < 2):
        return False
    elif x==2:
        return True
    else:
        for i in range(2, x):
            if x%i == 0:
                return False
                break
        return True
            
print is_prime(9)