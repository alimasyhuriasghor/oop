class Hero:

    def __init__(self, name: int, health: int) -> None:
        self.name = name
        self.health = health

class Marksman(Hero):

    def __init__(self, name, health):
        super().__init__(name, health)


