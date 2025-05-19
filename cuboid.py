class cuboid:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h

    def vol(self):
        return self.length*self.breadth*self.height
    

c1=cuboid(10,20,30)
print(c1)
print(c1.vol())
        