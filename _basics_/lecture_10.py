# ..............................................                Tuples

# List is mutable but 
# Tuple is Immutable (References changes but the value remains the same)                                  enhancing performance




# ..........................................                    Basics : Same as list       (Not much to read)


# >>> chai_type = ("black", "green", "ginger", "hot_coffee")
# >>> print(chai_type)
# ('black', 'green', 'ginger', 'hot_coffee')

# >>> chai_type[0]
# 'black'
# >>> chai_type[-1]
# 'hot_coffee'
# >>> chai_type[1:]
# ('green', 'ginger', 'hot_coffee')


# >>> chai_type[0] = "lemon"                                                 As it is Immutable (Reference may change but value in a reference never)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment




# Adding Tuples: 


# >>> herbal = ("masala", "coffee", "shilong")
# >>> all_tea = chai_type + herbal_tea                                          Adding in sequence
# >>> print(all_tea)
# ("black", "green", "ginger", "hot_cofee", "masala", "coffee", "shilong")


# Questioning: 

# >>> if "green" in all_tea:
# ...     print("green tea is spicy")
# ...
# green tea is spicy


# method: 

# >>> more_type.count("herbal")                                                 count() : mentioning the value to count
# 0
# >>> more_type.count("black")
# 1





# ............................................                   Database se tuple return karna is very common 


# >>> tea_type = ("black", "hot", "green")                                       Outside Tuple
# >>> print(tea_type)
# ('black', 'hot', 'green')

# >>> (black, coffee, light) = tea_type                                          Treating them as Variables : storing outside tuple (Number count of value must be same)

# >>> print(black)                                                               Accessing them through Variables: 
# black
# >>> print(coffee)
# hot
# >>> print(light)
# green



# >>> type(tea_type)                                                            type operator: name the type of data used
# <class 'tuple'>

# Nested tuple: 
    
# >>> nest = ("masala", ("1", 3, 4, 5), "hot")                                  tuple >> tuple (tuple inside tuple possible)
# >>> print(nest)
# ('masala', ('1', 3, 4, 5), 'hot')




