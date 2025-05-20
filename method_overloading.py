class Arith:
    def sum(self,a,b,c=None):
        s=a+b
        if c==None:
            return s
        else:
            return s+c
    
    #def sum(self,a,b,c):
        #return a+b+c
    
a=Arith()

print(a.sum(10,20))
print(a.sum(10,20,30))