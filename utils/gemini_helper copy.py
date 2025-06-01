import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # Make sure to set this in your .env file

client = genai.Client(api_key=api_key)

SAFEGUARD_INSTRUCTIONS = (
    "You are a legal rights assistant based on the Constitution of the Philippines. "
    "Only answer questions related to human rights, legal protections, or justice. "
    "Politely reject questions that are unrelated, inappropriate, or not legally grounded."
)

# Safety filters
SAFETY_SETTINGS = [
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
]

def get_legal_answer(user_prompt: str) -> str:
    try:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(f"{SAFEGUARD_INSTRUCTIONS}\n\nUser: {user_prompt}")]
            )
        ]

        config = types.GenerateContentConfig(
            safety_settings=SAFETY_SETTINGS,
            response_mime_type="text/plain"
        )

        response_text = ""
        for chunk in client.models.generate_content_stream(
            model="gemini-1.5-flash-8b",
            contents=contents,
            config=config
        ):
            response_text += chunk.text or ""
        
        return response_text.strip() or "⚠️ Gemini did not return a usable answer."

    except Exception as e:
        return "⚠️ Gemini could not process this request. Try again later or refine your question."
