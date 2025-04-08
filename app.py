import os
from agents.jd_summarizer import summarize_jd
from agents.resume_matcher import match_resume_to_jd
from agents.interview_scheduler import schedule_interview
from database.db_handler import insert_candidate_to_db, delete_database
from tools.email_sender import send_email

# Delete old database if exists
delete_database()

# File paths
resumes_folder = os.path.join("data", "sample_resumes")
jd_path = os.path.join("data", "samples_jds", "sample_jd1.txt")

print("📄 Loading Job Description...")
with open(jd_path, "r", encoding="utf-8") as f:
    jd_text = f.read()

if not jd_text.strip():
    print("❌ JD file is empty!")
    exit(1)
else:
    print("✅ JD loaded successfully.")

print("💡 Summarizing JD...")
jd_summary = summarize_jd(jd_text)

if jd_summary:
    print("📝 JD Summary:\n", jd_summary)
else:
    print("⚠️ No summary was returned by the model.")
    exit(1)

print("📂 Scanning resumes in:", resumes_folder)
resume_files = [f for f in os.listdir(resumes_folder) if f.lower().endswith(".pdf")]

if not resume_files:
    print("❌ No PDF resumes found in folder.")
    exit(1)

for resume_file in resume_files:
    resume_path = os.path.join(resumes_folder, resume_file)
    print(f"\n📑 Processing resume: {resume_file}")

    try:
        result = match_resume_to_jd(resume_path, jd_summary)
        if result:
            match_score, candidate_name, candidate_email = result
            print("✅ Match Score:", match_score)
            print("👤 Candidate Name:", candidate_name)
            print("📧 Candidate Email:", candidate_email)

            if match_score >= 80:
                print("🎯 Candidate passed the match threshold. Adding to database and scheduling interview...")

                phone = "N/A"  # Optional improvement: Extract phone number if available

                insert_candidate_to_db(candidate_name, candidate_email, phone, resume_path, match_score)
                schedule_interview(candidate_name, candidate_email, match_score)

                # Optional: send confirmation email
                send_email(candidate_email, "Interview Scheduled", f"Hi {candidate_name}, your interview has been scheduled. Match score: {match_score}%")

            else:
                print("❌ Candidate did not meet the shortlisting threshold.")
        else:
            print("⚠️ No result from resume matcher.")

    except Exception as e:
        print(f"❌ Error processing {resume_file}: {e}")
