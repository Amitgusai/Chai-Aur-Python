# ...................................................         Decorators in Python


# A decorator is a function that takes another function as input/parameter and extends its functionality without modifying its code.
# Decorators in Python are like tollbooth for functions, adding functionality without changing the original function.


# Most Basic Decorator Syntax: 
    
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
    def wrapper(*args, **kwargs):                                                                                       # args is a tuple of positional arguments passed to a function
                                                                                                                        # kwargs is a dictionary of keyword arguments passed to a function.
        ans = func(*args, **kwargs)                                                                                     
                                                                                                                        
                                                                                                                        # To access values of the arguments :-
                                                                                                                        
        args_value = ', '.join(str(args) for args in args)                                                              # 1. --> The comprehension iterates over the elements of args, kwargs and str(args) : converts each element to a string.
        kwargs_value = ', '.join(f"{key}:{value}" for key, value in kwargs.items())                                     # 2. --> join() : The join() function concatenates a list of strings into a single string, with a specified separator between each string.
                                                                                                                        
        
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




# ............................................................            3. Cache Return Value         (main point : args is of tuple type)


#  It stores the results of function calls in a dictionary to avoid redundant computations when the same arguments are passed to the function again.

import time

def cache(func):                                                                                                        
    
    cache_value = {}                                                                                                    # should be written outside the wrapper funciton and storing the result
                                                                                                                        # dictionary : In this accessing values are easy as compared to list(because of indexing in list)
    def wrapper(*args, **kwargs):
        
        # print(cache_value)                                                                                            # Rough
        
        if args in cache_value:                                                                                         # Inside the wrapper, this line checks if the input arguments (*args) are present in the cache_value dictionary. 
                                                                                                                        # If they are, it means the function has been called with those arguments before, 
            return cache_value[args]                                                                                    # so it returns the cached result (value) from the dictionary.
                                                                                              

        
        num = func(*args, **kwargs) 
        cache_value[args] = num                                                                                         # cache_value[args] = num: This line adds the input arguments (*args) as the 'key' and the result (num) as the 'value' to the cache_value dictionary. 
                    # key = value  pair                                                                                 # This stores the result for future reference.

        
        return num
    
    return wrapper

@cache
def log_running_function(a, b):
    time.sleep(4)                                                                                                       # To better understand the decorator's working
    return a + b

print(log_running_function(2, 3))       # same
print(log_running_function(5, 9))
print(log_running_function(2, 3))       # same


