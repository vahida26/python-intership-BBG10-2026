student=[{"name":"Riya","marks":85},
         {"name":"Amit","marks":90},
         {"name":"Sana","marks":78},
         {"name":"Rahul","marks":92}
         ]
highest=student[0]
for i in student:
    if i['marks'] > highest['marks']:
        highest=i
print("Highest student:", highest)