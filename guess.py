import random
n=random.randint(1,10)
guess=0

while guess!=n :
    guess=int(input("Guess a no between 1 to 10:"))
    if guess>n:
        print("sorry,value is greater than ",guess-n)
    elif guess<n:
        print("Sorry,value is smaller than ",n-guess)
    else:
        print("wow you won!!")
        break
