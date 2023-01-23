from abc import ABC, abstractmethod

class Animal(ABC, ):
    def __init__(self, trait1):
        self.trait1 = trait1
        

class Bird(Animal):
    def __init__(self, trait1, trait2):
        super().__init__(trait1)
        self.trait2 = trait2

    @abstractmethod
    def speak(self):
        pass

class Penguin(Bird):
    def __init__(self, trait1, trait2):
        super().__init__(trait1, trait2)
        self.fly_ = False

    def speak(self):
        return f"Honk"

    def slide(self):
        return f"slides...."

class Eagle(Bird):
    def __init__(self, trait1, trait2):
        super().__init__(trait1, trait2)
        self.fly_ = True

    def speak(self):
        return f"Caw"


bird1 = Eagle("Red", 7)
bird2 = Penguin("Black", -50)

print(bird1.trait1)
print(bird2.trait1)
print(bird1.fly_)
print(bird2.fly_)

