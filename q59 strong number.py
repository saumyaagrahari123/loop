

# x=int(input("enter the number"))
# temp=x
# total=0
# while (x>0):
#     dig=x%10
#     x=x//10
#     a=(dig)
#     total=total+a
# if total==temp:
#     print("its a strong number") 
# else:
#     print("its not a strong number")     


num=int(input("enter the number"))  
i=1
d=0
while num>i:
    a=num%10
    b=(num//10)%10
    c=(num//10)//10
    d=a+b+c
    if d%10==0:
        print(num,"is strong number")
    else:
        print(num,"is not strong number")
    i=i+1

