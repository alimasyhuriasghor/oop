class Hero:
    # Private class variable
    __jumlah = 0

    def __init__(self, name: str, health: int) -> None:
        # Public instance variables
        self.name = name
        self.health = health

        # Private instance variable
        self.__private = "Private"
        
        # The variable jumlah on class Hero will be incremented each time an instance of class Hero is created
        self.__class__.__jumlah += 1

# Create an instance of a class Hero
gerry = Hero("Gerry", 100)

print(gerry.__dict__)
print(Hero.__dict__)

# These two lines of code will thrown an AttributeError exception
# print(gerry.__private) 
# print(Hero.__jumlah)

# These two lines of code will work to access their private variables, but they are discouraged to do so.
print(gerry._Hero__private) 
print(Hero._Hero__jumlah)