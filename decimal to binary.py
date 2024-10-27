t=n=int(input("Enter decimal no:"))
i=0
sum=0
while n>0:
    r=n%2
    sum=sum*10+r
    n//=2
 
n=0   
while sum>0:
    r=sum%10
    sum=sum//10
    n=n*10+r

    
print("Binary of ",t,"is :",n)