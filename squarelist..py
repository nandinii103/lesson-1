num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the last number: "))

square = [ i ** 2 for i in range(num1 , num2 + 1)]
print("Square: " , square)
even = []
odd = []
for i in square:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even: " , even)
print("Odd:" , odd)