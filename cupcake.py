from toppings import Toppings

class Cupcake:
    def __init__(self,flavor,icing):

        self.flavor = flavor
        self.icing = icing
        self.toppings = list()
    

    def order_chocolate(self):
        return f"You order a {self.flavor} cupcake with {self.icing}"

    def order_vanilla(self):
        return f"You ordered a {self.flavor} cupcake {self.icing}"
    
    @classmethod
    def alternate(cls,newdessert):
        return f"I don't like cupcakes, may I have a {newdessert}?"


    #order_chocolate = Cupcake("chocolate","chocolate")
   # order_vanilla = Cupcake("vanilla","vanilla")