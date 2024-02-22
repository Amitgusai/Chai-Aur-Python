
# virtualenv : Virtual Environment 
# General understanding : It is as almost a different computer within your system which contains python 

# These packages will be isolated within the my_env and won't affect your system-wide Python installation.


# How to install modules form requirement from requirement.txt



# 1. Install virtualenv:
    
# pip install virtualenv



# 2. Create your environment:
    
# Open a command prompt and navigate to the desired location for your project.
# Run the following command to create a virtual environment named my_env:
    
# virtualenv <my_env>



# 3. Activate the environment:

# Navigate to the Scripts subdirectory of your created environment:

# Open command prompt from the subdirectory and Run Command:
    
# .\<my_env>\Scripts\activate                                       <my_env> : file name(.venv)



# If Problem raised: 
    
# PowerShell's execution policy, which is preventing you from running scripts. 
# This is a security feature in PowerShell to prevent unauthorized scripts from running on your system.

# You can change the execution policy using the Set-ExecutionPolicy: 

# Open PowerShell as an administrator.

# Run the command:

#                     Set-ExecutionPolicy RemoteSigned or                 RemoteSigned requires that all scripts and configuration files downloaded from the internet are signed by a trusted publisher, while 
#                     Set-ExecutionPolicy Unrestricted.                   Unrestricted allows all scripts to run.



# 4. Install packages:

# While the environment is activated, use pip to install necessary packages:
# pip install <package_name>

# These packages will be isolated within the <my_env> and won't affect your system-wide Python installation.



# 6. Deactivate the environment:

# When finished, deactivate the environment to return to your system's Python:
# deactivate    (Inside --> .venv)



# 7.Some Commands:

# pip list : show the list of installed modules

# pip list




# 8. Remove the environment (optional):

# If you no longer need the environment, delete its directory:
# del /f /q my_env








