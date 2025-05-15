def outer():
    print("outer call")
    def inner():
        print("inner call")
    
    inner();

outer();