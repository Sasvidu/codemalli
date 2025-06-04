import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# For sinhala conversions, use the gemini free api to translate English to Sinhala. 
# In the future, I plan to use a local hugging face model for en_to_si conversions.
def send_to_gemini(prompt_text):
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_text
                    }
                ]
            }
        ]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    response.raise_for_status()
    response_json = response.json()
    
    # Extract the text from the response; 
    # usually in 'candidates' -> first element -> 'content' for this API
    generated_text = response_json["candidates"][0]["content"]
    return generated_text

def translate_en_to_si(text):
    prompt = (
        "Translate the following English text into Sinhala:\n\n"
        f"{text}\n\n"
        "Please provide only the Sinhala translation, no extra explanation."
    )
    try:
        translation = send_to_gemini(prompt)
        return translation.strip(), "si"
    except Exception as e:
        print(f"[ERROR] Gemini translation failed: {e}")
        # fallback: return original English text and 'en'
        return text, "en"
