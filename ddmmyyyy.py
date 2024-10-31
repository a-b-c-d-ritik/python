date=input("Enter date in format(dd/mm/yyyy): ")
dd=date[:date.index('/'):]
mm=date[date.index('/')+1:date.rindex('/')]
yy=date[date.rindex('/')+1::]

print("date:",dd)
print("month:",mm)
print("year:",yy)