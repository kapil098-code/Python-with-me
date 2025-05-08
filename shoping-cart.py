item = input("what item would you like to buy?: ")
price =float(input("what is the price?: "))
quantity =int(input("How many would you likeu?: "))

total = price * quantity

print(f"Your have bought {quantity} x {item}/s")
print(f"You total is: ${round(total)}")