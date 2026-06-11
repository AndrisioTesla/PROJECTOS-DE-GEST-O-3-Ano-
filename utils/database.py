import sqlite3

DB = "database/history.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        result TEXT,
        confidence REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(text, result, confidence):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history(text, result, confidence)
    VALUES (?, ?, ?)
    """, (text, result, confidence))

    conn.commit()
    conn.close()


def get_all():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data