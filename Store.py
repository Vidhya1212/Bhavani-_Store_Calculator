
# # Bhavani Store - Billing Calculator
# My first Python project - Built on mobile

storename = "Bhavani"
print(f"Welcome to {storename} Store")
n=int(input("How may customers today:"))
     
for customer in range(n):
    print(f"\n--- Customer {customer+1} ---")
    price = float(input("Enter the price: "))
    discountpercent = float(input("Enter discount %: "))

    discount = price * discountpercent / 100
    finalprice = price - discount

    print(f"You pay: {finalprice}")

    if finalprice > 1000:
        print("Wow! FREE Gift! 🎁")
    else:
        print("Thank you! Visit again!")

# LOOP ENDS
print("===Welcome===")
