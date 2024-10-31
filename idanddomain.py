mail=input("Enter email add:")
userid=mail[:mail.index("@"):]
dom=mail[mail.index("@")+1:len(mail):]
print("userid :",userid)
print("domain :",dom)