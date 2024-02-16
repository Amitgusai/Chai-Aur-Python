# .....................................................           Object-Oriented Programming



# Attributes  ==  Variables 
# Generalized form


# ................................................            1. Basic Class and Object 

class Car:                                                                  # Convention : Capitalize the 'Name'
    # Syntax:                                                               # To provide input value or arguments from Object
    def __init__(self, brand, model):                                       # The purpose of the init() method in a class is to initialize the attributes or variables of an object when it is created. [It is also known as the constructor method]
                                                                            # By using the 'self' parameter, the method can access and assign values to the object's attributes, distinguishing them from the parameters passed to the method.
                                                                            
        self.brand = brand                                                 
        self.model = model                                                  
    
    # pass        -->                                                       # pass(a Keyword) : a placeholder to store future code
    
my_car = Car("Toyota", "Tata")                                              # Car() -> Syntax to create 'object' and my_car is copy of Object : Car()

print(my_car.brand)                                                         # The code `print(my_car.brand)` is accessing the `brand` attribute of the `my_car` object using the dot notation '.' and printing its value.
print(my_car.model)

























