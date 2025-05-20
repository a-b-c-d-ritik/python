class Rectangle:
    count=0
    def __init__(self,l,b):
        self.l=l
        self.b=b
        Rectangle.count+=1

    def area(self):
        return self.l*self.b
    @classmethod #decorator
    def countobj(cls):#self hi h cls v
        print(cls.count)
        print(id(cls))

r1=Rectangle(2,3)
print(r1.area())
r1.countobj()
print(id(r1))

r2=Rectangle(5,3)
print(r2.area())
Rectangle.countobj(r2)
print(id(r2))