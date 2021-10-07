
# num = int(input("enter the number:"))
# num2 = num
# sum = 0
# while(num>0):
#     sum=sum+(num%10)*(num%10)*(num%10)
#     num=num//10
# if num2==sum:
#     print("it is armstrong number")          
# else:
#     print("it is not armstrong number")
    


num=input("enter the number")
num2=int(num)
i=0
length=len(num)
sum=0
while i<len(num):
    rem=num2%10
    sum += rem ** length
    num2=num2//10
    i=i+1
if int(num) == sum:
    print("it is armstrong number")
else:
    print("it is not armstrong")



