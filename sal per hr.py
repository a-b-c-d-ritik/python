rate=int(input("Working wage per hour:"))
whrs=[]
t=0
sumhrs=0
print("Enter 7 day working hours record:")
for i in range(7):
    t=int(input())
    whrs.append(t)
    sumhrs=sumhrs+t

salary=sumhrs*rate
print("working hrs:",whrs)
print("Total salary of week is:",salary,"rs")