from threading import *;
from time import *;
def display():
    for x in range(65,91):
        print(x)
        sleep(1)


t=Thread(target=display,name='uc alphabets')
t.start()
for i in range(65,90):
    print(chr(i))
t.join()