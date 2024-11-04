l1=[1,2,3,4,5,6,3,7,8,6,4,5,3,29,9]
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x) 
print(l2)