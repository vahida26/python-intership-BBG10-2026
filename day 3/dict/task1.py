product={"pen":10, "bag": 400, "book": 250,
         "pad":200,"scale":800}
print("Product Prices:")
new_product={key: value for key, value in product.items() 
             if value>100}
print(new_product)