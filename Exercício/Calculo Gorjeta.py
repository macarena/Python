# Atribua um valor a variavel total na linha 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax #calcula o valor da refeição com o imposto
total = meal + meal * tip #calcula o valor da refeição + imposto + gorjeta

print meal
print("%.2f" % total)

def tax(bill):
    """Soma 8% de imposto a uma conta de restaurante."""
    bill *= 1.08
    print "Com imposto: %f" % bill
    return bill

def tip(bill):
    """Soma uma gorjeta de 15% a uma conta de restaurante."""
    bill *= 1.15
    print "com gorjeta de: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)