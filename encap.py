class User():
    def __init__(self, name, age, fav_colour, _password):
        self.name = name
        self.age = age
        self.fav_colour = fav_colour
        self._password = _password


    def getName(self, _password):
        if _password == self._password:
            return self.name
        else:
            return f"On yer bike!"

    def getAge(self):
        return self.age

    def getFav_colour(self):
        return self.fav_colour

    def get_password(self):
        return self._password

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setFav_colour(self, fav_colour):
        self.fav_colour = fav_colour

    def set_pasword(self, _password):
        self._password = _password

user1 = User("Earl", 34, "Purple", "Example123!")
        
# print(user1.name)
print(user1.getName("Example123"))

# print(user1.name)