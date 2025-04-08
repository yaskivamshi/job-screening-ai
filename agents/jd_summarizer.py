import requests
import os

def summarize_jd(jd_text):
    """
    Sends JD text to Ollama's local LLM API and returns a summarized version.
    """
    if not jd_text.strip():
        print("⚠️ Empty job description provided.")
        return None

    prompt = f"""
    Summarize the following job description into key sections: 
    1. Required Skills, 
    2. Experience, 
    3. Qualifications, 
    4. Job Responsibilities

    Job Description:
    {jd_text}
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",  # Ensure you're running ollama run llama3
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()

    except requests.exceptions.RequestException as e:
        print(f"❌ API Request failed: {e}")
        return None

if __name__ == "__main__":
    summary = summarize_jd("data/samples_jds/sample_jd1.txt")
    print(summary)
    # Use absolute path based on current file location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_jd_path = os.path.join(script_dir, "..", "data", "samples_jds", "sample_jd1.txt")

    try:
        with open(sample_jd_path, "r", encoding="utf-8") as file:
            jd_text = file.read()
        summary = summarize_jd(jd_text)
        if summary:
            print("📝 Summarized JD:\n", summary)
        else:
            print("⚠️ No summary returned.")
    except FileNotFoundError:
        print(f"❌ File not found: {sample_jd_path}")
    except Exception as e:
        print(f"❌ Error reading file: {e}")