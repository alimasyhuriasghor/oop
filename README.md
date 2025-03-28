# Howdy! Welcome To My OOP (Object-Oriented Programming) Repository

This repository contains all of my OOP (Object-Oriented Programming) tutorial from trusted sources. Each of which will have their own branch and reference from where I borrowed the Object-Oriented Programming tutorials.

# What Is OOP?

According to "[Dive Into Design Patterns](https://refactoring.guru/design-patterns/book)" book which was explained by [Indonesia Belajar](https://www.youtube.com/watch?v=_Ld8wMr4OZ4&list=PL2O3HdJI4voFoyU6YyuLBdrsBSZWWtbQt), Object-Oriented Programming is a paradigm based on the concept of wrapping pieces of **data** (attributes) and **behaviour** (methods) related to that data into special bundles called [objects](https://docs.python.org/3/glossary.html#term-object), which are constructed from a set of "blueprints" defined by a programmer called [classes](https://docs.python.org/3/glossary.html#term-class).

Often we hear the words "object" and "instance" are used interchangeably. However, in my opinion, object is any data that has attributes and methods, whereas an instance is a spesific object's name with given name. 

For instance, below is the example of Python code that implements OOP paradigm concept:

```python
# Create a template's name to make user-defined objects
class Person: 
    # Create an initializer to set attributes for each objects of a class Person
    def __init__(self, name: str, age: int) -> None:
        # Create instance variables for each objects of a class Person. They are also guaranteed to be unique to each instances.
        self.name = name
        self.age = age

    # Create a string (str) representation object that is meant to be readble to the user
    def __str__(self) -> str:
        return f"Person's name: {self.name}\nPerson's age: {self.age}"

    # Create an instance method to greet other instance's name
    def greet(self, other) -> None:
        print(f"{self.name} greets {other.name}")
        
# Create instances object of a class Person

# ali is indeed an instance because it is a spesific object's name that was created from a class Person. It is also an object because it has attributes and methods
ali = Person("Ali", 21)

# muchsin is indeed an instance because it is a spesific object's name that was created from a class Person. It is also an object because it has attributes and methods
muchsin = Person("Muchsin", 20)

# abdullah is indeed an instance because it is a spesific object's name that was created from a class Person. It is also an object because it has attributes and methods
abdullah = Person("Abdullah", 25)

# Print all of the instance details
print(ali) # Output: Person's name: Ali
           #         Person's age: 21

print(muchsin) # Output: Person's name: Muchsin
               #         Person's age: 20

print(abdullah) # Output: Person's name: Abdullah
                #         Person's age: 25

# Do something to the instances
ali.greet(muchsin) # Output: Ali greets Muchsin

abdullah.greet(muchsin) # Output: Abdullah greets Muchsin
    
```

# Code Elaborations

Please do note that `self` refers to the instance of a class. It is exists because all special and instance methods are always received their instances as for the first argument.

## Class

Class is a template to create objects.

## `__init__()`

`__init__()` is a special method in Python that is automatically called when we create an instance of a class. Its primary purpose is used to initialize the attributes of an object during object creation.

## `__str__()`

`__str__()` is a special method that returns a friendly user readable string representation of an object.

## `greet(self)`

`greet(self)` is an instance method. It is a method that bounds to the object of a class.
