# Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details 
# from the user and show the details that are relevant to the users.

# A simple example of this can be a car. A car has an accelerator, clutch, and break and we all know that pressing 
# an accelerator will increase the speed of the car and applying the brake can stop the car but we don’t know the 
# internal mechanism of the car and how these functionalities can work this detail hiding is known as data abstraction.

# To understand data abstraction we should be aware of the below basic concepts:

# OOP concepts in Python
# Classes in Python
# Abstract classes & Abstract Method in Python

# Importance of Data Abstraction
# It enables programmers to hide complex implementation details while just showing users the most crucial data and 
# functions. This abstraction makes it easier to design modular and well-organized code, makes it simpler to understand 
# and maintain, promotes code reuse, and improves developer collaboration.

# Data Abstraction in Python
# Data abstraction in Python is a programming concept that hides complex implementation details while exposing only 
# essential information and functionalities to users. In Python, we can achieve data abstraction by using abstract 
# classes and abstract classes can be created using abc (abstract base class) module and abstractmethod of abc 
# module.

# Abstraction classes in Python
# Abstract class is a class in which one or more abstract methods are defined. When a method is declared inside the 
# class without its implementation is known as abstract method.

# Abstract Method: 
# In Python, abstract method feature is not a default feature. To create abstract method and abstract classes we have 
# to import the “ABC” and “abstractmethod” classes from abc (Abstract Base Class) library. Abstract method of base 
# class force its child class to write the implementation of the all abstract methods defined in base class. 
# If we do not implement the abstract methods of base class in the child class then our code will give error. 
# In the below code method_1 is a abstract method created using @abstractmethod decorator.

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass
    
# Concrete Method: 
# Concrete methods are the methods defined in an abstract base class with their complete implementation. 
# Concrete methods are required to avoid reprication of code in subclasses. For example, in abstract base class 
# there may be a method that implementation is to be same in all its subclasses, so we write the implementation of 
# that method in abstract base class after which we do not need to write implementation of the concrete method again 
# and again in every subclass. In the below code startEngine is a concrete method.


# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()