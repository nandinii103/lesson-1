print("Welcome to the rule-based chatbot!")

name = input("What is your name: ")
print(f"Hello, {name}!")

while True:
    message = input("\nYou: ").lower()

    if message in ["hello", "hi", "howdy", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "what is your age" in message or "how old are you" in message:
        print("Bot: I am a billion years old!")

    elif "are you human" in message or "are you real" in message:
        print("Bot: I am a robot and not real!")

    elif "favorite food" in message or "best food" in message:
        print("Bot: I like biryani very much, it's very tasty!")

    elif "countries" in message or "place to visit" in message:
        print("Bot: I would enjoy visiting Spain or Mexico!")

    elif "cat or dogs" in message:
        print("Bot: I prefer dogs since they are cuter!")

    elif "fav movie" in message or "best movie" in message:
        print("Bot: I like the movie Harry Potter!")

    elif "tell me a joke" in message:
        print("Bot: Why do programmers wear glasses?")

    elif "why" in message:
        print("Bot: Because they can't C! (HAHAHA)")

    elif "what is your name" in message:
        print("Bot: My name is ChatBot123!")

    elif "goodbye" in message or "bye" in message:
        print("Bot: Bye! Have a good day!")
        break

    else:
        print("SORRY, I don't understand that query. Maybe ask another question!")

