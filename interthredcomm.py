from threading import *;

class mydata:
    def __init__(self):
        self.data=0
        self.flag=False
        self.lock=Lock()

    def put(self,d):
        while self.lock!=False:
            pass
        self.lock.acquire()
        self.data=d
        self.flag=True
        self.lock.release()
    
    def get(self):
        while self.lock!=True:
            pass
        self.lock.acquire()
        d=self.data
        self.flag=False
        self.lock.release()
        return d
    
def producer(data):
    i=1
    while True:
        data.put(i)
        print("producer",i)
        i=i+1

def consumer(data):
    while True:
        x=data.get()
        print("consumer",x)


data=mydata()

t1=Thread(target=lambda:producer(data))
t2=Thread(target=lambda:producer(data))

t1.start()
t2.start()
