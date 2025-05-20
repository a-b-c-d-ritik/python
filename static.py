class Rectangle:
    
    def __init__(self,l,b):
        self.l=l
        self.b=b
        

    def area(self):
        return self.l*self.b
    
    def issq(self):
        return self.l==self.b
    
    
    
r1=Rectangle(2,5)
r2=Rectangle(6,6)
print(r1.issq())
print(r2.issq())
