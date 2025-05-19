with open('my.data','rb') as f:
    print(f.read(2).decode())
    f.seek(3,0)
    f.seek(3,1)
    f.seek(3,1)
    print(f.read(1).decode())
