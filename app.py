from flask import Flask, render_template, request
from email_analyzer import analyze_email
from database import init_db, save_result, get_statistics

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    email_text = request.form.get("email_text", "")

    uploaded_file = request.files.get("email_file")

    if uploaded_file and uploaded_file.filename != "":
        email_text = uploaded_file.read().decode("utf-8")

    result = analyze_email(email_text)

    save_result(
        email_text,
        result["verdict"],
        result["score"]
    )

    return render_template(
        "result.html",
        result=result
    )


@app.route("/dashboard")
def dashboard():

    stats = get_statistics()

    return render_template(
        "dashboard.html",
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)