shopping_list = ["banana", "laranja", "maca"]

stock = {
    'pera': 15,
    'laranja': 32,
    'banana': 6,
    'maca': 0   
}
    
prices = {
    'pera': 3,
    'laranja' : 1.5,
    'banana': 4,
    'maca' : 2   
}
total = 0
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
	valor = prices[key] * stock[key]
	total = total + valor
print
print
print total


def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] >0:
            total += prices[key]
            stock[key] -= 1
    return total
