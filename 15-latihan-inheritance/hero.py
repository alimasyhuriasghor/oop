class Hero:

    def __init__(self, name: str) -> None:
        self.health_pool = list(range(0, 600, 100))
        self.attPower_pool = list(range(0, 60, 10))
        self.armor_pool = list(range(6))
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def __str__(self) -> str:
        return f"{self.__name}\n\tlevel: {self.__level}\n\thealth: {self.__health}\n\tattPower: {self.__attPower}\n\tarmor: {self.__armor}"
    
    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self, amount_health):
        self.__health_pool = amount_health

    @attPower_pool.setter
    def attPower_pool(self, amount_attack):
        self.__attPower_pool = amount_attack

    @armor_pool.setter
    def armor_pool(self, amount_armor):
        self.__armor_pool = amount_armor

    @gainExp.setter
    def gainExp(self, input):
        self.__exp = input
        if self.__exp >= 100:
            self.levelUp = self.__exp // 100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class HeroIntelligent(Hero):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.health_pool = list(range(0, 251, 50))
        self.attPower_pool = list(range(0, 101, 20))
        self.armor_pool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.levelUp = 1

class HeroStrength(Hero):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.health_pool = list(range(0, 700, 100))
        self.attPower_pool = list(range(0, 101, 20))
        self.armor_pool = list(range(0, 11, 2))
        self.levelUp = 1