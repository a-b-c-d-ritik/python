g=10
def f1():
    global g
    g=g+5
    print(g)
    #print(globals())
f1()

def f2():
    x,y,z=10,20,30
    print(locals())

f2()