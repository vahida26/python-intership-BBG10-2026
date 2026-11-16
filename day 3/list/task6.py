no=[10,20,40,70,60,30,80]
large=no[0]
second=None
for n in no:
    if n>large:
        second=large
        large=n
    elif second is None or n>second:
        second=n
print("Maximum value:", large)
print("Second maximum value:", second)  