# Any or all data ka type in python goes to memory not in the variable
# which is why:
# Python does not have any data type
# But:
# Memory me reference ka data type hota hai And memory me data ka type assign hota hai.


# Example:                          _IMP_
#     a = 5
#     a ka data type kya hai : nothing
#     5 ka data type : Number data type/object type


# refcount: No particular method as such written on some documents


# Python treats Strings and Numbers differently:
#     No Immediate Garbage Collection
#     Late garbage collection in case of String and Numbers for optimization as it can be used further in the program..


#   .....................................       __Most Important__      .....................................

# In List:
#     A list even with Same Value assigned is still considered as of different Reference.
#     New Reference will be created in memory each time a list is declared/updated whether of same value or not.


# WHY?:
#     As list is not immutable whose reference can not be changed which is why can be assigned to others.
#     It is mutable i.e. So it's Reference can be changed which is why we cannot assign it to others.


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
# >>> l1 is l2            Checking "Reference" are similar of both list
# False
# >>> l1[0] = 99          Changes in Second Reference
# >>> l1
# [99, 2, 3]
# >>> l2                  No impact on First Reference
# [1, 2, 3]



