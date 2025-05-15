def display():
    print("hello dost")

def fn(d):
    d()

fn(display)

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def call(f,x,y):
    f(x,y)

call(add,3,4)
call(sub,3,4)



#function returning function

def outer():
    print("outer")

    def inner():
        print("inner")

    return inner;


d=outer();

d();