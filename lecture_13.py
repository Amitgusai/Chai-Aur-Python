# ..............................................            Behind the Scene of Loops




# Iterate  ==  loop (same)


# ....................................................            Important           ...............................................




# 1.

# Iteration Tools: for, while, comprehension
# only applicable on objects which are iterable
# tools query to iterable objects to allow looping: iter() method send hoti hai
# when iter tool receives __next__ or next() as a response: jitne baar next() karte hai utni values print/use hogi
# At final index/value empty(out of range): Stop_Iteration - Exception raise hoga
# Iterable tools are pre-pragrammed how to read file and handle StopIteraiton Exception


# 2.

# Iterable Object: list, file etc. 
# Objects which allow iteration or looping in it.
# iter objects responses by returning __next__
# Iterable object point at the start from where continuous memory allocation starts + __nest__


# 3.

# __next__
# it symbolisies that more values still exist karti hai





# ....................................................            Iteration in File           ............................................




# Using chai.py file

# readline() :    Implemented within python.(making it easy to handle exception - '')


# >>> f = open('chai.py')                                                   Assigning a Variable : Opening any file

# >>> f.readline()
# 'print("Chai Aur Code")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# def = definations (functions)\n'
# >>> f.readline()
# 'def tea(n):\n'
# >>> f.readline()
# '    print(n)\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'tea("WorkOut")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# ''                                                                        End of Our Code: '' (representation)




# __next__():   Raw method    (Python's internal working)



# >>> f.__next__()                                                           Using __next__(): Internal Working of Python
# 'print("Chai Aur Code")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# '# def = definations (functions)\n'
# >>> f.__next__()
# 'def tea(n):\n'
# >>> f.__next__()
# '    print(n)\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'tea("WorkOut")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration                                                                 StopIteration   (exception) : as it is a representation of python inner working




# 1. Using For loop:                                                            Iterable tools are pre-pragrammed how to read file and handle StopIteraiton Exception


# >>> for read in open('chai.py'):                                              Loop to iterate a file
# ...     print(read, end='')                                                   end='' : no extra new line       
# ...
# print("Chai Aur Code")

# # def = definations (functions)
# def tea(n):
#     print(n)

# tea("WorkOut")                                                                This is the ending




# 2. Using While Loop:



# >>> f = open('chai.py')
# >>> while True:
# ...     line = f.readline()
# ...     if not line:                                                            not(a keyword): Handling empty lines
# ...             break
# ...     print(line,end = '')
# ...                                                                             Iterable tools are pre-pragrammed how to read file and handle StopIteraiton Exception
# print("Chai Aur Code")

# # def = definations (functions)
# def tea(n):
#     print(n)

# tea("WorkOut")




# //////////////////////////////////////////////

# Use of 'not'                                                                    Checking variable empty or not (true or false)

# >>> if "amit" not in test:
# ...     print("NO")
# ...
# >>> test = ""
# >>> if not test:
# ...     print("amit")
# ...
# amit





















