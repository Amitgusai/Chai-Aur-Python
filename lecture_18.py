# ..........................................................              Python Project - Youtube manager app



# >>> x = ("masala", "coffee", "comment")                                                              # enumerate : all values using enumerate can be converted into list in key-value pair
# >>> y = inumerate(x)
# <enumerate object at 0x000002494E23C220>
# >>> list(y)
# [(0, 'masala'), (1, 'coffee'), (2, 'comment')]                                                       # key:value - pair



# //////////////////

file = open('youtube.txt', 'w')                                                                         # 'w' - write mode : file not there then it will create a new file
                                                                                                        # # File Handling:  Code, Cautious interaction with database of files
try:
    file.write('chai aur code')                                                                         # The `try` block is used to execute the code that may raise an exception, if exception occurs the 'finally' block will always be executed
finally:
    file.close()                                                                                        # proper file handling(closing) to ensure that resources are released correctly.



with open('youtube.txt', 'w') as file:                                                                  # Better way of handling file operations in python
    file.write('chai aur python')                                                                       # 'with' : ensures that the file is properly closed even if an exception occurs


# //////////////////



















