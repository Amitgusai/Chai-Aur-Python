# ....................................................          Inner Working of Python         ..........................................


# . In Python, all data types are objects.

# Any or all data ka type in python relates to memory not to the variable
# which is why:
# Python does not have any data type (variable ka koi data type nahi hai)
# But:
# Memory me reference ka data type hota hai And memory me data ka type assign hota hai.


# Example:                          _IMP_
#     a = 5
#     a ka data type kya hai : nothing
#     5 ka data type : Number data type/object type 



# refcount: No particular method to find reference as such written on some documents
# Actually : Internally a compiler optimisation ka loop chal jata hai
# which give the same value for refcount
# we can find refcount using other methods like pointers etc. 



# Python treats Strings and Numbers differently:
#     No Immediate Garbage Collection
#     Late garbage collection in case of String and Numbers for optimization as it can be used further in the program..



#   .....................................       __Most Important__      .....................................


# In List:
    # In Python, when you declare a list, it's stored in a specific location in memory. T
    # his location is what we refer to as the reference of the list. Even if two lists have the same values, they are stored in different memory locations, hence they have different references.
    
# Why?
    # This is because Python lists are mutable, meaning their contents can be changed after they are created. 
    # So, each list needs its own unique location in memory where its contents can be modified independently of any other list


# Example: 

# >>> l1 = [1,2,3]        First Reference
# >>> l2 = l1
# >>> l1 == l2
# True
# >>> l1 is l2
# True
# >>> l1 = [1,2,3]        New Reference Created [Second]
# >>> l1 == l2            Checking "Values" are similar of both list
# True
# >>> l1 is l2            Checking "Reference" have similar object in both list
# False
# >>> l1[0] = 99          Changes in Second Reference
# >>> l1
# [99, 2, 3]
# >>> l2                  No impact on First Reference
# [1, 2, 3]


#   ...........................       __EXtras__      ............................

# >>> h1 = [1,2,3]
# >>> h2 = h1[:]            Creating a Copy (Whenever Slicing is done)
# >>> h1
# [1, 2, 3]
# >>> h2                    Copy of h1
# [1, 2, 3]
# >>> h1 == h2
# True
# >>> h1 is h2              Both Reference are Different
# False

# Copy:
# import copy
# h2 = copy.copy(h1)
