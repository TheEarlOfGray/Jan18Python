class Animal():
    def __init__(self, genus):
        self.genus = genus

    def speak(self, sound):
        return f"{self.genus} says {sound}"

class Bird(Animal):
    def __init__(self, colour, fly_, genus):
        super().__init__(genus)
        self.colour = colour
        self.fly_ = fly_

    def fly(self):
        if self.fly_:
            return f"Flies"
        else:
            return f"This bird cannot fly"

bird1 = Bird("blue", True, "BirdusBirdus")
bird2 = Bird("grey", False, "OtherusBirdus")

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

print(bird1.speak("tweet"))