print("before try")

try:
    n1=int(input('n1='))
    n2=int(input('n2='))
    c=n1//n2
    
except ZeroDivisionError as msg:
    print(msg)
else:
    print(n1,"/",n2,"=",c)
    print("no error")
