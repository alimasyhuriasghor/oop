class Hero:
    
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

class Marksman(Hero):
    pass

class Fighter(Hero):
    pass

# Create the instances object of each classes that were inherited from Hero class
murdock = Marksman("Murdock", 100)
greystone = Fighter("Greystone", 200)

print(murdock.name)
print(greystone.name)