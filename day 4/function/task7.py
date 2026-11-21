import time
def timer(func):
    def wrapper():
        start= time.time()
        func()
        end= time.time()
        print(f"Execution time: {end - start} seconds")
        
    return wrapper

@timer
def calculute():
    total=sum(range(1,1000000))
    print("Total:",total)
calculute()