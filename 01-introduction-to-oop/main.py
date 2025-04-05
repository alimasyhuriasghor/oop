# 1. Introduction To OOP

class Hero: # A class is a template to create user-defined objects
    pass

# Objects are variable name that has attributes and methods. In this examples, I didn't write the methods because this is just an introduction to OOP.
hero1 = Hero()
hero2 = Hero()

hero1.name = "Gerry"
hero1.health = 100
hero1.power = 40

hero2.name = "Mogi"
hero2.health = 100
hero2.power = 60

print(hero1.__dict__)
print(hero2.__dict__)