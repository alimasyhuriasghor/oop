class Hero:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __repr__(self) -> str:
        attrs = ", ".join(f"{key}='{value}'" if isinstance(value, str) else
                          f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"
    
hero1 = Hero("Gerry", 100)
hero2 = Hero("Ali", 1000)

print(hero1)
print(hero2)