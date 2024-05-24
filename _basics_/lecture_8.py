# ....................................                  List


# .......................................                       Basics:


# >>> tea_varieties = ["black", "green", "masala", "ginger"]
# >>> print(tea_varieties)
# ['black', 'green', 'masala', 'ginger']
# >>> print(tea_varieties[0])
# black
# >>> print(tea_varieties[-1])                                            mostly used as len() - any_number
# ginger


# Slicing in List:

    # >>> print(tea_varieties[:3])  
    # ['black', 'green', 'masala']
    # >>> print(tea_varieties[1:3])
    # ['green', 'masala']
    # >>> print(tea_varieties[0:3:2])
    # ['black', 'masala']
    # >>> tea_varieties[3]
    # 'ginger'




# ....................................                    Insertion throught slicing method

# >>> tea_varieties[3] = "Herbal"                                           Updating list values as list are mutable

# >>> print(tea_varieties)
# ['black', 'green', 'masala', 'Herbal']          

# >>> tea_varieties
# ['black', 'green', 'masala', 'herbal']


# >>> tea_varieties[1:2] = "lemon"                                            As it being treated as an Array
# >>> print(tea_varieties)
# ['black', 'l', 'e', 'm', 'o', 'n', 'masala', 'herbal']                      Not intended to do this
# >>>



# >>> tea_varieties = ["black", "green", "masala", "herbal"]
# >>> print(tea_varieties)
# ['black', 'green', 'masala', 'herbal']


# >>> tea_varieties[1:2] = ["lemon"]                                          So, Passing it as an Array
# >>> print(tea_varieties)
# ['black', 'lemon', 'masala', 'herbal']


# >>> tea_varieties = ["black", "lemon", "oolong", "herbal"]
# >>> tea_varieties[1:3]
# ['lemon', 'oolong']

# >>> tea_varieties[1:3] = ["green", "masala"]                                Updating multiple Value in list
# >>> print(tea_varieties)
# ['black', 'green', 'masala', 'herbal']


# ........................................                Tricky


# >>> tea_varieties = ['black', 'lemon', 'oolong', 'herbal']
# >>> print(tea_varieties)
# ['black', 'lemon', 'oolong', 'herbal']
# >>> tea_varieties[1:1]                                                      1 se start and 1 ko exclude
# []
# >>> tea_varieties[1:1] = ['test', 'test']
# >>> print(tea_varieties)
# ['black', 'test', 'test', 'lemon', 'oolong', 'herbal']                       New indexing
# >>> tea_varieties[1:3] = []                                                  insert nothing : deleting values 
# >>> print(tea_varieties)
# ['black', 'lemon', 'oolong', 'herbal']





# ..............................                              Methods in Syntax



#  >>> tea_varieties = ['black', 'green', 'oolong', 'ginger']
# >>> tea_varieties.append('masala')                                            append() :Adding at the last in list
# >>> print(tea_varieties)
# ['black', 'green', 'oolong', 'ginger', 'masala']

# >>> tea_varieties.pop()                                                       pop() : Removes last value in list
# >>> 'masala'
# >>> print(tea_varieties)
# >>> ['black', 'green', 'oolong', 'ginger']


# >>> tea_varieties.remove('green')                                             remove(): Removes specified value in list
# >>> print(tea_varieties)
# ['black', 'oolong', 'ginger']


# >>> tea_varieties = ['black', 'green', 'oolong', 'ginger']                    del : Remove based on Indexing in list
# >>> tea_varieties
# ['black', 'green', 'oolong', 'ginger']
# >>> del tea_varieties[1]
# >>> tea_varieties
# ['black', 'oolong', 'ginger']


# >>> tea_varieties
# ['black', 'oolong', 'ginger']
# >>> tea_varieties.insert(1, "black")                                          insert() : Inserting value in list (mentioning two arguments: index position , insert value)
# >>> tea_varieties
# ['black', 'black', 'oolong', 'ginger']


# >>> tea_varieties_copy = tea_varieties.copy()                                 New Reference for tea_varieties_copy
# >>> tea_varieties_copy == tea_varieties                                       Values are same 
# True
# >>> tea_varieties_copy is tea_varieties                                       Reference is different
# False   





# ....................................                    List comprehension : Calculation inside a list



# >>> squared_nums = [x**2 for x in range(10)]                                  range from 0 to 10
# >>> print(squared_nums)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]                                          Loops ka hi systax
# >>> print(range(10)) 
# range(0, 10)

# >>> cube_nums = [y**3 for y in range(5)]
# >>> print(cube_nums)
# [0, 1, 8, 27, 64]






