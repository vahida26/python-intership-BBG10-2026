inventory={"pen":10,
          "pencil":20,
          "eraser":15
          }
inventory['pen']+=10

product="book"
quantity=5
if product in inventory:
    if inventory[product]<=quantity: 
        inventory[product]+=quantity
        print("product sold successfully")
    else:
        print("product not available")
else:
        print("product not found")

print(inventory)