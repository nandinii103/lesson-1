print("Welcome to Basic AI chatbot123!")
name = input("enter your name: ")
print("hello" , name)
while True:
    message = input("\nHow can i asssist you with your task today?")
    if "hello" in message.lower() or "hi" in message.lower():
        print("Hello! nice ot meet you, what can i help you with!")
    elif "how are you" in message.lower():
        print("i am doing wonderfull! , thanks for asking")
    elif "your name" in message.lower():
        print("i am called Basic AI chatbot123 ")
    elif "thanks" in message.lower():
        print("no problem! you are welcome")
    elif "bye" in message.lower() or "goodbye!" in message.lower():
        print("See ya! have a great day!")
        break
    else:
        print("Sorry i dont understand that query, ask another question.")