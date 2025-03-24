from hero import Hero

def main():
    # Create the instance objects of a class Hero
    sniper = Hero("Sniper", 100, 10, 5)
    rikimaru = Hero("Rikimaru", 100, 20, 10)

    sniper.attack(rikimaru)
    print(rikimaru)


if __name__ == "__main__":
    main()