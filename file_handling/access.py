file=open('f1.txt','r')
str=file.read()
print(str)

file2=open('f2.txt','w')
file2.write("PKMKB")

print(file2.name,file2.mode,file2.closed)