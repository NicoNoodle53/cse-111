from datetime import datetime

#get the day of week
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

#get subtotal
subtotal = float(input("Please enter teh subtotal:"))

#check if it's Tuesday or Wednseday and if the subtotal is greater than 50
#if it is apply discount
if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount = subtotal *.1
        subtotal = subtotal - discount
        print(f"Discount amount: {discount:.2f}.")

#calculate tax and print results
tax = subtotal * .06
total = subtotal + tax
print(f"Sales tax amount {tax:.2f}")
print(f"Total: {total:.2f}.")


