from textblob import TextBlob

print("Welcome to the sentiment chatbot")

history = []
statistics = {"positive": 0, "negative": 0, "neutral": 0}

while True:
    message = input("\nEnter a sentence (or 'exit', 'stats', 'reset'): ")
    command = message.lower()

    if command == "exit":
        print("\nThank you for using this chatbot!")
        print("Final stats:", statistics)
        break

    if command == "stats":
        print("Stats:", statistics)
        continue

    if command == "reset":
        statistics = {"positive": 0, "negative": 0, "neutral": 0}
        print("Data reset.")
        continue

    blob = TextBlob(message)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
        print("Positive sentiment")
    elif polarity < 0:
        sentiment = "negative"
        print("Negative sentiment")
    else:
        sentiment = "neutral"
        print("Neutral sentiment")

    print("Sentiment:", sentiment)
    statistics[sentiment] += 1

