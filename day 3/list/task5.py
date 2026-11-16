student=[("John", 85), ("Alice", 92), ("Bob", 78)]
print("Student records:")
res=sorted(student, key=lambda x: x[1], reverse=True)
print(res)