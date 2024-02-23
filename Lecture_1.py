# .................................         Inner Workings of Python


# To import from another file chai.py
from chai import tea

tea("Lazy")

# Usually the byte code(runs faster) is hidden from the developer BUT 
# when we 'import' files or code from 'another file' then it is visible

# cpython (default) : It uses and is a standard version of python (python = cpython)

# 311 : Version name 

# __pycache__ : To Organisize the files : .pyc {compiled (to byte cod)e : Technical term} for readibility



# .......................            Python Virtual Machine 

# Code is looped to iterate byte code 
# also known as python interpreter 
# run-time engine

# Byte Code (instruction specific to Python Virtual Machine) is not a machine code (It does not directly instruct to Hardware) 

# Yes, your statement is correct. Bytecode, such as that used in the Java Virtual Machine (JVM) or Python Virtual Machine (PVM), is not the same as machine code. 
# Bytecode is a form of instruction set designed for efficient execution by a software interpreter, in this case, the JVM or PVM. 
# On the other hand, machine code is a computer programming language that is directly understood by the computer's hardware. 
# It is a series of binary instructions that the computer's processor can execute directly