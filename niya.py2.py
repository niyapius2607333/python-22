'''
Author : Niya Pius
Date : 15-10-2024
Python program to convert temparature from celsius to fahrenheit and vice versa.
Version 1.0
'''
temp=int(input("Enter the temparature"))
type=(input("IS THIS IN CELSIUS OR FAHRENHEIT?"))
final_temp=0
if type=='C':
    final_temp=9/5*temp+32
    print("Temparature in fahrenheit=",final_temp)
    print(temp," celsius is",final_temp,"fahrenheit")
else :
    final_temp=5/9*temp-32
    print("Temparature in celsius=",final_temp)
    print(temp," fahrenheit is",final_temp,"celsius")

