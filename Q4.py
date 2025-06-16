import pandas as pd

positive_reviews = ["loved", "amazing", "great", "excellent", "best", "wonderful","fantastic", "superb", "enjoyed", "brilliant"] * 5
negative_reviews = ["hated", "terrible", "boring", "worst", "poor", 
"awful", "bad", "disappointing", "unwatchable", "weak"] * 5

all_reviews = positive_reviews + negative_reviews
all_sentiments = ["positive"] * 50 + ["negative"] * 50

data = {
    'Review' : all_reviews,
    'Sentiment': all_sentiments,
}

df = pd.DataFrame(data)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=500, stop_words='english')
X = vectorizer.fit_transform(df['Review'])

from sklearn.model_selection import train_test_split

y = df['Sentiment']  # y will be either of positive label or negative.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   # random_state just helps us in ki hr baar same type of result so debugging becomes easier and "42" is not any speciifc but is famous (as found per research).

# Got to know about through google research and then understood it and implemented it
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

model = MultinomialNB()
model.fit(X_train, y_train) # Utilises in learning the patterns from data

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

def predict_review_sentiment(model, vectorizer, review):
    review_vector = vectorizer.transform([review])
    return model.predict(review_vector)
print (predict_review_sentiment(model, vectorizer, "Horrible movie"))

