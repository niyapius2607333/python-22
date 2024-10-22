'''
Author : Niya Pius
Date : 15-10-2024
Python program to find largest of three numbers
Version 1.0
'''
num1=int(input("Enter a  first number"))
num2=int(input("Enter a second number"))
num3=int(input("Enter a third number"))
large=0
if num1>num2:
    large=num1
elif large>num3:
    print(num1,"is the largest")
else:
    print(num3,"is the largest")
