n=int(input("Enter no:"))
t=n
sum=0
while n>0:
    r=n%10
    n//=10
    sum+=r
print("sum of digits of ",t," is :",sum)
