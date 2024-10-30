n=int(input("Enter no:"))
for j in range(1,n,1):
    ctr=0
    for i in range(1,j+1,1):
        if n%i==0:
            ctr+=1
    if ctr==2:
        print(j," is prime no")
