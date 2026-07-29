from textblob import TextBlob
print("welcome to the sentiment chatbot")
while True:
    message = input("enter a sentence (or type 'exit' to leave site )")
    if message.lower() == "exit":
        print("thank you for using this chatbot!")
        break
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        print("positive sentiment")
    elif polarity < 0:
        print("negative senitment")
    else:
        print("neutral sentiment")

    
        