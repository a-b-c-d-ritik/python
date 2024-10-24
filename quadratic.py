import math
print('Enter quadratic eqn(ax^2+bx+c=0 coefficients a,b and c)')
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
d=((b**2)-4*a*c)
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
print('Roots of quadratic eqn ',a,'x^2 + ',b,'x + ',c,' is ',r1,' ',r2)