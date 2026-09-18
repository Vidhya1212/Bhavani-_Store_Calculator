
# Bhavani Store - Billing Calculator
# My first Python project - Built on mobile

storename = "Bhavani"
print(f"Welcome to {storename} Store")

price = float(input("Enter the price: "))
discountpercent = float(input("Enter discount %: "))

discount = price * discountpercent / 100
finalprice = price - discount

print(f"Original Price: {price}")
print(f"Discount: {discount}")
print(f"You pay: {finalprice}")
print("Thank you for shopping!")
