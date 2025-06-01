# utils/gemini_helper.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

SAFEGUARD_INSTRUCTIONS = (
    "You are a legal rights assistant based on the Constitution of the Philippines. "
    "Only answer questions related to human rights, legal protections, or justice. "
    "Politely reject questions that are unrelated, inappropriate, or not legally grounded."
)

def get_legal_answer(user_prompt: str) -> str:
    try:
        response = model.generate_content(
            f"{SAFEGUARD_INSTRUCTIONS}\n\nUser: {user_prompt}",
            safety_settings=[
                {"category": "HARM_CATEGORY_DEROGATORY", "threshold": "BLOCK_LOW_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUAL", "threshold": "BLOCK_LOW_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_LOW_AND_ABOVE"},
            ]
        )
        return response.text
    except Exception as e:
        return "⚠️ Gemini could not process this request. Try again later or refine your question."
