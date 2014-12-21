#Quando você quiser exibir uma variável com uma string, há um modo melhor do que concatenar strings.

name = "Mike"
print "Ola %s" % (name)
#O operador % depois de uma string é usado para combinar uma string com variáveis. 
#O operador % substituirá um %s na string pela variável string que vem depois dele.

string_1 = "Camelot"
string_2 = "lugar"
#Lembre-se, usamos o operador % para substituir os espacadores temporarios %s com as variaveis entre parenteses.

name = "Mike"
print "Ola %s" % (name)
#Você precisa do mesmo número de %s termos em uma string que o número de variáveis entre parênteses:

print "Nao vamos para %s. E um %s bobo." % (string_1, string_2)
print "Os %s que %s %s!" % ("Cavaleiros", "Dizem", "Ni")
# Isso exibia "Os Cavaleiros que Dizem Ni!"

name = raw_input("Qual e o seu nome?")
quest = raw_input("Qual e sua missao?")
color = raw_input("Qual e sua cor favorita?")
#raw_input pergunta pro usuário no console

print "Ah, entao seu nome e %s, sua missao e %s, " \
"e sua cor favorita e %s." % (name, quest, color)