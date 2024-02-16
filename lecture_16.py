# .....................................................           Object-Oriented Programming



# Attributes  ==  Variables 
# Generalized form


# ................................................            1. Basic Class and Object 

class Car:                                                                  # Convention : Capitalize the 'Name'
    # Syntax:                                                               # To provide value as input
    def __init__(self, brand, model):                                       # __init__() : it is a method by which --> we can pass Variables/Attributes (Also called 'Constructor' -> 1st method to be called)
                                                                            # 'self' parameter -->  a reference to the current instance of the class, and is used to access variables that belongs to the class
        self.brand = brand                                                 
        self.model = model                                                  # self.brand --> Differtiating between a class variable/attribute and parameters
    
    # pass        -->                                                       # pass(a Keyword) : a placeholder to store future code
    
my_car = Car("Toyota", "Tata")                                              # Car() -> Syntax to create 'object' 

print(my_car.brand)                                                         # to access variables/attributes of a class -> "."
print(my_car.model)

























