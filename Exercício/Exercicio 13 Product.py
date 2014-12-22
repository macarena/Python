def product(x):
    count = 1
    for i in range(0,len(x)):
        count *=x[i]
    return count
print product([1,2,3,4,5])