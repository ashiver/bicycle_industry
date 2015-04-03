#Script for Model of the Bicycle Industry
from bicycles import *

s1 = Shop("Wheels", 20)

print " "

b1 = Bicycle("X1")
b2 = Bicycle("Flyer")
b3 = Bicycle("Roadster")
b4 = Bicycle("Fireball")
b5 = Bicycle("King")
b6 = Bicycle("Viper")

print " "

b1.stock(s1)
b2.stock(s1)
b3.stock(s1)
b4.stock(s1)
b5.stock(s1)
b6.stock(s1)

print " "

c1 = Customer("Ann", 200)
c2 = Customer("Bob", 500)
c3 = Customer("Carol", 1000)

print " "

for c in [c1, c2, c3]:
    for key in s1.prices:
        if c.money >= s1.prices[key]:
            print "{} can afford to buy a {}, which costs ${} at {}".format(c.name, key, str(s1.prices[key]), s1.name)
        
print ""

for model in s1.inventory:
    print "{} has {} {}s in stock.".format(s1.name, len(s1.inventory[model]), model)

print " "
                                   
c1.buy("X1",s1)
c2.buy("Flyer",s1)
c3.buy("Viper",s1)

print " "

for model in s1.inventory:
    print "{} has {} {}s in stock.".format(s1.name, len(s1.inventory[model]), model)

print " "

print "{} made a total profit of ${}.".format(s1.name, ((s1.prices[b1.model] + s1.prices[b2.model] + s1.prices[b6.model]) - (models[b1.model][0] + models[b2.model][0] + models[b6.model][0])))