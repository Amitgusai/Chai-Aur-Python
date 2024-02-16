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
                                     



# ..........................................................          4. Encapsulation  (example: a Capsule)




# class Car:                                                                  
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
                                                                            
#         self.__brand = brand                                                                # '__' (variable becomes private) : This means that the variable can be accessed within a class but now an Object cannot access it.                               
#         self.model = model                                                                  # To access them : we create methods
        
#     def get_brand(self):                                                                    # getters Convention : to start with 'get_' (we can change but will be breaking convention in industry)
#         return self.__brand + " !"                                                          # Useful in Cases where we need an response/input with some additional units for good appearance
        
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size                                              
        
        
# my_tesla = ElectricCar("Tesla", "model-S", "90kWh")        

# print(my_tesla.__brand)
# print(my_tesla.get_brand())            




# ....................................................              What is setter?                                                                           # HomeWork
 


# class Car:                                                                  
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
                                                                            
#         self.__brand = brand                                                               
#         self.model = model 
#     def get_brand(self):
#         return self.__brand

#     def set_brand(self, new_brand):
#         self.__brand = new_brand

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_vehicle = Car("tata", "nexon") 

# my_vehicle.set_brand("Toyota")                                                                  # setter method : Changes the variable  and update with a new value

# print(my_vehicle.get_brand())
# print(my_vehicle.brand)




# ........................................................            5. Polymorphism (concept)


# It allows different objects to respond to the same method call in different ways
# In the given context, the fuel_type() method is an example of polymorphism, as it is implemented differently in different classes that inherit from a common superclass


# class Car:                                                                  
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
#         self.brand = brand                                                               
#         self.model = model 
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel"
        
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size  
    
#     def fuel_type(self):
#         return "electric charge"                                            
        
        
# my_tesla = ElectricCar("Tesla", "model-S", "90kWh")  
# print(my_tesla.fuel_type())      

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())




# ............................................................            6. Class Variables





















