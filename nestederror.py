try:
    a=int(input("a="))
    b=int(input("b="))
    try:
        c=a//b
    except Exception as e:
        print(e)
except:
    print("errs")