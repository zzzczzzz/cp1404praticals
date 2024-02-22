"""
get number of item
for number of item
    get their price
    calculate total
if total is greater than $100
    10% is discounted
print total in 2 decimal place
"""

DISCOUNT_RATE = 0.1
total_price = 0

number_of_item = int(input("Number of items : "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items : "))
for i in range (number_of_item):
    price_of_item = float(input("enter price of item : $ "))
    total_price += price_of_item
if total_price > 100:
    discount_price = total_price * DISCOUNT_RATE
    total_price -= discount_price
print(f"total price for {number_of_item} items is ${total_price:.2f}")