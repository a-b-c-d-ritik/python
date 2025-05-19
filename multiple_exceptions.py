l=[10,20,30,40,50]
try:
    index=int(input('enter index:'))
    print(l[index])
#except IndexError:
    #print("invalid index!!!")
#except ValueError as msg:
    #print("invlid value!!!",msg)

#or we can handle both errors in single except
except (IndexError,ValueError) as msg:
        print(msg)
except:
    print("some error")

print('terminated succesfully')