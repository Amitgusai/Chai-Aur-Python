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

# //////////////////////////////////

# x = 99
# def func(y):
#     z = x + y                                                                       # here x value is replaced by global variables
#     return z

# ans = func(1)
# print(ans)

# ///////////////////////////////////

# x = 99
# def func3():
#     global x                                                                          # Avoid using 'global' keyword
#     x = 88                                                                            # Don't override the value, only access it (not a reliable code)
    
# func3()
# print(x)




# ...........................................................             CLOSURE



def f1():
    x = 88 
    def f2():
        print(x)                                                                        # Climbing concept : rooms -> house -> global    
    return f2               # f2 : definition return ki hai

result = f1()
# print(result)
result()



# //////////////////////////////////


def chaicoder(n):
    def actual(x):
        return x ** n
    return actual

f = chaicoder(2)
g = chaicoder(3)


print(f(2))
print(g(3))








