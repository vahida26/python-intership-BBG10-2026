n_price=45
bug=500

# 1. Calculates the total cost for 7 notebooks
total=n_price*7
print("Total cost for 7 notebooks:",total)

#2.Calculates how many notebooks can be bought with a budget of 500 rupees using floor division
n_bought=bug // n_price
print("Notebook bought withh 500:",n_bought)

#3.Calculates how much money is left over after buying the maximum number of notebooks, using modulus
m_left=bug % n_price
print("Money left after buying notebooks:",m_left)
