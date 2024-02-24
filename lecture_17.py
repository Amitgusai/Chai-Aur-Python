# ...................................................         Decorators in Python


# A decorator is a function that takes another function as input/parameter and extends its functionality without modifying its code.
# Decorators in Python are like tollbooth for functions, adding functionality without changing the original function.


# Most Basic Decorator: 
    
def debug(func):
    def wrapper():
        return func()
    
    return wrapper   



# .....................................................           1. Timing Function Execution



# Time a function takes to execute - using decorator

import time

#syntax: of making decorator
def timer(func):                                                                                                    # The `func` parameter in the `timer` function represents the original function(example_func) that is being timed.
    
    def wrapper(*args, **kwargs):                                                                                   # *args : arguments ,  **kwargs : keyword arguments
        
        start = time.time()                                                                                         # starting point time
        result = func(*args, **kwargs)                                                                              # calling the original function 'func' with argumets and storing in 'result' variable , allows the decorator to exucute the original funtion                                                                         
        end = time.time()                                                                                           # ending point time
        
        print(f"{func.__name__}ran in {end - start} time")                                                          # __name__ : name of the original function is accessed using 'name' attribute , Total time = end - start
        return result                                                                                               # To complete the execution of wrapper function, we returned something(result)
    
    return wrapper                                                                                                  # The 'wrapper' function is being returned by the 'timer' decorator.


@timer                                                                                                              # now --> whenever we will call example_func function, it cannot be directly called : It will go through @timer decorator
def example_func(n):        
    time.sleep(n)
    
example_func(2)                                                                                                     # In this case, the `example_func` function is passed as the `func` parameter when using the `@timer` decorator




# .........................................................         2. Debugging Function Calls


# To print the function name and the values of its arguments 


def debug(func):
    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)                                                                                     # To access name of the arguments :-
        args_value = ', '.join(str(args) for args in args)                                                              # join() : we get a iterable list --> (comprehension) applying looping --> str(arg) : value stored and converted to string
        kwargs_value = ', '.join(f"{key}={value} " for key, value in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return ans
    
    return wrapper                                                                                                      # wrapper ki definition return hori to debug 

@debug
def hello():
    print("hello")
    
@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
  
hello()  
greet("chai", greeting="hanji")




# ............................................................            3. Cache Return Value 


#  It stores the results of function calls in a dictionary to avoid redundant computations when the same arguments are passed to the function again.

import time

def cache(func):
    cache_value = {}                                                                                                    # should be written outside the wrapper funciton and storing the result
                                                                                                                        # dictionary : In this accessing values are easy as compared to list(because of indexing in list)
    def wrapper(*args, **kwargs):
        
        # print(cache_value)                                                                                              # Rough
        
        if args in cache_value:
            return cache_value[args]                                                                                    # without executing the function again 
        num = func(*args, **kwargs)
        cache_value[args] = num
        return num
    
    return wrapper

@cache
def log_running_function(a, b):
    time.sleep(4)                                                                                                       # To better understand the decorator's working
    return a + b

print(log_running_function(2, 3))       # same
print(log_running_function(5, 9))
print(log_running_function(2, 3))       # same
















