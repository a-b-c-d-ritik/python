class customer:
    def __init__(self,id,name,bdno,bstreet,bcity,bcountry,bpin):
        self.id=id
        self.name=name
        self.badd=self.Address(bdno,bstreet,bcity,bcountry,bpin)
        self.sadd=self.Address(bdno,bstreet,bcity,bcountry,bpin)

    class Address:
        def __init__(self,dno,street,city,country,pin):
            self.dno=dno
            self.street=street
            self.city=city
            self.country=country
            self.pin=pin

        def display(self):
            print(self.dno,"\n",self.street,"\n",self.city,"\n",self.country,"\n",self.pin)



c1=customer(123,'raju',546,"192st",'rampous','bharat',25352)
c1.badd.display()