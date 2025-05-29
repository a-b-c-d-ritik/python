import numpy as np;

a1=np.array(10) #scalar value
print(a1)
print(type(a1))

#1d array
a=np.array([1,2,3,4,5])
b=np.array((1,2,3,4,5))
c=np.array({1,2,3,4,5})

print(a)
print(b)
print(c)
print(type(c))


#2d array
a2=np.array([[1,2,3,4],[5,6,7,8]])
print(a2) 

#3d array
a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a3)

a4=np.array([1,2,3,4],ndmin=3)
print(a4) 
print(a4.dtype)
print(a.shape)

ac1=np.zeros(3)
ac2=np.ones((3,3))
ac3=np.empty((3,3,3))

print(ac1)
print(ac2)
print(ac3)