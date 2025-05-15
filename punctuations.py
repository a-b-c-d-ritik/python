punc='''!#$%^&*()_-+={}[];:"",<>.'''
str=input("Enter a string:")
snew=''
for x in str:
    if x not in str:
        snew=snew+x
    print(snew)