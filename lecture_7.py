# ...................................................                    Strings



# ..................................                Basics

# >>> chai = "lemon"
# >>> chai
# 'lemon'

# >>> print(chai)
# lemon

# >>> chai = "masala chai"

# >>> first_char = chai[0]                                              As strings are somewhat treated as List
# >>> print(first_char)
# m





# ..................................                 Slicing 


# >>> char = chai[:6]                                                   As starting with 0 so end part not included
# >>> char    
# 'masala' 

# >>> char = chai[1:6]
# >>> char
# 'asala'

# >>> char_1 = chai[:]
# >>> char_1
# 'masala chai'

# >>> num_list = "0123456789"
# >>> num_list[:]
# '0123456789'

# >>> num_list[0:7]
# '0123456'

# >>> num_list[0:-3]
# '0123456'

# >>> num_list[-2:-5]
# ''

# >>> num_list[0:8:2]                                                    3rd indicates : Hopping (skipping 2 places)
# '0246'

# >>> num_list[0:9:3]
# '036'





# .....................................                       Methods

# >> chai = 'Masala Chai'
# >>> chai
# 'Masala Chai'

# >>> print(chai.lower())                                                    lower() : Lower-Case
# masala chai

# >>> print(chai.upper())                                                    upper() : Upper-Case
# MASALA CHAI

# >>> chai                                                                   Actually reference doesn't change as string is immutable
# 'Masala Chai'

# >>> chai = "    Masala Chai    "                                           In web development, in input field suppose by unknowingly user type space, so striping is preferred.
# >>> chai
# '    Masala Chai    '
# >>> print(chai.strip())                                                    strip() : Removes all Unwanted space in string
# Masala Chai

# >>> chai = 'lemon chai'
# >>> print(chai.replace('lemon', 'ginger')                                  replace() : replaces a part of string with another string.
# ginger chai

# >>> chai                                                                   Same : Actual Reference doesn't change.
# 'lemon chai'

# >>> print(chai.replace('chai', 'tea'))
# lemon tea

# >> chai = "masala tea"
# >>> print(chai.find("tea"))                                                find() : string starting
# 7

# >>> print(chai.find("chai"))                                                 
# -1                                                                         If nothing found : -1 return as default Value

# >>> chai = "ginger chai chai chai chai"
# >>> print(chai.count("chai"))                                              No. of repeated string
# 4

# >>> chai = "lemon"
# >>> print(len(chai))                                                       no. of characters in a string
# 5





# .................................                   Conversion


# Converting string to list:                                                  .split()


# >>> chai = "Lemon, masala, mint, ginger"

# >>> print(chai.split())                                                     Default
# ['Lemon,', 'masala,', 'mint, ', 'ginger']

# >>> print(chai.split(", "))                                                 Mentioning exception (not included)
# ['Lemon', 'masala', 'mint', ginger']


# Converting List to String:                                                  "".join()
 

# >>> chai_list = ["lemon", "masala", "ginger"]   

# >>> print("".join(chai_list))                                                 Default
# lemonmasalaginger

# >>> print(" ".join(chai_list))                                                Mentioning or adding something to be more readable
# lemon masala ginger

# >>> print("-".join(chai_list))
# lemon-masala-ginger





# .................................                       Variables in String

# >>> coffee = "latte"
# >>> quantity = "4"

# >>> order = "I ordered {} cups of {} coffee"                                    {} : Placeholder (can place variables in it)
# >>> print(order)
# I ordered {} cups of {} coffee

# >>> print(order.format(quantity, coffee))                                       format() : places other variables in order
# I ordered 4 cups of latte coffee






# ...................................                   UNICODE ESCAPING


# >>> chai = r"Masala\nchai"                                                        Raw String indication
# >>> print(chai)
# Masala\nchai

# User: Windows Path

# Windows ke forward slash : '\' create many problems for windows path.                                     Important
# because '\' is a unicode character, so we use unicode escapes like r"" and \"                     

# Example: 

# >>> chai = "c:\user\pwd"
#   File "<stdin>", line 1
#     chai = "c:\user\pwd"
#                         ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

# Solution:     
    # >>> chai = r"c:\user\pwd"
    # >>> print(chai)
    # c:\user\pwd
    
    
    # >>> Speaker = "He said, \"masala chai is awesome\". "
    # >>> print(Speaker)
    # He said, "masala chai is awesome".


# >>> chai = r"c:\computer\mingw\"                                                   Problem arising at '\' at the last of string
#   File "<stdin>", line 1
#     chai = r"c:\computer\mingw\"
#            ^
# SyntaxError: unterminated string literal (detected at line 1)   

# Solution:
    # >>> chai = r"c:\computer\mingw"
    # >>> print(chai)
    # c:\computer\mingw




# ........................................                     Questioning in Strings

# >>> chai = "masala chai"
# >>> print("masala" in chai)
# True

# >>> print("coffee" in chai)
# False


