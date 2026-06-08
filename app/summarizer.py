import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")



def summarize_text(combined_text):

    

    prompt = f"""
            You are an expert educational note-taking assistant.

            Analyze both:

            1. Transcript content
            2. Visual content extracted from video frames

            Generate:

            - Executive Summary
            - Key Concepts
            - Key Takeaways
            - Interview Questions
            - Code Examples
            - Important Visual Insights

            Content:

            {combined_content}
            """

    response = model.generate_content(prompt)

    return response.text