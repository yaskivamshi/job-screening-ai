import sqlite3

# Configuration
DB_PATH = "job_screening.db"
MATCH_THRESHOLD = 80.0

def shortlist_candidates():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shortlisted (
        candidate_id INTEGER PRIMARY KEY,
        name TEXT,
        match_score REAL
    )
    """)

    # Fetch all candidates
    cursor.execute("SELECT id, name, match_score FROM candidates")
    all_candidates = cursor.fetchall()

    # Shortlist logic
    shortlisted = [
        (cid, name, score)
        for cid, name, score in all_candidates
        if score >= MATCH_THRESHOLD
    ]

    # Insert shortlisted
    cursor.executemany("INSERT OR IGNORE INTO shortlisted (candidate_id, name, match_score) VALUES (?, ?, ?)", shortlisted)

    conn.commit()
    conn.close()
    print(f"✅ Shortlisted {len(shortlisted)} candidate(s).")

if __name__ == "__main__":
    shortlist_candidates()
