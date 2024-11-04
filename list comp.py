l1=[]
for x in range(10):
    l1.append(x)
print(l1)

l2=[x for x in range(20)]
print(l2) 

l3=[x**2 for x in range(1,6)]
print(l3)

l4=[x for x in (10,5,7,8,12,3) if x%2==0]
print(l4)

l5=[x.lower() for x in 'Python']
print(l5)

l6=[x for x in 'ab$%$&@^*gsdgjdsj%^$$' if x.isalpha()]
print(l6)

#multiple input
data=input('Enter 3 names:')
l7=data.split()
print(l7)

#loop use
print("Enter 3 names:")
l8=[]
for i in range(3):
    l8.append(input())

print(l8)