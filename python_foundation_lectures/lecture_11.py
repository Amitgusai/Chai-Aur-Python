# ............................................                Conditionals




# .....................................               Input from User


# >>> age_count = input("age taken: ")
# age taken: 45
# >>> print(age_count)
# 45
# >>> print(age_count * 2)
# 4545                                                                                By default : input() take value in string data type
# >>>




# >>> age_count = int(input("Age of an Individual: "))                                Specified the data type (Number)
# Age of an Individual: 45
# >>> print(age_count)
# 45
# >>> print(age_count * 2)
# 90
# >>> print(age_count)
# 45





# ......................................................................                    Questions on Conditionals:              ......................................................



                                                            # 1. Age Group Categorization

# person_age = int(input("User_age: "))

# if person_age <= 12: 
#     print("child")
    
# elif (13 <= person_age <= 19): 
#     print("Teenager")
    
# elif (20 <= person_age and person_age <=59):
#     print("Adult")
    
# else:
#     print("Senior")




                                                            # 2. Movie Ticket Pricing

# user_age = int(input("age: "))
# day = input("day: ")

# price = 12 if user_age >= 18 else 8                                                     important_note: Python specific syntax

# if day == "Wednesday":
#     price = price - 2
    
# if user_age >= 18: 
#     print("Adult ticket: $",price)
# else:
#     print("Child ticket: $",price)


                                                                # 3. Grade  Calculator

# student_score = int(input("Marks obtained: "))

# if student_score >=101:
#     print("Please verify your grade again")
#     exit()                                                                              exit(): Exiting a python code (break: only used in Loop) 
    
# if student_score >= 90:
#     Grade = "A"
# elif student_score >=80:
#     Grade = 'B'
# elif student_score >= 70:
#     Grade = 'C'
# elif student_score >= 60:
#     Grade = "D"
# else:
#     Grade = "F"
    
# print("Grade:",Grade)



                                                                # 5. Fruit Ripenss Checker

# fruit = input("name of fruit: ")
# color = input("color: ") 

# if fruit == "banana":                                                                   checking if fruit is banana
#     if color == "green":
#         print("Banana is Unripe")
#     elif color == "yellow":
#         print("Banana is Ripe")
#     else:
#         print("Banana is Overripe")
# else:
#     print("No information")



                                                                # 5. Weather Activity Suggestion

# weather = input("weather: ")

# if weather == "Sunny":
#     print("Come on, go for a walk you lazy bum")
# elif weather == "Rainy":
#     print("Read a book, smarty")
# elif weather == "Snowy":
#     print("Ya hoo! let's build a snowman")
# else:
#     print("Wait No information was Broadcast, sorry for inconvinience")




                                                                    # 6. Transportation Mode Selection

# distance = int(input("Distance in Km: "))

# if distance < 3:
#     mode = "Walk"
# elif 15 > distance > 3:
#     mode = "Bike"
# else:
#     mode = "Car"

# print("Mode of Transportation is:",mode)



                                                                            # 7. Coffee Customization

# order = input("order: ")

# if order == "large":
#     print("Do you like have a 'Extra shot' of espresso ?")
#     option = input("preference: ")
#     if option == "yes":
#         print(order + " coffee with an extra shot")
#     elif option == "no":
#         print("Ok")
#     else:
#         print("Please answer.")
        
# elif order == "medium":
#     print("Do you like have a 'Extra shot' of espresso ?")
#     option = input("preference: ")
#     if option == "yes":
#         print(order + " coffee with an extra shot")
#     elif option == "no":
#         print("Ok")
#     else:
#         print("Please answer.")
        
# else: 
#     print("Do you like have a 'Extra shot' of espresso ?")
#     option = input("preference: ")
#     if option == "yes":
#         print(order + " coffee with an extra shot")
#     elif option == "no":
#         print("Ok")
#     else:
#         print("Please answer.")



                                                                    # 8. Password Strength Checker

# password = input("Enter password: ")
# password_length = len(password)

# if password_length < 6:
#     Strength = "weak"
# elif password_length <= 10:
#     Strength = "Medium"
# else:
#     Strength = "Strong"
    
# print("Password Strength:",Strength)




                                                                        # 9. Leap Year Checker

# year = int(input("Current year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):                                       and: (both condition must be true)
#     print("It is a Leap Year")
#                                                                                                    or: (any one can be true)
# else:
#     print("It is not a Leap Year")
                                                                 
                                                                 
                                                                            

                                                                    # 10. Pet Food Recommendation

# pet = input("Pet species: ")
# age = int(input("age: "))

# if pet == "dog":
#     if age < 2:
#         print("Give puppy food")
#     else:
#         print("Give senior dog food")

# elif pet == "cat":
#     if age > 5:
#         print("Give senior cat food")
#     else:
#         print("Give baby cat food")



