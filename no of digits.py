n=int(input("enter no:"))
t=n
ctr=0
while n>0:
    r=n%10
    n=n//10
    ctr+=1
print("no of digits in ",t," is :",ctr)