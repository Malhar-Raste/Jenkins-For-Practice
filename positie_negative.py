"""Write a program to asks user and check weather the number is postive negative or zero"""
num1 = int(input("Please enter the number you wish to enter = "))
if num1>0:
    print(num1 , " Is a positive number")
elif num1<0:
    print(num1 , " is a negative number")
else:
    print(num1 , " is equal to zero")