def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
        
    except KeyError as missing_key:
            print(f"Error: Missing key in order dictionary: {missing_key}" )
    else:
            print(f"Order conformed : {item}, Rs={price}")
    finally:
        print("Processing completed.")
        
process_order({"item": "Computer", "price": 59000})
print("***********************************")
process_order({"item": "CPU", "price": 40000})
print("*********************************")
