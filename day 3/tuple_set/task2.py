product=("Laptop", 52000, 2)
print("Product Name:", product)

try:
    product[1]= 55000
except TypeError:
    print("Error: Cannot modify a tuple.")
    
update_product=(product[0], 55000, product[2])
print("Updated Product:", update_product)