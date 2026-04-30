def hotelCost(nights):
    return nights * 1000

def planeCost():
    return 5000

def vehicleCost(days):
    return days * 500

def totalTripCost(nights , days):
    hotel = hotelCost(nights) 
    plane = planeCost()
    vehicle = vehicleCost(days)
    total = hotel + plane + vehicle
    return total 
print("Total trip cost was : " , totalTripCost(4,4))

