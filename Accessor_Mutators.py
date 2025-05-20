class Rectangle:
    
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def getlength(self):
        return self.l
    
    def setlength(self,l):
        self.l=l

    def getbreadth(self):
        return self.b
    
    def setbreadth(self,b):
        self.b=b


r1=Rectangle(10,20)

print(r1.getlength())
print(r1.getbreadth())

r1.setlength(30)
r1.setbreadth(50)

print(r1.getlength())
print(r1.getbreadth())