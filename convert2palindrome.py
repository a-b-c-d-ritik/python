#convert a given string to palindrome
str=input("Enter a string:")
temp=str[-1::-1]
str=str+temp
print (str)

temp=str[-1::-1]
if str==temp:
    print("palindrome")
else:
    print("Not palindrome")
