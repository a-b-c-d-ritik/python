def days():
    l=['sun','mon','tue','wed','thur','fri','sat','sun']
    i=0
    while True:
        x=l[i]
        i=(i+1)%7
        yield x

d=days()
t=1
while t<7:
    print(next(d))
    t=t+1
    