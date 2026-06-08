amount = float(input("Enter the total amount you have spent: "))
if amount >= 100:
    discount = 20
elif amount >= 50:
    discount = 10
else:
    discount = 0
print("Discount:" , discount , "%")