# Bhavani Store - Billing Calculator
# My first Python project - Built on mobile

store_name = "Bhavani"
print(f"Welcome to {store_name} Store")

price = float(input("Enter the price: "))
discount_percent = float(input("Enter discount %: "))

discount = price * discount_percent / 100
final_price = price - discount

print(f"Original Price: {price}")
print(f"Discount: {discount}")
print(f"You pay: {final_price}")
print("Thank you for shopping!")
