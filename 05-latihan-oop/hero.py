class Hero:

    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def __repr__(self) -> str:
        attrs = ", ".join(f"{key}='{value}'" if isinstance(value, str) else
                          f"{key}={value}" for key, value in self.__dict__.items())
        
        return f"{type(self).__name__}({attrs})"
    
    def attack(self, opponent) -> None:
        print(f"{self.name} attacks {opponent.name}")
        opponent.under_attack(self, self.power)

    def under_attack(self, opponent, amount_power) -> None:
        print(f"{self.name} gets under attack by {opponent.name}")
        recevied_damage = amount_power / self.armor
        print(f"The amount of damage that {opponent.name} attacked was {recevied_damage}")
        self.health -= recevied_damage
        print(f"The amount of {self.name}'s health after got under attack by {opponent.name} is {self.health}")

    