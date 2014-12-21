classes = ["Knight", "Paladin", "Druid", "Sorcerer"]
for i in classes:
    print i
else:
    op = raw_input("Escolha uma classe: ")
    if(op.lower() == "knight"):
       print "Boa escolha Campeao"
    elif (op.lower() == "paladin"):
        print "Entao voce gosta de ataques a longa distancia?"
    elif(op.lower() == "druid"):
        print "Voce pertecne a natureza"
    elif(op.lower() == "sorcerer"):
        print "Aproveite seus poderes de destruicao"
    else:
        print "Classe invalida"