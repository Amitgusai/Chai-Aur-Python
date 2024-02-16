# .....................................................           Object-Oriented Programming



# Attributes  ==  Variables 
# Generalized form : Anyone can use this


# ................................................            1. Basic Class and Object 


# class Car:                                                                  # Convention : Capitalize the 'Name' (good practice)
#     # Syntax:                                                               # To provide input value or arguments from Object
#     def __init__(self, brand, model):                                       # The purpose of the init() method in a class is to initialize the attributes or variables of an object when it is created and passing the parameter provided by object [It is also known as the constructor method]
#                                                                             # By using the 'self' parameter, the method can access and assign values to the object's attributes, distinguishing them from the parameters passed to the method.
#                                                                             # self : Also providing a linkage between Object --> my_car and class --> Car
#         self.brand = brand                                                 
#         self.model = model                                                 
    
#     # pass        -->                                                       # pass(a Keyword) : a placeholder to store future code
    
# my_car = Car("TATA", "Nexon")                                               # Car() -> Syntax to create 'object' and my_car is copy of Object : Car()

# print(my_car.brand)                                                         # The code `print(my_car.brand)` is accessing the `brand` attribute of the `my_car` object using the dot notation '.' and printing its value.
# print(my_car.model)



# ''''''''''''''''''''''''''''''''''''''''''''              Instance of a Class:      ( my_car --> specific Object, instance )

    
# An instance of a class is like a special version of something that we create based on a blueprint. Let's say we have a blueprint for a car. The blueprint tells us what a car 
# should have, like a brand and a model. But we can't actually drive the blueprint, right? We need to make a real car based on the blueprint.

# So, when we make a real car based on the blueprint, that real car is an instance of the car class. It has all the things that the blueprint says a car should have, like a brand 
# and a model. We can give it a specific brand, like Toyota, and a specific model, like Camry. And then we can use that instance of the car class to do things, like drive it or show it to our friends.

# In simple terms, an instance of a class is like a real thing that we create based on a plan or blueprint. It has all the characteristics that the plan says it should have




# .................................................           2. Class Method and Self




# class Car:                                                                  
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
                                                                            
#         self.brand = brand                                                 
#         self.model = model   
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"                                         # In a class, all variables will always be taken as self.variable format (using f string)
    
# my_car = Car("TATA", "Nexon")                                               

# print(my_car.brand)                                                         
# print(my_car.model)
# print(my_car.full_name())                                                           # as full_name is a function, so we will use '()' to access it
    



# .........................................................           3. Inheritance (Bringing Functionality)



# class Car:                                                                  
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
                                                                            
#         self.brand = brand                                                 
#         self.model = model   
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"        

# class ElectricCar(Car):                                                               # (Car) : ElectricCar is inheriting Car class
#     def __init__(self, brand, model, battery_size):
        
#         super().__init__(brand, model)                                                # The line `super().__init__(brand, model)` is calling the `__init__` method of the parent class (`Car`) 
#         self.battery_size = battery_size                                              # and passing the `brand` and `model` arguments to it. This allows -->
#                                                                                       # 'ElectricCar' class to inherit the `brand` and `model` attributes from the `Car` class
        
        

# my_tesla = ElectricCar("Tesla", "model-S", "90kWh")

# print(my_tesla.brand)  
# print(my_tesla.model)  
# print(my_tesla.battery_size)     
# print(my_tesla.full_name())
                                     



# ..........................................................          4. Encapsulation




class Car:                                                                  
    # Syntax:                                                               
    def __init__(self, brand, model):                                                                        
                                                                            
        self.brand = brand                                                 
        self.model = model   
        
    def full_name(self):
        return f"{self.brand} {self.model}" 

my_car = Car("TATA", "Nexon")                                               

print(my_car.brand)                                                         
print(my_car.model)
print(my_car.full_name()) 



