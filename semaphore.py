from threading import *;
from time import *;

l=Semaphore(2)            #available in threading module
def display(str1):
    l.acquire()
    for s in str1:
        print(s)
    l.release()


t1=Thread(target=display,args=('jai shree ram',))
t2=Thread(target=display,args=('jai Hanuman',))

t1.start()
t2.start()

