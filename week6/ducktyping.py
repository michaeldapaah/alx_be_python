class Dog:
    def make_sound(self):
        return "Woof!"
    
class Cat:
    def make_sound(self):
        return "Meow!"
    
class Bird:
    def make_sound(self):
        return "Chirp!"
    
def let_them_speak(animals):
    for animal in animals:
        print(animal.make_sound())

    
bird = Bird()
cat = Cat()
dog = Dog()

animals = [bird, cat, dog]
let_them_speak(animals)