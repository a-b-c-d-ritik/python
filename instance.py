class one:
    def __init__(self):
        self.a=10

    def fn(self):
        self.b=24

v1=one()
print(v1)
print(dir(v1))
print(v1.a)

v1.fn()
#print(t1.b)
print(dir(v1))