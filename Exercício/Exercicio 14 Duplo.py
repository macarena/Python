def remove_duplicates(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista
print remove_duplicates([4,5,5,4])