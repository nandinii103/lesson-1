child_tickets = float(input("Enter the price of child tickets: "))
if child_tickets >= 35:
    print("It is too overpriced!")
elif child_tickets <= 20:
    print("Its great and cheap!")
else:
    print("Its a affordable price!")