str1=input("Enter first string:")
str2=input("Enter second string:")

if len(str1) != len(str2):
    print("length is Not same")
else:
    for x in str1:
        if x not in str2:
            print("Not Anagram")
            break;
    else:
        print("Anagram")
        
            