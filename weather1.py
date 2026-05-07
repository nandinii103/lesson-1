weather = (1 , 0 ,0 , 0 , 1 , 1 , 0 )
rainy = 0 
sunny = 0
for i in weather:
    if i == 1:
        rainy += 1
    else:
        sunny += 1
if rainy > sunny:
    print("Rainy weather predicted")
else:
    print("Sunny weather predicted")