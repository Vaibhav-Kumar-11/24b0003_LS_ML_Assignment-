import pandas as pd

positive_samples = ["Good product", "Very useful", "Works well", "Loved it", "Highly recommended"] * 10 
negative_samples = ["Bad quality", "Not working", "Hate it", "Terrible experience", "Waste of money"] * 10

text_samples = positive_samples + negative_samples
labels = ['good']*50 + ['bad']*50

data = {
    "sample" : text_samples,
    "label" : labels,
}
df = pd.DataFrame(data)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=300, stop_words='english', lowercase=True)
X = vectorizer.fit_transform(df["sample"])

from sklearn.model_selection import train_test_split
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

def text_preprocess_vectorize(texts, vectorizer):
    return vectorizer.transform(texts)

# For an example:
sample = ["This was the worst product I ever used"]
vectorized_sample = text_preprocess_vectorize(sample, vectorizer)
print(model.predict(vectorized_sample))