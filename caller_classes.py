class Dept:
    def __init__(self):
        self.depts={
            'hr':'Human resource',
            'acc':'Accounts',
            'sd':'sales and distribution',
            'mkt':'marketing'
        }
    def __call__(self,dept):
        return self.depts[dept]
    

d=Dept()
s=d('hr')
print(s)


#closure
def Dept1():
    depts={             #variable
            'hr':'Human resource',
            'acc':'Accounts',
            'sd':'sales and distribution',
            'mkt':'marketing'
        }
    def dname(dept):
        return depts[dept]
    
    return dname

x=Dept1();
st=x('mkt')
print(st)
