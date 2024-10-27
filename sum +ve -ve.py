n=int(input("Enter how many numbers you want to add:"))
t=n
i=0
sump=sumn=0
while i<t:
    n=int(input("Enter no:"))
    if n>0:
        sump+=n
    elif n<0:
        sumn+=n
    else:
        print("invalid input")
    i+=1
print("sum of +ve's is ",sump)
print("sum of -ve's is ",sumn)


