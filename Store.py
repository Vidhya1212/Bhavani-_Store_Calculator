
# # Bhavani Store - Billing Calculator
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

# Smart Offer System - NEW
if finalprice > 1000:
    print("Wow! You get a FREE Gift from Bhavani Store! 🎁")
else:
    print("Thank you for shopping! Visit again!")

print("Thank you for shopping!")
