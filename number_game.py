
import random

num=random.randint (1,20)
for i in range (1,4):
    user_guess=int(input("enter the number"))
    if user_guess==num:
        print("hurray")
        print(num)
    if user_guess!=num:
        print("your guess is not correct")
    if i==3:
        print("the correct number is",num)



