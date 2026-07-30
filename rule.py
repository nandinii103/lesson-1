print("Welcome to the rule based chatbot!")
name = input("what is your name: ")
print("hello" , name)
while True:
    message = input("\nYou: ")
    message = message.lower()
    if message == "hello" or message == "hi" or message == "howdy":
        print("Bot: hello how can i help you today?")
    elif "what is your name?" in message:
        print("Bot: i am a rule based chtabot!")
    elif "what is your age" in message:
        print("Bot: i am a billion years old")
    elif "favourite food?" in message:
        print("Bot: i like biryani")
    elif "what countries do you want to visit?" in message:
        print("Bot: i want to visit Italy or Spain!")
    elif "goodbye i am leaving" in message:
        print("Bot: bye bye i shall go now")
        break
    else:
        print("sorry i dont understand that question")


