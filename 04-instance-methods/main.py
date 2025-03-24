class Hero:
    # Class variable
    jumlah = 0

    def __init__(self, name: str, health: int, attack: int):
        # Instance variable
        self.name = name
        self.health = health
        self.attack = attack

        # Variable jumlah pada class Hero akan bertambah setiap kali objek Hero dibuat
        self.__class__.jumlah += 1

    # Void function, method tanpa return dan tanpa argumen
    def siapa(self) -> None:
        print(f"Namaku adalah {self.name}")

    # Method dengan arugment dan tanpa return
    def health_up(self, up: int) -> int:
        self.health += up

    # Method dengan return
    def get_health(self) -> int:
        return self.health

# Main program
hero1 = Hero("Gerry", 100, 40)
hero2 = Hero("Mogi", 100, 60)

hero1.health_up(10)
print(hero1.get_health())
        