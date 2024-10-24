n=int(input("enter no:"))
t=n
ctr=0
while n>0:
    r=n%10
    n=n//10
    ctr+=1
sum=0
n=t
while n>0:
    r=n%10
    n=n//10
    sum=sum+(r**ctr)

if t==sum :
    print("palindrome")
else:
    print("Not palindrome")