# Howdy! Welcome To My OOP (Object-Oriented Programming) Repository

This repository contains all of my OOP (Object-Oriented Programming) tutorial from trusted sources. Each of which will have their own branch and reference from where I borrowed the Object-Oriented Programming tutorials.

# What Is OOP?

According to "[Dive Into Design Patterns](https://refactoring.guru/design-patterns/book)" book which was explained by [Indonesia Belajar](https://www.youtube.com/watch?v=_Ld8wMr4OZ4&list=PL2O3HdJI4voFoyU6YyuLBdrsBSZWWtbQt), Object-Oriented Programming is a paradigm based on the concept of wrapping pieces of **data** (attributes) and **behaviour** (methods) related to that data into special bundles called [objects](https://docs.python.org/3/glossary.html#term-object), which are constructed from a set of "blueprints" defined by a programmer called [classes](https://docs.python.org/3/glossary.html#term-class).

Often we hear the words "object" and "instance" are used interchangeably. However, in my opinion, object is any data that has attributes and methods, whereas an instance is a spesific object's name with given name. 

For instance, below is the example of Python code that implements OOP paradigm concept:

```python
class Person:
    """
    A class which represents a person.

    Attributes:
    name (str): the name of the person.
    age (int): the age of the person.
    """

    def __init__(self, name: str, age: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Error, expected 'name' to be str! Got {type(name).__name__}.")
        self.name = name

        if not isinstance(age, int):
            raise TypeError(f"Error, expected 'age' to be an int! Got {type(age).__name__}.")
        self.age = age

    def __str__(self) -> str:
        return f"Person's name: {self.name}\nPerson's age: {self.age}"
    
    def __repr__(self) -> str:
        attrs = ", ".join(f"{key}='{value}'" if isinstance(value, str) else
                          f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"

    def greet(self, other) -> None:
        """Greet other instance's name."""
        print(f"{self.name} greets {other.name}")

# Create instances of a class Person
ali = Person("Ali", 21)
muchsin = Person("Muchsin", 21)

# Print the objects detail
print(f"{ali!r}")

# Output: Person(name='Ali', age=21)

print(f"{muchsin!r}")

# Output: Person(name='Muchsin', age=21)

# Do something to the instances
ali.greet(muchsin)

# Output: Ali greets Muchsin

muchsin.greet(ali)

# Output: Muchsin greets Ali
```

# Code Elaborations

Please do note that `self` refers to the instance of a class. It is exists because all special and instance methods are always received their instances as for the first argument.

## 1. Class

Class is a template to create objects.

## 2. Init

`__init__(self, name: str, age: int) -> None` is a special method in Python that is automatically called when we create an instance of a class. Its primary purpose is used to initialize the attributes of an object during object creation.

## 3. Str

`__str__(self) -> str` is a special method in Python that returns a human-readble representation of the object it self.

## 4. Repr

`__repr__(self) -> str` is a special method in Python that returns the real object representation it self after we've defined the attributes value.

## 5. Greet

`greet(self, other) -> None` is an instance method. It's a method that bounds to the object of a class. Its primary purpose is to access and modify the object's attributes. In this case, it's used to acces the object's attribute to greet other instance's name.

> **Note**: Please do note that `self` is not a keyword in Python. However, by convention, all of instance and special methods must have `self` for their first parameter. It's also refers to the instance of a class, and behind the scences, Python automatically passes the instance to the first argument, which is `self`.
