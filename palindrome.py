n=int(input("Enter no:"))
t=n
sum=0
while n>0:
    r=n%10
    n//=10
    sum=sum*10+r

if t==sum:
    print("palindome")
else:
    print("Not palindrome")
