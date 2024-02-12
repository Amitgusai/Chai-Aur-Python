# .................................................           Loops



# .....................................             Questions on Loops          ..........................


                                                        # 1. Counting Positive Numbers

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count = 0

# for num in numbers:
#     if num > 0:
#         count = count + 1
# print("Positive numbers:",count)                                                   All it matter is indentation




                                                        # 2. Sum of Even Numbers

# number = int(input("Value of n: "))
# sum = 0

# for i in range(1, number+1):                                                        i for iteration (To not include 0)
#     if i % 2 == 0:
#         sum = sum + i

# print("Sum of all even numbers: ",sum)



                                                        # 3. Multiplication Table Printer


# number = int(input("Given Nunber: "))
# print("Multiplication Table: ")

# for i in range(1, 11):
#     if i == 5:
#         continue                                                                         continue: skipping 1 iteration
#     print(number, 'x', i, '=', number * i)



# Revision

    
# variable = "amit" 
# var = "gusai"
# order = "My first_name is {} and sur_name is {} "

# print(order.format(variable, var))





                                                        # 4. Reverse a String 

# string = "python"
# reversed_string = ""
# num = 1

# for char in string:                                                                        2 methods to solve
#     print(string[-num])
#     num = num + 1

# for char in string:
#     reversed_string = char + reversed_string

# print(reversed_string)




                                                        # 5. Find the Non-Repeated character

# string = "ranveer allabadiya run"

# for char in string:
#     non_repeat = string.count(char)                                                         character count in string
#     if non_repeat == 1:
#         print("First non_repeated character:",char)
#         break                                                                               break: exiting from loop          




# .................................................             while loop  




                                                        # 6. Factorial Calculator


# num = 5
# factorial = 1

# while num > 0:
#     factorial = factorial * num
#     num -= 1                                                                               SHOTCUT 

# print("Factorial:",factorial)




# # 7. Validate Input 



# while True:    
#     number = int(input("num: "))             
#     if (number >= 1 and number <= 10):
#         print("Processing...")
#         break                                                                                  As we are using while loop (True), so break statement in use
#     else:
#         print("Please give numbers between 1 to 10")
        
        
        
        

                                                        # 8. Prime Checker

    
        









