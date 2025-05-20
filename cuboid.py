class cuboid:
    def __init__(self,l,b,h):
        print(id(self))
        self.length=l
        self.breadth=b
        self.height=h

    def vol(self):
        print(id(self))
        return self.length*self.breadth*self.height
    
    def totalarea(self):
        return 2*(self.length*self.breadth+self.breadth*self.height+self.length*self.height)    

c1=cuboid(10,20,30)
print(c1)
print(c1.vol())
print(c1.totalarea())
        