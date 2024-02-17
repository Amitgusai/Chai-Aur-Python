# ...................................................         Decorators in Python



# .....................................................           1. Timing Function Execution



# Time a function takes to execute - using decorator
# We can take decorator as a toll pass

# import time

# #syntax: of making decorator
# def timer(func):                                                                                                    # The `func` parameter in the `timer` function represents the original function(example_func) that is being timed.
    
#     def wrapper(*args, **kwargs):                                                                                   # *args : arguments ,  **kwargs : keyword arguments
        
#         start = time.time()                                                                                         # starting point time
#         result = func(*args, **kwargs)                                                                              # calling the original function 'func' with argumets and storing in 'result' variable , allows the decorator to exucute the original funtion                                                                         
#         end = time.time()                                                                                           # ending point time
        
#         print(f"{func.__name__}ran in {end - start} time")                                                          # __name__ : name of the original function is accessed using 'name' attribute , Total time = end - start
#         return result                                                                                               # To complete the execution of wrapper function, we returned something(result)
    
#     return wrapper                                                                                                  # The 'wrapper' function is being returned by the 'timer' decorator.


# @timer                                                                                                              # now --> whenever we will call example_func function, it cannot be directly called : It will go through @timer decorator
# def example_func(n):        
#     time.sleep(n)
    
# example_func(2)                                                                                                     # In this case, the `example_func` function is passed as the `func` parameter when using the `@timer` decorator




# .........................................................         2. Debugging Function Calls



def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
    
greet("chai", greeting="hanji")

























