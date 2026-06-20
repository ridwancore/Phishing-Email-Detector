from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

emails = [
    "urgent verify your password now",
    "your account has been suspended",
    "click here to claim your prize",
    "meeting scheduled for tomorrow",
    "please review the attached report",
    "project discussion at 5 pm"
]

labels = [
    "phishing",
    "phishing",
    "phishing",
    "safe",
    "safe",
    "safe"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

joblib.dump(model, "models/phishing_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")