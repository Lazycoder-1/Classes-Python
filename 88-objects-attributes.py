
# assigning attributes to objects in the class

class Houses:
    def __init__(self,location,price,model):
        self.location = location
        self.price = price
        self.model = model
    def house(self):
        print('This {} at {} now costs {}$'.format(self.model,self.location,self.price))

hs1 = Houses('Miami',20000000,'2 Bedroom')
hs2 = Houses('Denver',15000,'4 Bedroom')

print(hs1.house())
print(hs2.house())


# examples from W3 Schools










