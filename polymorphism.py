def driver(car):
    car.drive()


class creta:
    def drive(self):
        print("creta is driving")
    
class mercedes:
    def drive(self):
        print("mercedes is driving")


c=creta()
driver(c)

m=mercedes()
driver(m)