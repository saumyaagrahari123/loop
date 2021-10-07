a=1
while a<=5:
    guess_number=int(input("enter the guessing number"))
    if guess_number==5:
        print("correct guessing number")
        break
    else:
        print("try again")
    a+=1

