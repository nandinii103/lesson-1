num = int(float(input("Enter a decimal number: ")))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        digit = num % 2
    binary = binary + digit * value
    value = value * 10
    value = 1
    num = num // 2

    print("Binary:", binary)
    