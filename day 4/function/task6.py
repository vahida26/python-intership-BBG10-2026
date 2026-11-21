def total(n):
    if n == 1:
        return 1
    else:
        return n + total(n - 1)
print("Total:",total(5))