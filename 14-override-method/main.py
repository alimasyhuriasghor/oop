class Hero:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def info(self) -> None:
        print("Show info in Hero's class")
        print(f"Hero's name: {self.name}\nHero's type: {type(self).__name__}\nHero's health: {self.health}")

class Marksman(Hero):
    
    def __init__(self, name, health=100):
        super().__init__(name, health)

    # Override the info method
    def info(self) -> None:
        print("Show info in Marksman's class")
        print(f"Hero's name: {self.name}\nHero's type: {type(self).__name__}\nHero's health: {self.health}")

# Create instance object of a class Marksman which was inherited from Hero class

sparrow = Marksman("Sparrow")

sparrow.info()