def anti_vowel(text):
    vogal = {"a","e","i","o","u","A","E","I","O","U"}
    novaString = ""
    for i in text:
        if i not in vogal:
            novaString += i
    return novaString
print anti_vowel("Rafael")
        