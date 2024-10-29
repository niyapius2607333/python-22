'''
Author : Niya Pius
Date : 15-10-2024
Python program to print multiplication table of a number
Version 1.0
'''
number=int(input("Enter a number"))
limit=int(input("Enter the limit"))
for i in range(0,limit):
    print(number,"*",i,"=",number*i)
