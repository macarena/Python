def purify(lista):
    new_list = []
    for i in lista:
        if(i%2 == 0):
            new_list.append(i)
            
    return new_list
print purify([6,8,12,2,23])