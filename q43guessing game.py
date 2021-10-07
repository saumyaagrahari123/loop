a=1
while a<=5:
    guess_number=int(input("enter the guessing number"))
    if guess_number==5:
        print("Wow! you guess the correct number")
        break
    elif guess_number<=4:
        print("the number is lesser")
    elif guess_number>=6:
        print("the number is greater")
    else:
        print("try again")
    a+=1

