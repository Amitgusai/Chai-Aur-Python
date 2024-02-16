# ............................................................            Scope     and     Closure         ..............................................



# when making function : think as creating a new house within memory 
# variable declared within function are 'Function' variables (Local-variables)

# All the other variables are 'Global' variables




# .............................................................           SCOPE



# username = "amit"
# def test():
#     username = "chai"                                                             # Global variable is applicable throught the python file
#     print(username)                                                               # username = "chai" : dead after function is completed (only applicable within the declared function)

# print(username)
# test()

# # //////////////////////////////////

# x = 99
# def func(y):
#     z = x + y                                                                       # here x value is replaced by global variables
#     return z

# ans = func(1)
# print(ans)

# # ///////////////////////////////////

# x = 99
# def func3():
#     global x                                                                          # Avoid using 'global' keyword
#     x = 88                                                                            # Don't override the value, only access it (not a reliable code)
    
# func3()
# print(x)




# ...........................................................             CLOSURE



# def f1():
#     x = 88 
#     def f2():
#         print(x)                                                                        # Climbing concept : rooms -> house -> global (variables)    
#     return f2                                                                           # f2 : definition return hora hai (reference)
#                                                                                         # f2() : this means execution
                                                                                        
# result = f1()                                                                           # Reference of f2
# print(result)                                                                           
# result()                                                                                # Closure : not only the defination of f2 but also references of all the variables associated or used with it are being send to result (ex : BackPack)



# //////////////////////////////////


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual                                                                           # returning definition of actual (Reference)

f = chaicoder(2)                                                                            # closure : 'f' contain the definition/reference of actual() function + BackPack -> reference of variables(num) used in it are also returned to 'f'
g = chaicoder(3)

print(f(7))                                                                                 # Argument given to the actual() function which is stored in f and g variable
print(g(5))                                                                                 # f and g are closure (function object)


