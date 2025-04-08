
# 🔍 Enhancing Job Screening with AI and Data Intelligence

### 🚀 Submitted for: **Accenture Hack the Future: A Gen AI Sprint Powered by Data**  
👤 **Individual Contributor**: Vamshi Yaski  
Status: ✅ Completed

---

## 📌 Problem Statement

Current job screening methods are time-consuming and often lack the ability to match resumes accurately with job descriptions. This project automates and enhances the recruitment process using **multi-agent AI**, **natural language understanding**, and **data intelligence**.

---

## 💡 Solution Overview

Developed a solo-built multi-agent system** that:
- Extracts, summarizes, and compares **Job Descriptions (JDs)** and **Resumes (CVs)**
- Generates a **match score** using NLP-based similarity
- Sends automated **email invitations** to shortlisted candidates
- Utilizes **Open Source LLMs (Ollama)**, **Flask**, **SQLite**, and **custom Python tools**

---

## 🧠 Key Features

- 📄 **JD Summarization Agent**: Summarizes large JDs using an on-prem OpenAI-compatible LLM
- 🧾 **Resume Parsing Agent**: Extracts skills, education, and experience from PDF resumes
- 🔍 **Matching Agent**: Calculates similarity between parsed resumes and summarized JDs
- 📧 **Email Agent**: Notifies shortlisted candidates via email
- 🗃️ **SQLite Database**: Stores candidate data and match scores
- 🌐 **Flask UI**: Upload resumes, view JDs, and check match results

---

## 📂 Folder Structure

```
job-screening-ai/
│
├── main.py                   # Flask app entry point
├── jd_summarizer.py          # Summarizes Job Descriptions
├── cv_parser.py              # Extracts resume data
├── matcher.py                # Calculates match score
├── email_agent.py            # Sends emails
├── db.sqlite3                # SQLite database
├── .env                      # Stores API keys
├── requirements.txt          # Project dependencies
│
├── templates/
│   └── index.html            # Frontend UI
├── data/
│   ├── sample_resumes/       # Resume PDFs
│   └── samples_jds/          # JD text files
```

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask, SQLite
- **AI Models**: Ollama LLMs (on-prem), OpenAI-compatible APIs
- **Frontend**: HTML (Jinja2 templates).
- **Tools**: dotenv, PDFMiner, python-docx, smtplib



---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the app:
   ```bash
   python app.py

---

📸 Demo Screenshot Email

![image](https://github.com/user-attachments/assets/115d9417-dd6a-430f-a5e8-20601cf535dc)

---

## 🧠 AI Agents & Flow

1. **JD Summarizer Agent** ➝
2. **Resume Parser Agent** ➝
3. **Matching Agent** ➝
4. **Email Agent**

---

## 🧪 Ethical Web Scraping Test

Included a script to demonstrate responsible scraping from **open GitHub job postings**, following all `robots.txt` rules.

---

## 📎 Deliverables

- ✅ Final Codebase with README
- ✅ Ethical Scraper Script
- 🧠 Ollama Embeddings (Bonus)

---

## 🧠 Future Enhancements

- Add ML-based role predictions
- Support batch JD/Resume uploads
- Build dashboards for recruiters

---

## 🙌 Acknowledgements

Thanks to **Accenture**, **geeks for geeks**, and the **Hackathon Team** for organizing and facilitating this sprint.

---

## 📬 Contact

**Vamshi Yaski**  
📧 vamshiyaski@gmail.com  
🔗 [GitHub](https://github.com/yaskivamshi)  
🔗 [LinkedIn](https://www.linkedin.com/in/vamshi-yaski)

---
