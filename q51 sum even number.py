# write a program to print the sum of the first 10 even number

index=0
sum=0
while index<=100:
    if index%2==0:
        sum+=index
        # index+index=sum
        print(index)
    index+=1
print(sum)
