def make_counter(start):
    count=start
    def increament():
        nonlocal count # use : enclosing function variable change
        count=count+1
        return count
    return increament

counter1=make_counter(0)
counter2=make_counter(100)

print(counter1())
print(counter1())

print(counter2())
print(counter2())
print(counter2())

print("counter 1:",counter1())
print("counter 2:",counter2())
  