day = input("enetr the day: ")
weather = input("enter the weather(sunny/rainy): ")
return_book =input("do your needa return a book? (yes/no): ")

if return_book == "yes" and weather == "sunny":
    print("visit the library and reurn your book")
elif return_book == "yes" and weather == "rainy":
    print("take an umbrella and return your book")
elif day == "sunday":
    print("enjoy reading at home")