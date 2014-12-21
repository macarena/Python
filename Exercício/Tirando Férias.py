def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    destiny = city.lower()
    if destiny == "charlotte":
        return 183
    elif destiny == "tampa":
        return 220
    elif destiny == "pittsburgh":
        return 222
    elif destiny == "los angeles":
        return 475
    else:
        return "Destino invalido"

def rental_car_cost(days):
    cost = 40 * days
      cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
'''
Lembre-se que uma declaração elif e verificada apenas se todas as declarações if/elif anteriores falharem.
'''
