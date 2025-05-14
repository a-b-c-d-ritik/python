def add(a,b):
    c= a + b
    return c

print(add(5,6)) #positional call


def sub(x,y):
    r=x-y
    return r

print(sub(y=1000,x=1111))



#default arguments
def add3(a=0,b=0,c=0):
    return a+b+c

print(add3(5,7))

#in list
def additem(item1,l=[]):
    l.append(item1)
    return l

print(additem(22))
print(additem(252))