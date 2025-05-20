class rational:
    def __init__(self,p=1,q=1):
        self.p=p
        self.q=q
    
    def __add__(self,other):
        s=rational()
        s.p=self.p*other.q+self.q*other.p
        s.q=self.q*other.q
        return s
    
    def __str__(self):
        return str(self.p,"/",self.q)
r1=rational(1,1)
r2=rational(3,2)
print((r1+r2).p,"/",(r1+r2).q)
#print(r1.__add__(r2))
print(r1+r2)