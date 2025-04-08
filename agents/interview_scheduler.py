from tools.email_sender import send_email

def schedule_interview(name, email, score):
    subject = "Interview Invitation from AI Job Screening System"
    message = f"""
Hi {name},

Congratulations! Based on your resume match score of {score}, you have been shortlisted for the next round.

Please choose your preferred interview time slot:
- 📅 Date: [Insert Date Options]
- ⏰ Time: [Insert Time Options]
- 💻 Format: Online

Kindly reply to this email with your preferred slot.

Best,
HR Team
"""
    send_email(email, subject, message)
    print(f"📬 Interview email sent to {email}")
