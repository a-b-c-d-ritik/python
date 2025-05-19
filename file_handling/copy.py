f=open("NEW.jpeg",'rb')

data=f.read()

cp=open('img.jpeg','wb')
cp.write(data)

f.close()
cp.close()