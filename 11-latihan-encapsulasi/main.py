class Hero:

    # Private class variable
    __jumlah = 0

    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = power
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__power = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthStandar

        self.__class__.__jumlah += 1

    def __str__(self) -> str:
        return f"{self.__name}: level {self.__level}\n\thealth = {self.__health}/{self.__healthMax}\n\tattack = {self.__power} \n\tarmor = {self.__armor}"
    
    @property
    def gainExp(self) -> None:
        pass

    @gainExp.setter
    def gainExp(self, addExp) -> None:
        self.__exp += addExp
        if self.__exp >= 100:
            print(f"{self.__name} level up!")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__power = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    
    def attack(self, opponent) -> None:
        self.gainExp = 50
    
slardar = Hero("Slardar", 100, 5, 10)
axe = Hero("Axe", 100, 5, 10)
print(slardar)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar)

