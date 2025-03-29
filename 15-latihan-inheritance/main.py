from hero import HeroIntelligent, HeroStrength

def main():
    lina = HeroIntelligent("Lina")
    slardar = HeroStrength("Slardar")

    print(lina)
    print("\n")
    print(slardar)

    lina.gainExp = 200
    slardar.gainExp = 250
    
    print(lina)
    print("\n")
    print(slardar)

if __name__ == "__main__":
    main()
