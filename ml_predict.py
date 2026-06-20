import joblib

# Load trained model and vectorizer
model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_email(email_text):
    X = vectorizer.transform([email_text])
    prediction = model.predict(X)[0]

    return prediction