#product price above average

price=[150,350,200,450,100,500,120,180,290,400]
avg=sum(price)/len(price)

print("Average price of the products:",avg)

res=[p for p in price if p>avg]

print("Products with price above average:",res)