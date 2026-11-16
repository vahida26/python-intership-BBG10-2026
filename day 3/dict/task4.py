name=["apple","banana","grapes","mango","orange"]
group={}
for i in name:
    first=i[0]
    group.setdefault(first,[]).append(i)
print(group)