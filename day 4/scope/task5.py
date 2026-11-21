mode="global"

def outer():
    mode="enclosing"
    
    def inner():
        mode="local"
        print("Inner:",mode)
    inner()
    print("outer:",mode)
outer()
print("global:",mode)