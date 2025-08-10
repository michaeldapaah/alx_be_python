class Bird:
    def fly(self):
        return "Flies high in the sky high"
    def run(self):
        return "Runs fast on the ground"
    
class Mammal:
    def fly(self):
        return "Flies high in the sky"
    def run(self):
        return "Runs on four legs"
   
class Bat(Bird, Mammal):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a bat that can fly and run."
    

bat = Bat("Bruce")
print(bat.fly())  # Output: Flies high in the sky
print(bat.run())  # Output: Runs fast on the ground