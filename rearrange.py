str=input("Enter string:")
lowc=''
upc=''
for x in str:
    if x.islower():
        lowc=lowc+x
    elif x.isupper():
        upc=upc+x
    
roder=lowc+upc
print(roder)