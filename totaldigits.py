num = int(input("Enter a number: "))

digits = 0

if num == 0:
    count = 1

else:
    num = num // 10
    digits += 1