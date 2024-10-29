limit=int(input("Enter a limit"))
for number in range(2,limit+1):
    isPrime=True
    for i in range(2,number//2+1):
        if number%i==0:
            isPrime=False
    if isPrime==True:
       print(number)