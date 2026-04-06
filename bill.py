
units = int(input("Enter the number of units consumed: "))

if units < 50:
 cost = units * 2.60
 tax = 25

elif units < 100:
    cost = units * 3.25 
    tax = 35

elif units < 200:
    cost = units * 5.26
    tax = 45

else:
     cost = units * 8.45 
     tax = 75

total = cost + tax
print("Total cost is:" , total)