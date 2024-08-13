
# introduction to inheritance
# a process in which one class takes the attributes from another class

# Houses is the parent class
class Houses:
    def __init__(self,location,price):
        self.location = location
        self.price = price
    def action(self):
        print('This house in {} costs ${}'.format(self.location,self.price))
# City is the child class , in which the parent class passed(pass) in
class City(Houses):
    pass

Florida = City('Miami',300000)
San_Francisco = City('Silicon Valley', 45000)
Florida.action()









