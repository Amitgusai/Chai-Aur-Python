#   ......................................          Numbers


# ...................................                  Basics: 

# >>> x = 2
# >>> y = 3
# >>> z = 4
# >>> x+y
# 5

# >>> 84 + 4.29                                                                    Higher Value data type takes priority
# 88.29


# >>> 'amit' + 12                                                                   Operations only on Similar Data types can be Performed

# >>> int(34.5453)                                                                  Type Conversion   
# 34
# >>> float(13)
# 13.0

# >>> 'chai' + ' aur' + ' Code'                                                      Concactination(string adding)
# 'chai aur Code'

# >>> x, y, z
# (2, 3, 4)                                                                          Tuple 
# >>> y % 2                                                                           Modula (Remainder find out)
# 1

# >>> 100 * 2
# 200
# >>> 5 ** 100
# 7888609052210118054117285652827862296732064351090230047702789306640625              Indinite Handling Precision (only in Python)


# Read about them: 

# >>> repr('code')
# "'code"
# >>> str('code')
# code
# >>> print('code')
# code


# Complex Numbers:
    
    # >>> 2 + 3j
    # >>> (2 + 3j) * 2
    # (4+6j)
    






# ...............................               Tricky Problems:

# >>> x, y, z 
# (2, 3, 4)
# >>> x < y < z                                                     Simply means: x < y and y < z 
# True                                                              In case of 'and' : both satisfied then 'true'
# >>> 1 == 5
# False
# >>> 1 == 1
# True
# >>> 1 == 4 < 9
# False






# ................................                  Math Module:

# >>> import math 

# >>> math.floor( 3.9)                                      Closest Bottom Value
# 3
# >>> math.floor(-3.1)
# -4
# >>> math.trunc(3.5)
# 3
# >>> math.turnc( -3.9)                                     Closest Towards 0
# -3
    
    
    
    


# ...................................               Random Module:

# Random.random():

    # >>> import random                                             Gives random Values(generally 0 - 1 decimals)
    # >>> random.random()
    # 0.2291063031490974
    # >>> random.random()
    # 0.29116266419933856

# Random.choice():
    
    # >>> l1 = [2,3,4,5,12]
    # >>> random.choice(l1)                                            Random Values among the option choices in the List
    # 5
    # >>> random.choice(l1)
    # 3
    # >>> random.choice(li)
    # 12


# Random.randint():

    # >>> random.randint(4,100)                                         Range have to be mentioned
    # 86                                                                Gives Random Values but only Integers
    # >>> random.randint(4,100)
    # 35
    # >>> random.randint(4,100)
    # 67


# Random.Shuffle():                                               
    
    # >>> li = [1,2,3,4,5,6,7]
    # >>> random.shuffle(li)
    # >>> li
    # [1, 5, 2, 7, 4, 6, 3]                                             Shuffles values each time runs
    # >>> li
    # [1, 5, 2, 7, 4, 6, 3]
    # >>> random.shuffle(li)
    # >>> li
    # [7, 2, 5, 3, 1, 6, 4]
    
    




# ..............................                    Some Literals Methods: 

# >>> oct(12)                                                                     Octal Literals(base 8)
# '0o14'                                                                          starts : 0o
# >>> bin(90)                                                                     Binary Literals(base 2)
# '0b1011010'                                                                     starts : 0b
# >>> hex(12)                                                                     Hexadecimal Literals(base 16)
# '0xc'                                                                           starts : 0x

# >>> int('28', 8)                        
# Traceback (most recent call last):                                              Error : 28 not of base 8
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 8: '28'

# >>> oct(28)                                                                     Preferred : Methods                                             
# '0o34'
# >>> 0o34
# 28







# .............................                 Decimal Type: 

# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004                                            Python Short-comings
# >>> 0.1 + 0.1 + 0.1 - 3.0
# 5.551115123125783e-17


# >>> from decimal import Decimal

# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') + Decimal('0.3')
# Decimal('0.6')                                                                        Precise Representation of Decimal Numbers
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')                                                                        Expected Results







# ...............................                Fraction Type :

# >>> from fractions import Fraction

# >>> myfra = Fraction(1,4) + Fraction(1,4)                         Precise Represenration of Rational Numbers
# >>> print(myfra)







# ................................             Boolean Example :

# >>> type(True)                                   type operator - tells data type
# <class 'bool'>
# >>> True == 1
# True
# >>> False == 0
# True
# >>> True is 1                                     Reference is different in memory
# False






# ................................                  Sets:

# >>> set1 = {1,2,3,4,5}                                              Not similar to Dictionary as they have Key:Value pair
# >>> set2 = {2,5,7,8}
# >>> set1 and set2                                                   Intersection  (Similar in Both)
# {2,5}
# >>> set1 or set3                                                    Union (Unique(Excluded similar))
# {1,3,4,7,8}



