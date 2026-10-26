
# Task 7: Sentiment Analyzer
# Local demo — no API requests required.

positive_words = {
    "good", "great", "excellent", "happy", "love", "wonderful",
    "amazing", "helpful", "best", "enjoy", "fantastic", "success"
}

negative_words = {
    "bad", "terrible", "awful", "sad", "hate", "poor",
    "worst", "angry", "disappointed", "failure", "useless", "difficult"
}

def analyze_sentiment(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()

    positive_count = sum(word.strip("!?") in positive_words for word in words)
    negative_count = sum(word.strip("!?") in negative_words for word in words)

    if positive_count > negative_count:
        sentiment = "POSITIVE 😊"
    elif negative_count > positive_count:
        sentiment = "NEGATIVE 😟"
    else:
        sentiment = "NEUTRAL 😐"

    print("\nSentiment:", sentiment)
    print("Positive words:", positive_count)
    print("Negative words:", negative_count)

print("=" * 45)
print("AI SENTIMENT ANALYZER")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    text = input("\nEnter text to analyze: ").strip()

    if text.lower() == "exit":
        print("Goodbye!")
        break

    if text:
        analyze_sentiment(text)
    else:
        print("Please enter some text.")
