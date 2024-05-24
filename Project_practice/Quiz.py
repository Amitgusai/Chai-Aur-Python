import random
import math

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

x = random.randint(lower, upper)

count = 0

limit = math.log(upper - lower + 1, 2)          # Power of 2 is the limit

while count < limit:
    count += 1

    guess = int(input("Choose a possible number: "))

    if guess == x:
        print("Congratulation! you guessed correctly")
        break

    elif guess > x:
        print("You guessed too high")

    elif guess < x:
        print("You guessed too small")

if count >= limit:
    print(f"The number is {x}")
    print("Better luck next time")
