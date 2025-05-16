def miles2km(miles):
    return 1.6*miles

print(miles2km(10))

#lambdafn

m2k=lambda miles:1.6*miles
print(m2k(10))


add=lambda a,b:a+b
print(add(19,11))


g=lambda a,b:a if a>b else b
print(g(10,23))