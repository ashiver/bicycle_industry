# Class Definitions for An Object-Oriented Model of the Bicycle Industry

#Model names mapped to price in USD, weight in lbs
models = {
    "X1":  [100, 30],
    "Flyer":  [250, 10],
    "Roadster":  [150, 25],
    "Fireball":  [400, 15],
    "King":  [600, 12],
    "Viper":  [800, 8]
}

class Bicycle(object):
    def __init__(self, model):
        self.model = model
        print "Created a new {}.".format(model)
        
    def stock(self, shop):
        shop.inventory[self.model].append(self)
        print "Added a {} to {}'s inventory. {} now has {} {}s.".format(self.model, shop.name, shop.name, len(shop.inventory[self.model]), self.model)
      

class Shop(object):
    def __init__(self, name, markup):
        self.name = name
        self.markup = float(markup)
        self.inventory = {key: [] for key in models}
        self.prices = {key: float((models[key][0] + (models[key][0] * (self.markup / 100)))) for key in models}
        self.money = 0
        print "The shop {} now exists.".format(name)
        
    def sell(self, model, customer):
        if len(self.inventory[model]) > 0:
            if self.prices[model] <= customer.money:
                customer.bikes.append(self.inventory[model][0])    
                self.inventory[model].pop(0)
                customer.money = customer.money - self.prices[model]
                self.money = self.money + self.prices[model]
                print "{} sold a {} to {} for ${}".format(self.name, str(model), customer.name, self.prices[model])
                print "{} has {} model {}s remaining in its inventory.".format(self.name, len(self.inventory[model]), model)
            else:
                print "Oops. {} doesn't have enough money to buy a {}.".format(customer.name, str(model))
        else:
            print "Oops. {} doesn't have any model {}s in stock.".format(self.name, str(model))
    
class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = float(money)
        self.bikes = []
        print "{} now exists and has ${} to spend.".format(name, money)
        
    def buy(self, model, shop):
        if len(shop.inventory[model]) > 0:
            if shop.prices[model] <= self.money:
                self.bikes.append(shop.inventory[model][0])
                shop.inventory[model].pop(0)
                self.money = self.money - shop.prices[model]
                shop.money = shop.money + shop.prices[model]
                print "{} bought a {} from {}.".format(self.name, str(model), shop.name)
                print "The bike cost ${} and {} has ${} left to spend.".format(shop.prices[model], self.name, self.money)
            else:
                print "Oops. {} doesn't have enough money to buy a {}.".format(self.name, str(model))
        else:
              print "Oops. {} doesn't have any model {}s in stock.".format(shop.name, str(model))
