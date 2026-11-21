def build_invoice(name,*prices,**details):
    total = sum(prices)
    print("Customer name:",name)
    print("Total amount:",total)
    print("Extra details:",details)
    
build_invoice("Riya", 100, 200, 300, 
               discount="10%", tax="5%") 
   