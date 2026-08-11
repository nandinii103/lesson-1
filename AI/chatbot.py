print("welcome to ai chatbot")
name = input("Enter your name: ")
print("hello" , name)
message = input("how can i assist you today?")
if "hello" in message.lower() or "hi" in message.lower():
    print("hello nice to meet you")
elif "how are you" in message.lower():
    print("i am good , thank you for asking")
elif "your name?" in message.lower():
    print("i am a simple ai chatbot")
elif "bye" in message.lower():
    print("goodbye have a wonderful day")
else:
    print("sorry i dont understand that yet")


