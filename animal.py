from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, genus, colour):
        self.genus = genus
        self.colour = colour

    @abstractmethod
    def speak(self):
        return f"{self.genus} says 'generic sounds'"

class Bird(Animal):
    def __init__(self, colour, fly_, genus):
        super().__init__(genus, colour)
        self.fly_ = fly_

    def speak(self):
        return f"{self.genus} says tweet."

    def fly(self):
        if self.fly_:
            return f"Flies"
        else:
            return f"This bird cannot fly"

class Fish(Animal):
    def __init__(self, colour, fins, genus):
        super().__init__(genus, colour)
        self.fins = fins

    def speak(self):
        return f"{self.genus} says blub."

bird1 = Bird("blue", True, "BirdusBirdus")
bird2 = Bird("grey", False, "OtherusBirdus")
fish1 = Fish("Blue", 5, "FishusFishus")

print(bird1.fly())
print(bird2.fly())

setattr(bird2, "colour", "None")
print(bird2.colour)

delattr(bird2, "colour")
try:
    print(bird2.colour)
except:
    print("There is no corresponding attribute")

print(bird1.genus)
print(bird2.genus)

print(bird1.speak())
print(fish1.speak())

new = Animal()