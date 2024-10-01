"""Private members"""
# Private members are similar to protected members, the difference is that the class members declared private should neither 
# be accessed outside the class nor by any base class. 


# In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

# However, to define a private member prefix the member name with double underscore “__”.

# Python program to
# demonstrate private members

# Creating a Base class


class Base:
    def __init__(self):
        self.a = "Bhavesh Mali"
        self.__c = "Bhavesh Mali"

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class
