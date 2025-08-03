class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
tomatoes = Product("Tomatoes", 5, 3)
print(f"{tomatoes.name} : {tomatoes.total_price()} ghana cedis only")

    