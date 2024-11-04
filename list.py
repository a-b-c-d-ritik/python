list1=[1,2,3,4,5]
for x in list1:
    print(x)

list2=list((1,2,3,4,5))
for x in list2:
    print(x)

print(list1)
list2.append(60)
print(list2)

list=[1,2,3,4,5,6,7,8,9,10]
list[0:3]=[11,12,13]
print(list)
list[0:3]=[99,100]
print(list)
list[0:2]=[99,100,98,97,96,95]
print(list)
list[::2]=[1,2,3,4,5,6,7]
print(list)

li=[1,2,3,4,5,6,7,8,9,10]
li[::3]=['a','b','c','d' ]
print(li)
