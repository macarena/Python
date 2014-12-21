#REVISÃO FUNÇÕES
def distance_from_zero(distance):
    if type(distance) == int or type(distance) == float:
         distancia = abs(distance)
         return distancia
    else:
        return "Nao"


print distance_from_zero(50)