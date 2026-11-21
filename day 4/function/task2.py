def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    print("Discount amount:", discount_amount)
    final_price = price - discount_amount
    print("Final price:", final_price)

apply_discount(1000) 
apply_discount(1000,percent=20)