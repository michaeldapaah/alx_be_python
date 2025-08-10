class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"
    

dog = Dog("shammy")
print(dog.eat())
print(dog.bark())

