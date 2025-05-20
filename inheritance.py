class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        

    def area(self):
        return self.l*self.b
    
class cuboid(Rectangle):

    def __init__(self,l,b,h):
        super().__init__(l,b)
        self.h=h
    
    def vol(self):
        return self.l*self.b*self.h

#r1=Rectangle(10,20)
c1=cuboid(30,20,10)

print(c1.vol())