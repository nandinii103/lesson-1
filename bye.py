valid = False 

while not valid:
    try:
        num = int(input("Enter a number: "))
        valid = True
        if num % 2 == 0:
            while True:
                print("I hate algebra so much")
            
        else:
            print("Number is not  divisible by 2")
    except ValueError:
        print("Invalid input")


