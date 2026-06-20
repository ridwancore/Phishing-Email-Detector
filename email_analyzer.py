import re
from ml_predict import predict_email

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "bank",
    "login",
    "click here",
    "limited time",
    "account suspended",
    "winner"
]


def analyze_email(email_text):

    score = 0
    reasons = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in email_text.lower():
            score += 10
            reasons.append(
                f"Suspicious keyword detected: {keyword}"
            )

    urls = re.findall(r'https?://\S+', email_text)

    if urls:
        score += len(urls) * 5
        reasons.append(f"{len(urls)} URL(s) detected")

    shorteners = ["bit.ly", "tinyurl", "goo.gl"]

    for url in urls:
        if any(short in url for short in shorteners):
            score += 20
            reasons.append("Shortened URL detected")

    score = min(score, 100)

    if score >= 50:
        verdict = "Phishing Suspected"
    else:
        verdict = "Likely Safe"

    ml_prediction = predict_email(email_text)

    return {
        "score": score,
        "verdict": verdict,
        "reasons": reasons,
        "ml_prediction": ml_prediction
    }