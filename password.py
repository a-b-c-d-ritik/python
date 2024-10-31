p1=input("Enter password:")
p2=input("Enter confirm password:")

if p1==p2:
    print("Password matches succesfully")
elif p1.casefold()==p2.casefold():
    print("Please check the casses and try again")
else:
    print("Enterd passwords are not matching")