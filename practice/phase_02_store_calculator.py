import math
name = input("Track name? ")
price = float(input("Price? "))
quantity = int(input("Quantity being purchased? "))
subtotal = price * quantity
discount = float(input("Discount percentage? "))
discount_amount = subtotal * discount / 100
final_total = subtotal - discount_amount
print(f"Track name: {name}")
print(f"Qantity: {quantity}")
print(f"                    Subtotal: {subtotal:.2f}")
print(f"Discount amount: {discount_amount}")
print(f"                    Final total: {final_total:.2f}")