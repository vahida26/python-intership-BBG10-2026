from functools import reduce
numbers =[10,20,90,40,50]
largest= reduce(lambda a, b: a if a > b else b, numbers)
print("Largest number:", largest) 