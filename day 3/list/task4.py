matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
res=[[row[i]  for row in matrix] for i in range(3)]

for row in res:
    print(row)