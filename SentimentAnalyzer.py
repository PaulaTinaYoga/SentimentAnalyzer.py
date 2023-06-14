from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_scores = []

    def analyze_sentiment(self, texts):
        for text in texts:
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            self.sentiment_scores.append(sentiment_score)

    def display_sentiment_scores(self):
        print("Sentiment Scores:")
        for score in self.sentiment_scores:
            print(score)

def main():
    texts = ["I love this movie!", "The weather is terrible.", "The food was delicious.", "I feel sad today."]

    analyzer = SentimentAnalyzer()
    analyzer.analyze_sentiment(texts)
    analyzer.display_sentiment_scores()

if __name__ == "__main__":
    main()
