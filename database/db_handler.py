# database/db_handler.py

import sqlite3
import os
from datetime import datetime

DB_NAME = "job_screening.db"

def connect_to_db():
    return sqlite3.connect(DB_NAME)

def delete_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print("🗑️ Deleted existing database: job_screening.db")
    else:
        print("ℹ️ No existing database to delete.")

def create_candidates_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            resume_path TEXT,
            match_score REAL,
            interview_status TEXT DEFAULT 'Pending',
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_candidate_to_db(name, email, phone, resume_path, score):
    create_candidates_table()

    conn = connect_to_db()
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO candidates (name, email, phone, resume_path, match_score, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, resume_path, score, timestamp))

    conn.commit()
    conn.close()
    print("✅ Candidate inserted into database.")
