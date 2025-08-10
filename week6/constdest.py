class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"farewell my friend {self.name}")


person = Person("Mike", 22)
del person
