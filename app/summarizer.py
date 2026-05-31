import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")



def summarize_text(text):

    text = text[:30000]

    prompt = f"""
    You are an expert note-taking assistant.

    Analyze the following YouTube transcript and generate:

    1. Video Title
    2. Executive Summary (5-10 lines)
    3. Key Concepts (5 bullet points)
    4. Key Takeaways (5 bullet points)
    5. Interview Questions (5 questions)

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text