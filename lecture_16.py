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
    
# my_car = Car("TATA", "Nexon")                                               # Car() -> Syntax to create 'object' 

# print(my_car.brand)                                                         # The code `print(my_car.brand)` is accessing the `brand` attribute of the `my_car` object using the dot notation '.' and printing its value.
# print(my_car.model)





# ''''''''''''''''''''''''''''''''''''''''''''              Instance of a Class:      ( my_car --> specific Object, instance of a class)

    
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
#         return f"{self.brand} {self.model}"                                         # In a class, all variables will always be taken in self.variable format 
    
# my_car = Car("TATA", "Nexon")                                               

# print(my_car.brand)                                                         
# print(my_car.model)
# print(my_car.full_name())                                                           # as full_name is a function, so we will use '()' to access/execute it
    



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




# ............................................................            6. Class Variables Count




# class Car:   
#     total_car = 0                                                               
#     # Syntax:                                                               
#     def __init__(self, brand, model):                                                                        
#         self.brand = brand                                                               
#         self.model = model 
#         Car.total_car += 1                                                                              # Total number of variables counted (not much use)
        
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size                                              
        
        
# my_tesla = ElectricCar("Tesla", "model-S", "90kWh")                                                     # This is also being created by __init__method in class Car  

# safari= Car("Tata", "Safari")     

# safari_2 = Car("Toyoto", "Safari")
#                                                                                                         # In Python : No Immediate Garbage Collection
# safari_3= Car("Kia", "Safari")

# # print(safari.total_car)                                                                               # Not a right way to access it
# print(Car.total_car)                                                                                    # Direct access





# ..........................................................          7. Static Method


# Static methods are just like regular method. But unlike regular methods, Static methods doesn't need an object of a class to be called
# A special way to get information or do something without needing to use the object directly


# class Car:   
    
#     total_car = 0                                                               
                                                                
#     def __init__(self, brand, model):                                                                        
#         self.brand = brand                                                               
#         self.model = model 
#         Car.total_car += 1                                                                              # Total number of variables counted (not much use)
    
#     @staticmethod                                                                                       # @static method : Decorators
#     def general_description():                                                                          # Not any need to use self in static method (no linkage needed for object)
#         return "Car is 5 star rated in toughness." 
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size                                                                                          

# safari= Car("Tata", "Safari")     

# # print(safari.general_description())                                                                   # Object unable to access a static method
# print(Car.general_description())                                                                        # Static method using only class and no need of Object
  




# .......................................................            8. Property Decorators


# To enhance method ki functionality and to implement some rules.


# class Car:   
    
#     total_car = 0                                                               
                                                                
#     def __init__(self, brand, model):                                                                        
#         self.brand = brand                                                               
#         self.__model = model                                                                            # making 'model' private
#         Car.total_car += 1                                                                              
    
    
#     @staticmethod                                                                                       # @static method : Decorators
#     def general_description():                                                                         
#         return "Car is 5 star rated in toughness." 
    
#     @property                                                                                           # @property : read-only , over-riding is now not possible (accessable only as a property )
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size                                                                                          

# safari= Car("Tata", "Safari")  

# safari.model = "city"                                                                                    # We have to prevent this change/update
                                                             
# print(safari.model)                                                                    
  




# .........................................................           9. Class Inheritance and isinstance() function





# class Car:   
    
#     total_car = 0                                                               
                                                                
#     def __init__(self, brand, model):                                                                        
#         self.brand = brand                                                               
#         self.__model = model                                                                            
#         Car.total_car += 1                                                                              
    
    
#     @staticmethod                                                                                       
#     def general_description():                                                                         
#         return "Car is 5 star rated in toughness." 
    
#     @property                                                                                           
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):                                                               
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)                                                
#         self.battery_size = battery_size                                                                                          


# my_tesla = ElectricCar("Tesla", "model-s", "90-KWH")

# # safari= Car("Tata", "Safari")  

# print(isinstance(my_tesla, Car))                                                                        # isinstance() function : object of ElectricCar as well as Car
# print(isinstance(my_tesla, ElectricCar))    





# ..........................................................         10. Multiple Inheritance           (Doubt)



# class Battery:
#     def __init__(self, model):
#         self.model = model
        
# class Engine:
#     def __init__(self, power):
#         self.power = power
        
# class ElectricCar(Battery, Engine):
#     def __init__(self, model, power):
#         super().__init__(model)
#         # super().__init__(power)                                                                               # This is over-riding my Battery class

# my_new_tesla = ElectricCar("cello", "506-HorsePower")

# print(my_new_tesla.model)
# # print(my_new_tesla.power)
    
    
    
    
    
# ////////////////////////////////////////////////////////////////////////////////////



# class Battery:
#     def battery_size(self):
#         return "long lasting battery"
    
# class Engine:
#     def engine_info(self):
#         return "more cc than a bike's"
    
# class ElectricCar(Battery, Engine):
#     pass

# my_new_tesla = ElectricCar()
# print(my_new_tesla.engine_info())
# print(my_new_tesla.battery_size())
