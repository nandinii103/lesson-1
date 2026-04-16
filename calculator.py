def add(a , b):
    print("" , a + b)
def subtract(a , b):
    print("-" , a - b)

def multiply(a , b):
    print("*" , a * b)
def division(a , b):
    print("//" , a // b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("choose operator")
print("1. add ")
print("2. subtract")
print("3. multiply")
print("4. division ")

choice = int(input("Enter choice (1-4)"))
if choice == 1:
    add(num1 , num2)
elif choice == 2:
    subtract(num1 , num2)
elif choice == 3:
    multiply(num1 , num2)
elif choice == 4:
    division(num1 , num2)
else:
    print("invalid choice")



    