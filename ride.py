print("Select your ride: ")

print("1. Car")

print("2. Bike")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
   print("Select your Car:")
   print("1. Sedan")
   print("2. SUV")
   car_choice = int(input("Enter your choice (1 or 2): "))

if car_choice == 1:
   print("You selected Sedan")
else:
   print("You selected SUV")

elif choice == 2:   

print("Select your Bike:")
print("1. Sports Bike")
print("2. Cruiser")
bike_choice = int(input("Enter your choice (1 or 2): "))

if bike_choice == 1:
   print("You selected Sports Bike")

else:
 print("You selected Cruiser")


