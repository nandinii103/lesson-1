def cube(n):
    return n * n * n

def check(number): 
    if number % 3 == 0:
        result = cube(number)
        print(result)
    else:
        print("number is not divisible")
check(6)