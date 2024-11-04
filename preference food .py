fav1=['pizza','nuggets','hotdog','noodles','pasta','burger']
fav2=['burger','hotdog','noodles','pasta','nuggets','pizza']
indx1=len(fav1)
indx2=len(fav2)
idx=0
for i in range(len(fav1)): 
    idx=i+fav2.index(fav1[i])
    if indx1+indx2>idx:
        indx1=i
        indx2=fav2.index(fav1[i])

print(fav1[indx1],indx1+indx2)

