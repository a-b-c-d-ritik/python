weekhr=[int(x) for x in input('Enter working hrs per day separated by spaces:').split()]
print("total working hr:",sum(weekhr))
rate=int(input("Enter wage per hr:"))
print("salary=",rate*sum(weekhr))