from threading import *;
from time import *;

class mt(Thread):
    def run(self):
        for x in range(65,91):
                print(x)
                sleep(1)


t=mt()
t.start()
for i in range(65,90):
    print(chr(i))
t.join()