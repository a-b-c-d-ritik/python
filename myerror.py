class myerror(Exception):
    print("error")

try:
    raise myerror("kuch h")
except myerror as e:
    print(e)