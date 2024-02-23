# .................................         Inner Workings of Python


# To import from another file chai.py
from chai import tea

tea("Lazy")

# Usually the byte code(runs faster) is hidden from the developer BUT 
# when we 'import' files or code from 'another file' then the byte code is visible
 

    """
    Compiled to byte code
    Works only on imported files
    """

# cpython (default) : It uses and is a standard version of python (python = cpython)

# 311 : Version name 

# __pycache__ : To Organisize the files : .pyc {compiled python file} for readibility

# .pyc : This compiled python is also known as 'Frozen Binaries'  
# But:


    """ 
    1. '.pyc' is a compiled python file that still requires the help of python interpreter to execute, meanwhile
    2.'Frozen Binaries' is a standclone executable file which includes both python application and python interpreter.
    """
    

# Byte code runs faster: mostly check of syntax are done when converting to byte code 

# .......................            Python Virtual Machine 

# Code is looped to iterate byte code : that's why python is interpreter language (as looping is done line by line)
# also known as python interpreter 
# run-time engine


    """ Byte Code (instruction specific to Python Virtual Machine) is not a machine code (It does not directly instruct to Hardware)."""


    """
    Bytecode, such as that used in the Java Virtual Machine (JVM) or Python Virtual Machine (PVM), is not the same as machine code. 
    Bytecode is a form of instruction set designed for efficient execution by a software interpreter, in this case, the JVM or PVM.
    """
    
    """
    On the other hand, machine code is a computer programming language that is directly understood by the computer's hardware. 
    It is a series of binary instructions that the computer's processor can execute directly.
    """