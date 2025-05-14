def one(a,b,c,d,e,f):
    return a+b+c+d+e+f

def two(a,b,/,c,d,e,f):
    return a+b+c+d+e+f

def three(a,b,/,c,d,*,e,f):
    return a+b+c+d+e+f

print(one(1,2,3,4,5,6))
print(two(1,2,3,4,5,6))
print(two(1,2,c=3,f=4,d=5,e=6))

print(three(1,2,3,4,e=5,f=6))

#positional only
def padd(a,b,/):
    return a+b

print(padd(2,5))

#keyword only
def kadd(*,a,b):
    return a+b

print(kadd(a=2,b=5))