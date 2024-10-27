#ap =a+id//comment

a=int(input("Enter first element:"))
d=int(input("Enter common difference:"))
n=int(input("Enter no of terms:"))

for i in range(0,n+1):
    print(a+i*d)

for i in range(a,a+n*d+1,d):
    print(i)