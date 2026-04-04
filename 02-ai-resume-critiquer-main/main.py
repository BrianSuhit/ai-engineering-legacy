import os
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader

 
load_dotenv()
my_api_key = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=my_api_key)


def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        accumulated_text = ""
        for page in reader.pages:
            accumulated_text += page.extract_text()
        return accumulated_text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
    
def analyze_profile():
    file_name = "cv-brian.pdf"
    
    print(f"🔍 Analyzing {file_name}...")
    pdf_text = extract_text_from_pdf(file_name)
    
    if not pdf_text:
        return

    model = genai.GenerativeModel('gemini-3-flash-preview')
    
    prompt = f"""
    Act as a senior technical recruiter for a leading tech company.
    Your task is to provide a constructive and technical critique of this resume.
    
    Points to evaluate:
    1. Clarity of technical skills.
    2. Impact of the mentioned projects.
    3. Specific advice for someone who wants to be an AI Engineer.
    
    Resume to analyze:
    {pdf_text}
    """

    print("🧠 The AI is processing your profile...")
    response = model.generate_content(prompt)
    
    print("\n" + "="*50)
    print("📋 CAREER CRITIQUE REPORT")
    print("="*50 + "\n")
    print(response.text)

if __name__ == "__main__":
    analyze_profile()