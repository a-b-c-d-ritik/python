n=int(input("Enter how many numbers you want to give:"))
t=n
i=0
max=0
while i<t:
    n=int(input("Enter no:"))
    if n>max:
        max=n
    i+=1
print("max is ",max)

