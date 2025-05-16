def decorator(fun):
    def wrapper(msg):
        print("*"*15)
        fun(msg)
        print("*"*15)
    return wrapper

def display(msg):
    print(msg)

t=decorator(display)
t("kya mamu")

#or we can do
display=decorator(display)
display("yo boy")


#or we can do
@decorator
def display1(msg):
    print(msg)

#display=decorator(display)
display1("yo boyhjgjgjjgju")