from textblob import TextBlob
print("welcome to the sentiment chatbot")
history = []
statisctics = {"positve": 0 , "negative": 0 , "neutral": 0 }
while True:
    message = input("/nEnter a sentence(or 'exit' , 'stats' , 'reset'):")
    command = message.lower()
if command == exit:
    print("\nThank you for using this chatbot!")
    print("final stats:" , statisctics)
    break
if command == statisctics:
    print("stats" , statisctics)
    countinue
if command == "reset":
    statisctics = {"positve": 0 , "negative": 0 , "neutral": 0 }
    print("data reset")
    continue

    polarity = blob.sentiment.polarity
    if polarity > 0:
        print("positive sentiment")
    elif polarity < 0:
        print("negative senitment")
    else:
        print("neutral sentiment")

print("sentiment: " , sentiment)
statisctics[sentiment] += 1

    
        