class iphone6:
    def home(self):
        print("iphone6 home button pressed")
    
class iphonex(iphone6):
    def home(self):
        print("iphonex home  is touched")
        super().home()

i6=iphone6()
i6.home()

ix=iphonex()
ix.home()