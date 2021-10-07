
perfect=int(input("enter the number"))
i=1
sum=0
while i%perfect:
    if perfect%i==0:
        sum=sum+i
    i=i+1
if sum==perfect:
    print(perfect,"is perfect number")
else:
    print(perfect,"is not perfect number")