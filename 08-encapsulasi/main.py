class Hero:

    def __init__(self, name: str, health: int, power: int) -> None:
        self.__name = name
        self.__health = health
        self.__power = power

    # Getter
    def get_name(self) -> str:
        return self.__name
    
    def get_health(self) -> int:
        return self.__health
    
    def get_power(self) -> int:
        return self.__power
    
    # Setter
    def attack(self, amount_attack) -> None:
        self.__health -= amount_attack

    def set_power(self, new_power) -> None:
        self.__power = new_power

    
# Awal dari game
gerry = Hero("Gerry", 100, 30)

# Game berjalan
print(gerry.get_name())

gerry.attack(5)
print(gerry.get_health())

gerry.set_power(50)
print(gerry.get_power())