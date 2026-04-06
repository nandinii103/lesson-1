medical = input("Do you have any medical conditions: (Yes/No)")
if medical == "Yes":
    print("You are allowed to take the exam")
else:
    attendance = int(input("Enter your attendance percentage: "))
    if attendance >= 75:
        print("You can take the exam ")
    else:
        print("You cannot take the exam")