# .........................................................................               Function question





# .................................................                 1. Basic Function Syntax


# function(defination)    :   def 

# def square(number):                                                  #parameters : placeholders
#     ans = number ** 2
#     return ans

# ans = square(4)                                                             #arguments
# print(ans)




# .....................................................             2. Function with Multiple Parameters



# def sum(num1, num2):
#     add = num1 + num2
#     return add

# result = sum(4, 5)
# print(result)



# ........................................................              3. Polymorphism in Function (same thing --> different behaviour --> different situations)



# Polymorphism is handled by python internally

# def multiply(para1, para2):
#     multiply = para1 * para2
#     return multiply

# ans = multiply("and", 4)
# ans1 = multiply(3, 5)
# print(ans , ",", ans1)




# ..........................................................            4. Function Returning Multiple Values




# def radius(radius):
#     area = 3.14 * radius ** 2
#     circumferance = 2 * 3.14 * radius
#     return area, circumferance                                        Can return two values, list etc.

# a, b = radius(4)
# print(a, ",", b)


# How to make it to only two decimal places:                            HOMEWORK



# ..........................................................            5. Default Parameter Value:




# def greet(name = "default value"):                                     # This is a default value if no arguments is passed to the Function def
#     return "Hello, " + name + "!"
    
# ans = greet()
# print(ans)



# ........................................................              6. Lambda Function



                                                                                # lambda function : functions with no name [Directly function likh sakte hai single line]
                                                                                # useful when a functions working is not multiple times in a code
                                                                                
# cube = lambda x:x ** 3                                                        # First x : parameter 
                                                                                # second x ** 3 : code working
                                                                                # This definition of lambda cannot be stored in another variable (Reference can)
                                                                                
# print(cube(3))                                                                # cube is storing a lambda function in itself

                                                                                # Use of lambda in python frameworks (more)




# ..........................................................            7. Function with *args ('*' : Ashtrick)



# def sum_all(number):
#     sum = 0                                                                    # Loop in funtion
#     for i in number:
#         sum = sum + i
#     return sum 
    

# print(sum_all([1, 2, 5]))                                                      # passing it as an Array
# print(sum_all([1, 2, 3, 4, 5, 5]))
# print(sum_all([8, 6, 5, 4, 14, 5]))


                                            # In python : *args


# def sum_all(*args):                                                             # '*' : Multiple Arguments can be handled [args(good practice) can be replaced but not '*']
#     print(args)                                                                 # Tuple format
#     for i in args:
#         print(i * 2)
#     return sum(args)                                                            # sum() : Default method to add
 

# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5, 5))
# print(sum_all(8, 6, 5, 4, 14, 5))





# .........................................................           8. Function with **kwargs



# def print_kwargs(**kwargs):                                                       # '**' : key value in pair ['*' : does not recongnize the named arguments]
#     for key, value in kwargs.items():
#         print(key, value)
    
# print_kwargs(name = "amit", power = "inner_thoughts")                             # Named Arguments
# print_kwargs(name = "amit")
# print_kwargs(name = "amit", power = "inner_thoughts", weak = "understading")




# ..............................................................          9. Generator Function with yield 




# def even_generator(limit):                                                                   # We can also use an empty list to solve this
#     for i in range(2, limit + 1, 2):                                                         # 2 is not inclusive : it only skips 1 value (as we needed even numbers ony)
#         yield i                                                                              # yield : Also returns value 'but' also saves previous state of variable 'i' in memory and performs the next tasks with it's previous state in mind every single time a function is called
    
    
# for num in even_generator(10):
#     print(num)


# how is it now iterable, why? : range() is iterable




# ...............................................................             10. Recursive Function 



                                                                                                # Exit check karo in Recursion 
# def factorial(n):                                                                             # Indinite loop
#     return n * factorial(n-1)

                                                    # This is Recursion -->
                                                    
# def factorial(n):                                                                             # Behind the scene a tree is forming (for understanding)
#     if n == 0:                                                                                
#         return 1                                                                              # Exit strategy sochni hai in Recursion
#     else:
#         return n * factorial(n-1)


# print(factorial(5))
