subscribers={"a@gmail.com","b@gmail.com","f@gmail.com"}
customers={"d@gmail.com","a@gmail.com","f@gmail.com"}

no_purchases= subscribers-customers
no_subscribers= customers-subscribers

print("Subscribers who never purchases:", no_purchases)
print("Customers who never subscribers:", no_subscribers)