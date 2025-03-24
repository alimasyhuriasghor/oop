class Hero:
    # Class variables are variables that are shared across all instances
    jumlah = 0

    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        # Instance variables are variables that are unique to each instances of a class
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

        # .__class__ is a special attribute that every instance in Python has. It points to the class from which the instance was created
        self.__class__.jumlah += 1

    def __repr__(self) -> str:
        attrs = ", ".join(f"{key}='{value}'" if isinstance(value, str) else
                          f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"

hero1 = Hero("Gerry", 100, 40, 60)
hero2 = Hero("Mogi", 100, 60, 40)

print(hero1)
print(hero2)