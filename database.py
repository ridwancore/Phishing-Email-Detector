import sqlite3


def init_db():
    conn = sqlite3.connect("phishing_detector.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_text TEXT,
        verdict TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_result(email_text, verdict, score):
    conn = sqlite3.connect("phishing_detector.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO email_analysis (email_text, verdict, score)
    VALUES (?, ?, ?)
    """, (email_text, verdict, score))

    conn.commit()
    conn.close()
def get_statistics():
    conn = sqlite3.connect("phishing_detector.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM email_analysis")
    total = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM email_analysis
    WHERE verdict='Phishing Suspected'
    """)
    phishing = cursor.fetchone()[0]

    safe = total - phishing

    conn.close()

    return {
        "total": total,
        "phishing": phishing,
        "safe": safe
    }