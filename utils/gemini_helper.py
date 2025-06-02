# utils/gemini_helper.py
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

SAFEGUARD_INSTRUCTIONS = (
    "You are a legal rights assistant based on the legal grounds of the Philippines. "
    "Only answer questions related to human rights, legal protections, or justice. "
    "Politely reject questions that are unrelated, inappropriate, or not legally grounded.\n\n"
)

SAFETY_SETTINGS = [
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
]

def get_legal_answer_with_memory(chat_history: list, language: str = "English") -> str:
    """
    Send the entire conversation (including a leading instruction) as a single 'user' content.
    chat_history: List of dicts [{"role":"user"/"assistant","content": "..."}].
    language: "English" or "Filipino" (to prefix language hint).
    """

    try:
        # 1) Build a single "user" string containing:
        #    - the system instruction (SAFEGUARD_INSTRUCTIONS)
        #    - the entire conversation so far, annotated
        #    - the latest user prompt at the end.
        # 
        #    We will concatenate like:
        #      "Instruction...\n\n"
        #      "User: ...\nAssistant: ...\nUser: ... (latest)\n"
        #
        #    Gemini will see the full context, despite using only role="user".

        conversation_prefix = SAFEGUARD_INSTRUCTIONS

        # If the user asked in Filipino, prepend a note. Otherwise, leave it English.
        if language.lower() == "filipino":
            conversation_prefix = "[Filipino] " + conversation_prefix

        # Build the conversation string
        convo_str = ""
        for turn in chat_history:
            role = turn["role"]
            text = turn["content"].strip()
            if role == "user":
                convo_str += f"User: {text}\n"
            else:
                convo_str += f"Assistant: {text}\n"

        # The final piece (the very last user message) is already included above as the last "User:" line.
        # So our entire message to Gemini will be:
        full_prompt = conversation_prefix + convo_str

        # 2) Wrap that as a single Content with role="user"
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=full_prompt)]
            )
        ]

        # 3) Create a config
        config = types.GenerateContentConfig(
            temperature=0.2,
            top_p=0.9,
            max_output_tokens=1024,
            safety_settings=SAFETY_SETTINGS,
            response_mime_type="text/plain"
        )

        # 4) Stream the response chunks
        response_text = ""
        for chunk in client.models.generate_content_stream(
            model="gemini-1.5-flash",
            contents=contents,
            config=config
        ):
            response_text += chunk.text or ""

        return response_text.strip() or "⚠️ Gemini did not return a usable answer."

    except Exception as e:
        return f"⚠️ Gemini could not process this request. Error: {str(e)}"
