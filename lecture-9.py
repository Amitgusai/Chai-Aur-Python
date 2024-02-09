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
# >>> chai_type['name'] = 'rajasthani'
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















