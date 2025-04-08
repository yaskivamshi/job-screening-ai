import os
import re
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


def extract_name_and_email(text):
    # Email extraction
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group() if email_match else "Not found"

    # Try explicit name patterns first
    name_match = re.search(r'(?:Name|Full Name|Candidate)\s*[:\-]?\s*([A-Z][a-z]+\s+[A-Z][a-z]+)', text)
    if name_match:
        name = name_match.group(1)
    else:
        # Fallback: guess name from top lines
        lines = text.strip().split("\n")
        name = "Not found"
        for line in lines[:10]:  # Check first 10 lines
            match = re.match(r"^([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)$", line.strip())
            if match:
                name = match.group(1)
                break

    return name, email


def match_resume_to_jd(resume_path, jd_summary):
    resume_text = extract_text_from_pdf(resume_path)
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_summary)

    vectorizer = CountVectorizer().fit_transform([resume_clean, jd_clean])
    similarity = cosine_similarity(vectorizer)[0][1]
    match_score = round(similarity * 100, 2)

    candidate_name, candidate_email = extract_name_and_email(resume_text)
    return match_score, candidate_name, candidate_email


if __name__ == "__main__":
    jd_summary = """
    Required Skills: Python, JavaScript, React, Full-stack development
    Experience: 2+ years in full-stack development
    Qualifications: Bachelor’s degree in CS
    Responsibilities: Building APIs, Developing UI, AWS cloud work
    """

    resume_path = "data/sample_resumes/resume1.pdf"
    score, name, email = match_resume_to_jd(resume_path, jd_summary)
    print(f"✅ Resume Match Score: {score}%")
    print(f"👤 Name: {name}")
    print(f"📧 Email: {email}")
