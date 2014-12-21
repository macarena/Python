def censor(text,word):
    lista = text.split()
    for i in range(0,len(lista)):
        if lista[i] == word:
            lista[i] = "*" * len(word)
    
    return " ".join(lista)

print censor("rafa is rafa when rafa is not rafa","rafa")