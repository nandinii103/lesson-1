try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age entered")
    else:
        print("Valid age")

        if age % 2 == 0:
            print("The age is even")
        else:
          print("The age is odd")
except ValueError:
    print("Wrong input! pls enter a valid number")