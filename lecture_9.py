# .........................................                     Dictionaries


# In dictionaries, order doesn't matter(ex: user_info) unlike list we create our own key (not a default : indexing).

# Key-Value pair    ---     Items

# List : key are not defined by developer
# Dictionaries : values as well as keys are defined by developer

# All data types in value can be assigned


# ....................................                      Basics



# Accessing values


# >>> chai_type = {"chai": "black", "name": "rajwari", "cups": 2}
# >>> print(chai_type)
# {'chai': 'black', 'name': 'rajwari', 'cups': 2}

# >>> chai_type["chai"]                                                   Key mentioned
# 'black'
# >>> chai_type["cups"]
# 2

# Method: 
    
#     >>> chai_type.get("name")                                           get() : To access dictionary
#     >>> 'rajwari'

# Updating:
    
# >>> chai_type = {"chai": "black", "name": "rajwari", "cups": 2}
# >>> chai_type
# {'chai': 'black', 'name': 'rajwari', 'cups': 2}
# >>> chai_type['name'] = 'rajasthani'                                    Inserting another key:value pair
# >>> chai_type
# {'chai': 'black', 'name': 'rajasthani', 'cups': 2}



# .....................................                   Loop in Dictionaries:                       
    
# >>> chai_type
# {'chai': 'black', 'name': 'rajasthani', 'cups': 2}
# >>> for n in chai_type:                                                   In dictionary, Iterate (result:keys)
# ...     print(n)
# ...
# chai
# name
# cups


# >>> for n in chai_type:
# ...     print(n,chai_type[n])                                              Printing values as well
# ...
# chai black
# name rajasthani
# cups 2



# >>> for n in chai_type:
# ...     print(n,chai_type[n],end = ":")                                     Specifying the Ending
# ...
# chai black:name rajasthani:cups 2:>>>


# >>> for key, value in chai_type.items():                                    items() : key-value ka pair
# ...     print(key, value)
# ...
# chai black
# name rajasthani
# cups 2




# ....................................              Quesioning: 

# >>> chai_type = {"masala": "spicy", "ginger": "mint", "green": "fresh"}

# >>> print(chai_type)
# {'masala': 'spicy', 'ginger': 'mint', 'green': 'fresh'}
# >>> if "masala" in chai_type:
# ...     print("It is spicy")
# ...
# It is spicy




# ........................................              Methods: 

# >>> print(len(chai_type))                                                     len() : no.of items(key:value pair)
# 3

# >>> chai_type.pop("masala")                                                   pop() : key must be mentioned as it is not in a sequential order.                      
# 'spicy'

# >>> print(chai_type)
# {'ginger': 'mint', 'green': 'fresh'}


# >>> chai_type = {'masala': 'spicy', 'ginger': 'mint', 'green': 'fresh'}

# >>> chai_type.popitem()                                                       popitem() : item(key:value) removed from last value in dictionary
# ('green', 'fresh')

# >>> print(chai_type)
# {'masala': 'spicy', 'ginger': 'mint'}

# >>> chai_type_copy = chai_type                                                A new Reference copy is created
# >>> chai_type_copy is chai_type                                               Reference are different
# True




# .......................................               Dictionaries   In   Dictionary


# >>> star_bucks = {                                              
# ... "coffee": {"masala": {"chai": "hot", "tea": "cold"}},                        Multiple dictionaries 
# ... "latte": {"cappichino": "good", "year": 23}
# ... }

# >>> print(star_bucks)
# {'coffee': {'masala': {'chai': 'hot', 'tea': 'cold'}}, 'latte': {'cappichino': 'good', 'year': 23}}


# Accessing:


# >>> star_bucks["coffee"]                                                         star_bucks(dictionary) accessing key(coffee) = result(dictionary)
# {'masala': {'chai': 'hot', 'tea': 'cold'}}

# >>> star_bucks["coffee"]["masala"]                                               star_bucks["coffee"](treating as whole variable) accessing key(masala)
# {'chai': 'hot', 'tea': 'cold'}

# >>> star_bucks["latte"]
# {'cappichino': 'good', 'year': 23}

# >>> star_bucks["latte"]["year"]                                                  Example
# 23
# >>> star_bucks["latte"]["cappichino"]
# 'good'





# ........................................                  Dictionary Comprehension (Calculation within Dictionary)


# >>> squared = {x:x**2 for x in range(5)}                                         key must be mentioned (To make key:value pair)

# >>> print(squared)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# >>> cube = {x : x++5 for x in range(10)}

# >>> print(cube)
# {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 11, 7: 12, 8: 13, 9: 14}






