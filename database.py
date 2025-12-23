import sqlite3

DB_NAME = "jobs.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            role TEXT,
            location TEXT,
            apply_link TEXT,
            status TEXT DEFAULT 'Not Applied'
        )
    """)

    conn.commit()
    conn.close()

def insert_jobs(jobs):
    conn = connect_db()
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (company, role, location, apply_link)
            VALUES (?, ?, ?, ?)
        """, (job["company"], job["role"], job["location"], job["apply_link"]))

    conn.commit()
    conn.close()

def get_jobs(location=None):
    conn = connect_db()
    cursor = conn.cursor()

    if location:
        cursor.execute("SELECT * FROM jobs WHERE location LIKE ?", (f"%{location}%",))
    else:
        cursor.execute("SELECT * FROM jobs")

    rows = cursor.fetchall()
    conn.close()
    return rows
