#Quando voc� quiser exibir uma vari�vel com uma string, h� um modo melhor do que concatenar strings.

name = "Mike"
print "Ola %s" % (name)
#O operador % depois de uma string � usado para combinar uma string com vari�veis. 
#O operador % substituir� um %s na string pela vari�vel string que vem depois dele.

string_1 = "Camelot"
string_2 = "lugar"
#Lembre-se, usamos o operador % para substituir os espacadores temporarios %s com as variaveis entre parenteses.

name = "Mike"
print "Ola %s" % (name)
#Voc� precisa do mesmo n�mero de %s termos em uma string que o n�mero de vari�veis entre par�nteses:

print "Nao vamos para %s. E um %s bobo." % (string_1, string_2)
print "Os %s que %s %s!" % ("Cavaleiros", "Dizem", "Ni")
# Isso exibia "Os Cavaleiros que Dizem Ni!"

name = raw_input("Qual e o seu nome?")
quest = raw_input("Qual e sua missao?")
color = raw_input("Qual e sua cor favorita?")
#raw_input pergunta pro usu�rio no console

print "Ah, entao seu nome e %s, sua missao e %s, " \
"e sua cor favorita e %s." % (name, quest, color)