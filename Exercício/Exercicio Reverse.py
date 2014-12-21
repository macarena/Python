def reverse(text):
    novaString = ""
    teste = len(text) - 1
    for i in text:
        reversing = text[teste]
        novaString += text[teste]
        teste-=1
    return novaString
print reverse("Rafael")