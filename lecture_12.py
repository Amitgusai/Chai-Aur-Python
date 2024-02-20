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
        
        
        
        


# ...........................................................               Important - 3Q           ............................................................



                                                                # 8. Prime Checker

    
        
# prime = int(input("Given Number: "))
# is_prime  = True

# if prime > 1:                                                           As prime numbers are positive
#     for n in range(2, prime):                                           range from 2 as 1 and value of prime can divide prime
#         if (prime % n == 0):
#             is_prime = False
#             break
    
# if is_prime is False:
#     print("Given number is Not Prime")
# else:
#     print("Given number is Prime")




#                                                       9. List Uniqueness Checker [2 methods used]


#                                                                   Method - 1 : Time Complexity -- O(n**2)

# items  = ["mango", "apple", "orange", "apple", "banana"]

# for i in range(len(items)):                                                # converting i from str to int using range
#     for j in range(i + 1, len(items)):
#         if(items[i] == items[j]):
#             print(items[i])
#             break
            

 

#                                                                   Method - 2 : Time Complexity -- O(n)    [Using : set()]


# unique = set()                                                              #set(): It only keeps unique value in it 
# print(unique)                                                               #set(): This is an Empty set

# for i in items:
#     if i in unique:                                                           
#         print("Duplicate:",i)                                               Duplicate found in unique 
#         break
#     else: 
#         unique.add(i)                                                       Adding list items in empty set() : unique
    
# print(unique)                                                               Added by above loop





#                                                               10. Exponential Backoff  (Real World Usage)


# Usage : Password, OTP [Increase wait time during retries]

# import time                                                                     #using time module

# wait_time = 1                                                                   #In seconds
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("Attempt:", attempts + 1, "wait_time:", wait_time)
#     time.sleep(wait_time)                                                       #time.sleep(//value): To sleep the system by given value
#     wait_time *= 2
#     attempts += 1



