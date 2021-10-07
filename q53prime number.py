prime=int(input("enter the number"))
a=1
b=0
while a<=prime:
    if (prime%a==0):
        b=b+1
    a=a+1
if b==2:
    print("it is a prime number")
else:
    print("it is not prime number")







