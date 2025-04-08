import sqlite3

conn = sqlite3.connect("job_screening.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM shortlisted")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
