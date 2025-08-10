class Calculator:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def multiply(x,y):
        return x * y
    
add = Calculator.add(5, 3)
print(add)

multiply = Calculator.multiply(5, 3)
print(multiply)